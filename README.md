# E-Shop Streamlit Application

A modern e-commerce web application built with Streamlit.

## Features

- ✅ **User authentication** (login/signup via modal dialogs)
- 🛍️ Product catalog shown on the home page with cards, filters and search
- 🔍 Live product search and category/price filters
- 🛒 Shopping cart and checkout flow (login required to add items)
- 💳 Checkout with mock payment options (Credit Card & QR Code)
- 👩‍💼 **Admin backend** for managing products (add/remove)
- 📱 Responsive and modern UI with navbar and styled components

## Prerequisites

- **Python 3.8 or higher** - [Download here](https://www.python.org/downloads/)
- During Python installation, make sure to check **"Add Python to PATH"**

## Installation & Setup

### Option 1: Automatic Setup (Easy)
Simply double-click `run_app.bat` - it will install dependencies and start the app.

### Option 2: Manual Setup
1. Open Command Prompt or PowerShell in this folder
2. (Optional but recommended) create and activate a virtual environment:
   ```powershell
   python -m venv .venv           # creates folder .venv
   .\.venv\Scripts\activate     # activate in PowerShell
   # or use `source .venv/bin/activate` on macOS/Linux
   ```
3. Install dependencies:
   ```powershell
   python -m pip install --upgrade pip
   python -m pip install -r requirements.txt
   ```
   If you see an error saying `streamlit` not found, run
   `python -m pip install streamlit` manually.
4. Run the app:
   ```powershell
   streamlit run app.py
   ```
   or equivalently
   `python -m streamlit run app.py`

## Running the App

Once dependencies are installed, start the app with:
```
streamlit run app.py
```

The app will open automatically at `http://localhost:8501`

## Test Credentials

You can log in with one of the built‑in accounts:

- **Username:** user1  | **Password:** pass1  (regular user)
- **Username:** admin  | **Password:** adminpass  (administrator)

Or create a new normal account using the **Sign Up** button.

Administrators can access an **Admin** button in the navbar after logging in; the panel allows adding and removing products.

## Available Products

1. **Smart TV** - $1,200 (Electronics)
2. **Notebook** - $900 (Electronics)
3. **Monitor** - $350 (Electronics)
4. **Smart Watch** - $250 (Wearables)

## How to Use

1. **Sign Up / Log In** - Create an account or use test credentials
2. **Browse Products** - Browse the catalog with filters and search
3. **Add to Cart** - Click "Add to Cart" on any product
4. **Checkout** - Review your cart and proceed to payment
5. **Payment** - Choose between Credit Card or QR Code payment

## Troubleshooting

### Python not found
- Install Python from https://www.python.org/downloads/
- Make sure to check "Add Python to PATH"

### Streamlit not found
Run: `pip install -r requirements.txt`

### Port already in use
Run: `streamlit run app.py --server.port 8502`

## Project Files

- `app.py` - Main Streamlit application
- `ecommerce_app.py` - Alternative e-commerce template
- `requirements.txt` - Python dependencies
- `run_app.bat` - Batch script for easy setup and running

## Deployment

This project is built with Streamlit and can be hosted on any service that supports Python applications. The easiest way to make your e-shop available on the web is to use [Streamlit Cloud](https://streamlit.io/cloud), which will provide you with a permanent URL that you can share.

### Deploying to Streamlit Cloud
1. Push the repository to GitHub (public or private).
2. Log in at https://streamlit.io/cloud and click **New app**.
3. Select the repo, branch and entry point `app.py`.
4. Click **Deploy**. After a minute the live app will open and you will have a link like:
   `https://share.streamlit.io/<your‑username>/<repo‑name>/main/app.py`
5. Share that URL with customers and friends.

> Example (replace with your own once deployed):
> `https://share.streamlit.io/yourname/Newone1/main/app.py`

You can also deploy to other platforms such as Heroku, AWS, or Azure by using a `Procfile` or containerizing the app. A simple `Procfile` would look like:
```
web: streamlit run app.py --server.port=$PORT
```

## notes

- Cart data is temporary and resets when you log out
- User accounts are stored in session (not persistent)
- Images are fetched from Unsplash
