import pandas as pd
import numpy as np

# Load cleaned data
df = pd.read_csv("cleaned_data.csv")

# Sort by stock and date
df = df.sort_values(by=["Name", "date"])

# Daily return
df['daily_return'] = df.groupby('Name')['close'].pct_change()

# Log return
df['log_return'] = np.log(df['close'] / df['close'].shift(1))

# 20-day rolling volatility (std deviation of returns)
df['volatility_20d'] = df.groupby('Name')['daily_return'].rolling(window=20).std().reset_index(0, drop=True)

# 20-day rolling mean return
df['mean_return_20d'] = df.groupby('Name')['daily_return'].rolling(window=20).mean().reset_index(0, drop=True)

# Drop rows with NaN (first 20 rows of each group will have NaNs)
df.dropna(inplace=True)

# Save to CSV
df.to_csv("features.csv", index=False)

print("✅ Feature engineering complete. Saved to 'features.csv'")
