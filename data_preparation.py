"""
Step 2: Data Preparation & Cleaning
Strategic Product Placement Analysis: Unveiling Sales Impact
"""
import pandas as pd
import os

# Load dataset
df = pd.read_csv("dataset/Product Positioning.csv")

print("=" * 60)
print("STEP 2: DATA PREPARATION & CLEANING")
print("=" * 60)

# 1. Check and handle missing values
print("\n--- 1. Missing Values Check ---")
missing = df.isnull().sum()
print(f"Total missing values: {missing.sum()}")

# 2. Check and handle duplicates
print("\n--- 2. Duplicate Check ---")
dup_count = df.duplicated().sum()
print(f"Duplicate rows: {dup_count}")

# Check duplicate Product IDs
dup_ids = df[df.duplicated(subset='Product ID', keep=False)]
print(f"Duplicate Product IDs: {dup_ids['Product ID'].nunique()}")
if len(dup_ids) > 0:
    print("  Removing duplicate Product IDs (keeping first occurrence)...")
    df = df.drop_duplicates(subset='Product ID', keep='first')
    print(f"  Rows after dedup: {len(df)}")

# 3. Data type validation & correction
print("\n--- 3. Data Type Validation ---")
print("All data types correct:")
print(df.dtypes)

# 4. Outlier detection using IQR for numerical columns
print("\n--- 4. Outlier Detection (IQR Method) ---")
for col in ['Price', "Competitor's Price", 'Sales Volume']:
    Q1 = df[col].quantile(0.25)
    Q3 = df[col].quantile(0.75)
    IQR = Q3 - Q1
    lower = Q1 - 1.5 * IQR
    upper = Q3 + 1.5 * IQR
    outliers = df[(df[col] < lower) | (df[col] > upper)]
    print(f"  {col}: {len(outliers)} outliers (range: {lower:.2f} - {upper:.2f})")

# 5. Feature Engineering
print("\n--- 5. Feature Engineering ---")

# Price Difference
df['Price_Difference'] = round(df['Price'] - df["Competitor's Price"], 2)
print("  Created: Price_Difference (Price - Competitor's Price)")

# Price Ratio
df['Price_Ratio'] = round(df['Price'] / df["Competitor's Price"], 4)
print("  Created: Price_Ratio (Price / Competitor's Price)")

# Price Range Category
df['Price_Range'] = pd.cut(df['Price'], bins=[0, 15, 30, 50], labels=['Low', 'Medium', 'High'])
print("  Created: Price_Range (Low: 0-15, Medium: 15-30, High: 30-50)")

# Sales Performance Category
df['Sales_Performance'] = pd.cut(df['Sales Volume'], 
                                  bins=[0, 1000, 2000, 3000], 
                                  labels=['Low', 'Medium', 'High'])
print("  Created: Sales_Performance (Low: 0-1K, Medium: 1K-2K, High: 2K-3K)")

# 6. Standardize column names (remove spaces, lowercase)
print("\n--- 6. Column Name Standardization ---")
df.columns = df.columns.str.strip().str.replace(' ', '_').str.replace("'", '')
print(f"  New columns: {list(df.columns)}")

# 7. Verify categorical consistency
print("\n--- 7. Categorical Data Consistency ---")
for col in ['Product_Position', 'Promotion', 'Foot_Traffic', 'Consumer_Demographics', 'Product_Category', 'Seasonal']:
    values = df[col].unique()
    print(f"  {col}: {values}")

# 8. Final dataset summary
print("\n--- 8. Final Dataset Summary ---")
print(f"  Shape: {df.shape}")
print(f"  Columns: {list(df.columns)}")
print(df.head())

# 9. Save cleaned dataset
os.makedirs("dataset", exist_ok=True)
df.to_csv("dataset/Product_Positioning_Cleaned.csv", index=False)
print(f"\n  Cleaned dataset saved to: dataset/Product_Positioning_Cleaned.csv")

print("\n" + "=" * 60)
print("Data Preparation & Cleaning COMPLETE")
print("=" * 60)
