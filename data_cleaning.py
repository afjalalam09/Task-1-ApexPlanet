import pandas as pd

# Load dataset
df = pd.read_csv("raw_data.csv")

# Check missing values and duplicates
print(df.isnull().sum())
print(df.duplicated().sum())

# Remove duplicates
df = df.drop_duplicates()

# Fill missing sales with median
if 'Sales' in df.columns:
    df['Sales'] = df['Sales'].fillna(df['Sales'].median())

# Convert date column
if 'Order_Date' in df.columns:
    df['Order_Date'] = pd.to_datetime(df['Order_Date'])
    df['Order_Year'] = df['Order_Date'].dt.year

# Save cleaned data
df.to_csv("cleaned_data.csv", index=False)
