import pandas as pd

# Load data
df = pd.read_csv("raw_sales.csv")

# Fix amount column
df["amount"] = pd.to_numeric(df["amount"], errors="coerce")

# Fill missing values
df["amount"] = df["amount"].fillna(0)
df["city"] = df["city"].fillna("Unknown")

# Save cleaned data
df.to_csv("clean_sales.csv", index=False)

print("Cleaning complete!")
print(df)