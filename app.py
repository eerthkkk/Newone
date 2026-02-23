import streamlit as st

# Cart system
if "cart" not in st.session_state:
    st.session_state.cart = []

def show_signup():
    st.markdown("""
    <div style='background: #fff; border-radius: 12px; box-shadow: 0 2px 12px #eee; padding: 2rem; max-width: 400px; margin: auto;'>
    """, unsafe_allow_html=True)
    st.header("Sign up")
    new_user = st.text_input("New Username", key="signup_user_modal")
    new_pass = st.text_input("New Password", type="password", key="signup_pass_modal")
    if st.button("Sign up", key="signup_btn_modal"):
        if new_user in st.session_state.USERS:
            st.error("Username already exists")
        elif not new_user or not new_pass:
            st.error("Username and password required")
        else:
            st.session_state.USERS[new_user] = new_pass
            st.success("Sign up successful! Please log in.")
            st.session_state.show_signup = False
    if st.button("Back", key="signup_back_btn"):
        st.session_state.show_signup = False
    st.markdown("</div>", unsafe_allow_html=True)

# Checkout modal
def show_checkout():
    st.markdown("""
    <div style='background: #fff; border-radius: 12px; box-shadow: 0 2px 12px #eee; padding: 2rem; max-width: 500px; margin: auto;'>
    """, unsafe_allow_html=True)
    st.header("Checkout")
    total = sum(item["price"] for item in st.session_state.cart)
    st.write("## Cart Items")
    for item in st.session_state.cart:
        st.write(f"- {item['title']} (${item['price']})")
    st.write(f"### Total: ${total}")
    st.divider()
    st.subheader("Buyer Information")
    buyer_name = st.text_input("Full Name", key="buyer_name")
    buyer_address = st.text_area("Address", key="buyer_address")
    buyer_email = st.text_input("Email", key="buyer_email")
    st.divider()
    if not buyer_name or not buyer_address or not buyer_email:
        st.warning("Please fill in all buyer information before proceeding.")
        st.markdown("</div>", unsafe_allow_html=True)
        return
    payment_method = st.radio("Select payment method", ["Credit Card", "QR Code"])
    if payment_method == "Credit Card":
        st.write("#### Enter Credit Card Details")
        card_num = st.text_input("Card Number")
        card_name = st.text_input("Name on Card")
        card_exp = st.text_input("Expiry Date (MM/YY)")
        card_cvv = st.text_input("CVV")
        if st.button("Pay by Credit Card"):
            st.success("Payment successful! Thank you for your purchase.")
            st.session_state.cart = []
            st.rerun()
    else:
        st.write("#### Scan QR Code to Pay")
        st.image("https://api.qrserver.com/v1/create-qr-code/?data=PAYMENT_DEMO&size=200x200", caption="QR Payment Demo")
        if st.button("Confirm QR Payment"):
            st.success("Payment successful! Thank you for your purchase.")
            st.session_state.cart = []
            st.rerun()
    st.markdown("</div>", unsafe_allow_html=True)

# Streamlit import must be first
import streamlit as st

# User database stored in session state
if "USERS" not in st.session_state:
    st.session_state.USERS = {
        "user1": "pass1",
        "user2": "pass2"
    }
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False
if "username" not in st.session_state:
    st.session_state.username = ""

if not st.session_state.logged_in:
    # Navigation bar with Sign up and Log in buttons
    st.markdown('''
<div class="navbar">🛒 E-Shop | รายการสินค้า | Cart
<button onclick="window.location.href='#'" id="signup-btn" style="float:right;background:#28a745;color:#fff;border:none;padding:0.5rem 1rem;border-radius:4px;margin-left:8px;">สมัครสมาชิก</button>
<button onclick="window.location.href='#'" id="login-btn" style="float:right;background:#007bff;color:#fff;border:none;padding:0.5rem 1rem;border-radius:4px;">เข้าสู่ระบบ</button>
</div>
''', unsafe_allow_html=True)
    if "show_signup" not in st.session_state:
        st.session_state.show_signup = False
    if "show_login" not in st.session_state:
        st.session_state.show_login = True
    # Show signup modal
    if st.session_state.show_signup:
        show_signup()
        st.stop()
    # Show login modal
    if st.session_state.show_login:
        st.markdown("""
        <div style='background: #fff; border-radius: 12px; box-shadow: 0 2px 12px #eee; padding: 2rem; max-width: 400px; margin: auto;'>
        """, unsafe_allow_html=True)
        st.header("Log in")
        username = st.text_input("Username", key="login_user")
        password = st.text_input("Password", type="password", key="login_pass")
        if st.button("Log in"):
            if username in st.session_state.USERS and st.session_state.USERS[username] == password:
                st.session_state.logged_in = True
                st.session_state.username = username
                st.success("Login successful!")
                st.session_state.show_login = False
                st.rerun()
            else:
                st.error("Invalid username or password")
        if st.button("Back", key="login_back_btn"):
            st.session_state.show_login = False
        st.markdown("</div>", unsafe_allow_html=True)
        st.stop()

