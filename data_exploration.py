"""
Step 1: Data Collection & Exploration
Strategic Product Placement Analysis: Unveiling Sales Impact
"""
import pandas as pd

# Load dataset
df = pd.read_csv("dataset/Product Positioning.csv")

print("=" * 60)
print("STEP 1: DATA COLLECTION & EXPLORATION")
print("=" * 60)

# 1. Basic Info
print("\n--- Dataset Shape ---")
print(f"Rows: {df.shape[0]}, Columns: {df.shape[1]}")

print("\n--- Column Info ---")
print(df.dtypes)

print("\n--- First 5 Rows ---")
print(df.head())

print("\n--- Statistical Summary (Numerical) ---")
print(df.describe())

print("\n--- Statistical Summary (Categorical) ---")
print(df.describe(include='object'))

print("\n--- Missing Values ---")
print(df.isnull().sum())

print("\n--- Duplicate Rows ---")
print(f"Duplicate rows: {df.duplicated().sum()}")

print("\n--- Unique Values per Column ---")
for col in df.columns:
    print(f"  {col}: {df[col].nunique()} unique values")

print("\n--- Value Counts for Categorical Columns ---")
for col in ['Product Position', 'Promotion', 'Foot Traffic', 'Consumer Demographics', 'Product Category', 'Seasonal']:
    print(f"\n  {col}:")
    print(df[col].value_counts().to_string().replace('\n', '\n    '))

print("\n--- Sales Volume by Product Position ---")
print(df.groupby('Product Position')['Sales Volume'].agg(['mean', 'median', 'min', 'max', 'count']))

print("\n--- Price vs Competitor Price Comparison ---")
df['Price Difference'] = df['Price'] - df["Competitor's Price"]
print(f"  Avg Price Difference: {df['Price Difference'].mean():.2f}")
print(f"  Products priced higher than competitor: {(df['Price Difference'] > 0).sum()}")
print(f"  Products priced lower than competitor: {(df['Price Difference'] < 0).sum()}")
print(f"  Products priced equal to competitor: {(df['Price Difference'] == 0).sum()}")

print("\n" + "=" * 60)
print("Data Collection & Exploration COMPLETE")
print("=" * 60)
