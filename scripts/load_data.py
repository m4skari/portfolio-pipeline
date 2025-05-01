import pandas as pd
from sqlalchemy import create_engine
from database_connection import get_engine

# Read the CSV
df = pd.read_csv("all_stocks_5yr.csv")
df.dropna(inplace=True)

# Fix date column type
df['date'] = pd.to_datetime(df['date'])

# Connect to SQLite
engine = get_engine()

# Load into SQLite
df.to_sql('stock_prices', con=engine, if_exists='replace', index=False)

print("Data loaded into 'stock_prices' table in stock_data.db")