# Custom CSS for modern look
st.markdown("""
    <style>
    .navbar {background: #222; color: #fff; padding: 1rem; font-size: 1.2rem;}
    .search-bar {margin-bottom: 1rem;}
    .product-card {background: #fff; border-radius: 8px; box-shadow: 0 2px 8px #eee; padding: 1rem; margin-bottom: 1rem;}
    .product-img {width: 100%; height: 180px; object-fit: cover; border-radius: 8px;}
    .add-cart-btn {background: #007bff; color: #fff; border: none; border-radius: 4px; padding: 0.5rem 1rem;}
    .product-title {font-weight: bold; font-size: 1.1rem;}
    .product-price {color: #28a745; font-size: 1rem; margin-bottom: 0.5rem;}
    </style>
""", unsafe_allow_html=True)

# Navigation bar
st.markdown('<div class="navbar">🛒 E-Shop | Home | Products | Cart</div>', unsafe_allow_html=True)

# Sidebar filters
st.sidebar.header("Filters")
st.sidebar.write(f"Logged in as: {st.session_state.username}")
if st.sidebar.button("Logout"):
    st.session_state.logged_in = False
    st.session_state.username = ""
    st.rerun()
category = st.sidebar.selectbox("Category", ["All", "Electronics", "Wearables"])
price_range = st.sidebar.slider("Price Range", 100, 2000, (100, 2000))

# Mock product data
products = [
    {
        "title": "Smart TV",
        "price": 1200,
        "img": "https://images.unsplash.com/photo-1517336714731-489689fd1ca8?auto=format&fit=crop&w=400&q=80",
        "category": "Electronics"
    },
    {
        "title": "Notebook",
        "price": 900,
        "img": "https://images.unsplash.com/photo-1519389950473-47c0e7f7c1b0?auto=format&fit=crop&w=400&q=80",
        "category": "Electronics"
    },
    {
        "title": "Monitor",
        "price": 350,
        "img": "https://images.unsplash.com/photo-1519125323398-675f0ddb6308?auto=format&fit=crop&w=400&q=80",
        "category": "Electronics"
    },
    {
        "title": "Smart Watch",
        "price": 250,
        "img": "https://images.unsplash.com/photo-1516574187841-cb9cc2ca948b?auto=format&fit=crop&w=400&q=80",
        "category": "Wearables"
    }
]

# Search bar
search_query = st.text_input("🔍 Search products...", key="search", help="Type to search products")

# Filter products
filtered_products = [
    p for p in products
    if (category == "All" or p["category"] == category)
    and price_range[0] <= p["price"] <= price_range[1]
    and (search_query.lower() in p["title"].lower() if search_query else True)
]

# Product grid layout
cols = st.columns(2)
for idx, product in enumerate(filtered_products):
    with cols[idx % 2]:
        st.markdown(f"""
<div class="product-card">
    <img src="{product['img']}" class="product-img"/>
    <div class="product-title">{product['title']}</div>
    <div class="product-price">${product['price']}</div>
""", unsafe_allow_html=True)
        if st.button(f"Add to Cart {product['title']}", key=f"cart_{idx}"):
            st.session_state.cart.append(product)
            st.success(f"{product['title']} added to cart!")
        st.markdown("</div>", unsafe_allow_html=True)

# Cart and checkout section
st.sidebar.write("## 🛒 Cart")
if st.session_state.cart:
    for i, item in enumerate(st.session_state.cart):
        st.sidebar.write(f"{item['title']} (${item['price']})")
        if st.sidebar.button(f"Remove {item['title']}", key=f"remove_{i}"):
            st.session_state.cart.pop(i)
            st.rerun()
    st.sidebar.write(f"Total: ${sum(item['price'] for item in st.session_state.cart)}")
    if st.sidebar.button("Checkout"):
        st.session_state.show_checkout = True
else:
    st.sidebar.write("Cart is empty.")

# Show checkout modal if triggered
if "show_checkout" in st.session_state and st.session_state.show_checkout:
    show_checkout()
    st.session_state.show_checkout = False
