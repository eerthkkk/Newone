import streamlit as st

# Initialize session state
if "cart" not in st.session_state:
    st.session_state.cart = []
# USERS now stores dicts with password & admin flag
if "USERS" not in st.session_state:
    st.session_state.USERS = {
        "user1": {"password": "pass1", "is_admin": False},
        "admin": {"password": "adminpass", "is_admin": True}
    }
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False
if "username" not in st.session_state:
    st.session_state.username = ""
if "is_admin" not in st.session_state:
    st.session_state.is_admin = False
# control which modal/panel is visible
if "show_signup" not in st.session_state:
    st.session_state.show_signup = False
if "show_login" not in st.session_state:
    st.session_state.show_login = False
if "show_checkout" not in st.session_state:
    st.session_state.show_checkout = False
if "show_admin" not in st.session_state:
    st.session_state.show_admin = False
# store products in session state for dynamic admin edits
if "PRODUCTS" not in st.session_state:
    st.session_state.PRODUCTS = [
        {
            "title": "Smart TV",
            "price": 1200,
            "img": "https://images.unsplash.com/photo-1517336714731-489689fd1ca8?auto=format&fit=crop&w=400&q=80",
            "category": "Electronics"
        },
        {
            "title": "Notebook",
            "price": 900,
            "img": "https://images.unsplash.com/photo-1519389950473-47c0e7f9de74?auto=format&fit=crop&w=400&q=80",
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

# Product database
PRODUCTS = [
    {
        "title": "Smart TV",
        "price": 1200,
        "img": "https://images.unsplash.com/photo-1517336714731-489689fd1ca8?auto=format&fit=crop&w=400&q=80",
        "category": "Electronics"
    },
    {
        "title": "Notebook",
        "price": 900,
        "img": "https://images.unsplash.com/photo-1519389950473-47c0e7f9de74?auto=format&fit=crop&w=400&q=80",
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

def show_signup():
    # display signup inside a modal
    with st.modal("Sign up"):
        new_user = st.text_input("New Username", key="signup_user_modal")
        new_pass = st.text_input("New Password", type="password", key="signup_pass_modal")

        col1, col2 = st.columns(2)
        with col1:
            if st.button("Sign up", key="signup_btn_modal"):
                if new_user in st.session_state.USERS:
                    st.error("Username already exists")
                elif not new_user or not new_pass:
                    st.error("Username and password required")
                else:
                    st.session_state.USERS[new_user] = {"password": new_pass, "is_admin": False}
                    st.success("Sign up successful! Please log in.")
                    st.session_state.show_signup = False
                    st.session_state.show_login = True
                    st.rerun()
        with col2:
            if st.button("Back", key="signup_back_btn"):
                st.session_state.show_signup = False
                st.session_state.show_login = False
                st.rerun()


def show_login():
    with st.modal("Log in"):
        username = st.text_input("Username", key="login_user")
        password = st.text_input("Password", type="password", key="login_pass")
        col1, col2 = st.columns(2)
        with col1:
            if st.button("Log in", key="login_btn"):
                user = st.session_state.USERS.get(username)
                if user and user.get("password") == password:
                    st.session_state.logged_in = True
                    st.session_state.username = username
                    st.session_state.is_admin = user.get("is_admin", False)
                    st.session_state.show_login = False
                    st.success("Login successful!")
                    st.rerun()
                else:
                    st.error("Invalid username or password")
        with col2:
            if st.button("Sign up", key="show_signup_btn"):
                st.session_state.show_signup = True
                st.session_state.show_login = False
                st.rerun()

def show_checkout():
    st.markdown("""
    <div style='background: #fff; border-radius: 12px; box-shadow: 0 2px 12px #eee; padding: 2rem; max-width: 500px; margin: auto;'>
    """, unsafe_allow_html=True)
    st.header("Checkout")
    
    if not st.session_state.cart:
        st.warning("Your cart is empty!")
        st.markdown("</div>", unsafe_allow_html=True)
        return
    
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
        card_num = st.text_input("Card Number", type="password")
        card_name = st.text_input("Name on Card")
        card_exp = st.text_input("Expiry Date (MM/YY)")
        card_cvv = st.text_input("CVV", type="password")
        if st.button("Pay by Credit Card"):
            st.success("Payment successful! Thank you for your purchase.")
            st.session_state.cart = []
            st.session_state.show_checkout = False
            st.rerun()
    else:
        st.write("#### Scan QR Code to Pay")
        st.image("https://api.qrserver.com/v1/create-qr-code/?data=PAYMENT_DEMO&size=200x200", caption="QR Payment Demo")
        if st.button("Confirm QR Payment"):
            st.success("Payment successful! Thank you for your purchase.")
            st.session_state.cart = []
            st.session_state.show_checkout = False
            st.rerun()
    
    st.markdown("</div>", unsafe_allow_html=True)

# CSS Styling (updated for modern look)
st.markdown("""
    <style>
    .navbar {background: linear-gradient(90deg, #4b6cb7, #182848); color: #fff; padding: 1rem 2rem; font-size: 1.4rem; display:flex; justify-content: space-between; align-items:center;}
    .nav-button {background:#fff; color:#182848; border:none; padding:0.4rem 1rem; border-radius:5px; cursor:pointer; margin-left:0.5rem;}
    .product-card {background: #fff; border-radius: 12px; box-shadow: 0 4px 12px rgba(0,0,0,0.1); padding: 1rem; margin-bottom: 1rem;}
    .product-img {width: 100%; height: 200px; object-fit: cover; border-radius: 8px;}
    .product-title {font-weight: bold; font-size: 1.2rem; margin-top: 0.5rem;}
    .product-price {color: #e55353; font-size: 1.3rem; margin-bottom: 0.5rem; font-weight: bold;}
    </style>
""", unsafe_allow_html=True)

# navigation area
with st.container():
    cols = st.columns([3,1,1,1])
    cols[0].markdown("<h2 style='margin:0;'>🛒 E-Shop</h2>", unsafe_allow_html=True)
    if st.session_state.logged_in:
        cols[1].markdown(f"<span>Welcome, <b>{st.session_state.username}</b></span>", unsafe_allow_html=True)
        if cols[2].button("Logout"):
            st.session_state.logged_in = False
            st.session_state.username = ""
            st.session_state.is_admin = False
            st.session_state.cart = []
            st.session_state.show_admin = False
            st.rerun()
        if st.session_state.is_admin:
            if cols[3].button("Admin"):
                st.session_state.show_admin = True
    else:
        if cols[1].button("Log In"):
            st.session_state.show_login = True
        if cols[2].button("Sign Up"):
            st.session_state.show_signup = True

# display modals/panels
if st.session_state.show_login:
    show_login()
if st.session_state.show_signup:
    show_signup()

# admin panel
if st.session_state.logged_in and st.session_state.is_admin and st.session_state.show_admin:
    def show_admin_panel():
        st.header("Admin Dashboard")
        st.subheader("Add / Remove Products")
        tcol1, tcol2 = st.columns(2)
        title = tcol1.text_input("Title", key="admin_title")
        price = tcol1.number_input("Price", min_value=0.0, step=0.01, key="admin_price")
        img = tcol1.text_input("Image URL", key="admin_img")
        category = tcol1.text_input("Category", key="admin_cat")
        if tcol2.button("Add Product", key="admin_add"):
            if title and price and img:
                st.session_state.PRODUCTS.append({
                    "title": title,
                    "price": price,
                    "img": img,
                    "category": category or "Misc"
                })
                st.success("Product added.")
                st.rerun()
        st.divider()
        st.subheader("Existing Products")
        for i, p in enumerate(st.session_state.PRODUCTS):
            colA, colB = st.columns([8,2])
            colA.write(f"{p['title']} – ${p['price']} ({p.get('category','')})")
            if colB.button("Remove", key=f"admin_remove_{i}"):
                st.session_state.PRODUCTS.pop(i)
                st.rerun()
    show_admin_panel()
else:
    # product listing (available to everyone)
    # build filters in sidebar
    st.sidebar.header("Filters")
    category = st.sidebar.selectbox("Category", ["All"] + sorted({p.get("category","") for p in st.session_state.PRODUCTS}))
    price_range = st.sidebar.slider("Price Range", 0, 2000, (0, 2000))
    
    # search bar
    search_query = st.text_input("🔍 Search products...")
    
    # compute filtered list
    filtered_products = [
        p for p in st.session_state.PRODUCTS
        if (category == "All" or p.get("category") == category)
        and price_range[0] <= p.get("price",0) <= price_range[1]
        and (search_query.lower() in p.get("title","").lower() if search_query else True)
    ]
    
    if st.session_state.show_checkout:
        # require login to checkout
        if not st.session_state.logged_in:
            st.warning("Please log in before checking out.")
            st.session_state.show_checkout = False
        else:
            show_checkout()
    else:
        st.header("Products")
        if filtered_products:
            cols = st.columns(2)
            for idx, product in enumerate(filtered_products):
                with cols[idx % 2]:
                    st.markdown(f"""
                    <div class="product-card">
                        <img src="{product.get('img','')}" class="product-img"/>
                        <div class="product-title">{product.get('title','')}</div>
                        <div class="product-price">${product.get('price','')}</div>
                    """, unsafe_allow_html=True)
                    if st.button("Add to Cart", key=f"cart_{idx}"):
                        if not st.session_state.logged_in:
                            st.warning("You must log in to add items to the cart.")
                        else:
                            st.session_state.cart.append(product)
                            st.success(f"{product.get('title')} added to cart!")
                    st.markdown("</div>", unsafe_allow_html=True)
        else:
            st.warning("No products found matching your filters.")
        
        # cart sidebar (only when logged-in)
        st.sidebar.header("🛒 Shopping Cart")
        if st.session_state.cart:
            for i, item in enumerate(st.session_state.cart):
                st.sidebar.write(f"• {item.get('title')} - ${item.get('price')}")
                if st.sidebar.button(f"Remove", key=f"remove_{i}"):
                    st.session_state.cart.pop(i)
                    st.rerun()
            total = sum(item.get('price',0) for item in st.session_state.cart)
            st.sidebar.write(f"**Total: ${total}**")
            if st.sidebar.button("Proceed to Checkout"):
                st.session_state.show_checkout = True
                st.rerun()
        else:
            st.sidebar.write("Your cart is empty.")
