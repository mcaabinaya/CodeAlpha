import pandas as pd

# Load dataset
df = pd.read_csv("books_dataset.csv")

# Display first 5 rows
print("First 5 Rows:")
print(df.head())

# Dataset shape
print("\nDataset Shape:")
print(df.shape)

# Column names
print("\nColumn Names:")
print(df.columns)

# Data types
print("\nData Types:")
print(df.dtypes)

# Clean Price column
df["Price"] = df["Price"].str.replace("Â£", "", regex=False).astype(float)
# Missing values
print("\nMissing Values:")
print(df.isnull().sum())

# Statistical summary
print("\nStatistical Summary:")
print(df.describe())

# Average price
print("\nAverage Price:")
print(df["Price"].mean())

# Highest price
print("\nHighest Price:")
print(df["Price"].max())

# Lowest price
print("\nLowest Price:")
print(df["Price"].min())

# Rating distribution
print("\nRating Distribution:")
print(df["Rating"].value_counts())