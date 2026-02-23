import streamlit as st

# Mock product data
products = [
    {
        "title": "Smart TV",
        "price": 499.99,
        "image": "https://images.unsplash.com/photo-1517336714731-489689fd1ca8?auto=format&fit=crop&w=400&q=80",
    },
    {
        "title": "Notebook",
        "price": 899.99,
        "image": "https://images.unsplash.com/photo-1519389950473-47c0e7f9de74?auto=format&fit=crop&w=400&q=80",
    },
    {
        "title": "Monitor",
        "price": 199.99,
        "image": "https://images.unsplash.com/photo-1519125323398-675f0ddb6308?auto=format&fit=crop&w=400&q=80",
    },
    {
        "title": "Smart Watch",
        "price": 149.99,
        "image": "https://images.unsplash.com/photo-1516574187841-cb9cc2ca948b?auto=format&fit=crop&w=400&q=80",
    },
]

# Custom CSS for styling
st.markdown(
    """
    <style>
    .navbar {
        background: #fff;
        padding: 1rem 2rem;
        border-bottom: 1px solid #eee;
        display: flex;
        justify-content: space-between;
        align-items: center;
    }
    .search-bar {
        width: 300px;
        padding: 0.5rem;
        border-radius: 5px;
        border: 1px solid #ccc;
    }
    .product-grid {
        display: flex;
        flex-wrap: wrap;
        gap: 2rem;
        justify-content: flex-start;
    }
    .product-card {
        background: #fff;
        border-radius: 10px;
        box-shadow: 0 2px 8px rgba(0,0,0,0.05);
        padding: 1rem;
        width: 250px;
        text-align: center;
    }
    .product-card img {
        width: 100%;
        height: 150px;
        object-fit: cover;
        border-radius: 8px;
    }
    .add-cart-btn {
        background: #007bff;
        color: #fff;
        border: none;
        padding: 0.5rem 1rem;
        border-radius: 5px;
        cursor: pointer;
        margin-top: 0.5rem;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# Navigation bar
st.markdown(
    """
    <div class="navbar">
        <div><b>ShopEasy</b></div>
        <form>
            <input class="search-bar" type="text" placeholder="Search products..." name="search">
        </form>
    </div>
    """,
    unsafe_allow_html=True,
)

# Sidebar filters
st.sidebar.header("Filters")
st.sidebar.selectbox("Category", ["All", "Electronics", "Wearables", "Computers"])
st.sidebar.slider("Price Range", 0, 1000, (0, 1000))

# Search functionality
search_query = st.text_input("", "", key="search_input", placeholder="Search products...")

filtered_products = [
    p for p in products
    if search_query.lower() in p["title"].lower()
]

# Product grid layout
st.markdown('<div class="product-grid">', unsafe_allow_html=True)
for p in filtered_products:
    st.markdown(f'''
        <div class="product-card">
            <img src="{p['image']}" alt="{p['title']}">
            <h4>{p['title']}</h4>
            <p><b>${p['price']:.2f}</b></p>
            <form action="#">
                <button class="add-cart-btn">Add to Cart</button>
            </form>
        </div>
    ''', unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)
