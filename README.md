# 📊 S&P 500 Portfolio Optimization

This project uses 5 years of S&P 500 stock data to build a Markowitz-optimized portfolio using a reproducible data science pipeline.

---

## 🔧 Project Structure
portfolio_project/ ├── all_stocks_5yr.csv # Raw dataset ├── cleaned_data.csv # Preprocessed data ├── features.csv # Engineered features ├── stock_data.db # SQLite database ├── pipeline.py # Main pipeline script ├── requirements.txt # Python dependencies ├── README.md # This file └── scripts/ ├── database_connection.py # DB connector ├── load_data.py # CSV to SQLite ├── preprocess.py # Data cleaning └── feature_engineering.py # Feature extraction

---

## ⚙️ How to Run the Pipeline

1. Create a virtual environment:
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   pip install -r requirements.txt
