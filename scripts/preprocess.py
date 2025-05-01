import pandas as pd
from database_connection import get_engine

engine = get_engine()
df = pd.read_sql("SELECT * FROM stock_prices", con=engine)

df['date'] = pd.to_datetime(df['date'])
df = df.sort_values(by=['Name', 'date'])
df = df.dropna()
df.to_csv("cleaned_data.csv", index=False)

print("Preprocessing complete. Cleaned data saved to 'cleaned_data.csv'")
