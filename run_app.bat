@echo off
echo ============================================
echo E-Shop Streamlit Application Setup
echo ============================================
echo.
echo This batch file will help you set up and run the e-commerce app.
echo.
echo Step 1: Checking for Python...
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo Python is NOT installed. Please install Python from https://www.python.org/downloads/
    echo Make sure to check "Add Python to PATH" during installation.
    pause
    exit /b 1
)
echo Python found!

echo.
echo Step 2: Installing dependencies...
REM ensure pip is up-to-date and install via python -m pip
python -m pip install --upgrade pip >nul 2>&1
python -m pip install -r requirements.txt
if %errorlevel% neq 0 (
    echo Failed to install dependencies. Make sure you have an internet connection and pip is working.
    echo You can also try running "python -m pip install streamlit" manually.
    pause
    exit /b 1
)
echo Dependencies installed successfully!

echo.
echo Step 3: Starting the Streamlit app...
echo The app will open in your browser at http://localhost:8501
echo.
streamlit run app.py
pause
