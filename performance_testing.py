"""
Step 6: Performance Testing & Data Validation
Strategic Product Placement Analysis: Unveiling Sales Impact
Validates data integrity, statistical tests, and analysis accuracy
"""
import pandas as pd
import warnings
warnings.filterwarnings('ignore')

df = pd.read_csv("dataset/Product_Positioning_Cleaned.csv")

print("=" * 60)
print("STEP 6: PERFORMANCE TESTING & DATA VALIDATION")
print("=" * 60)

passed = 0
failed = 0

def test(name, condition):
    global passed, failed
    if condition:
        print(f"  [PASS] {name}")
        passed += 1
    else:
        print(f"  [FAIL] {name}")
        failed += 1

# ============================================================
# TEST 1: Data Integrity Checks
# ============================================================
print("\n--- TEST 1: Data Integrity ---")
test("No missing values", df.isnull().sum().sum() == 0)
test("No duplicate rows", df.duplicated().sum() == 0)
test("No duplicate Product IDs", df['Product_ID'].duplicated().sum() == 0)
test("Dataset has 989 rows", len(df) == 989)
test("Dataset has 14 columns", len(df.columns) == 14)

# ============================================================
# TEST 2: Data Type Validation
# ============================================================
print("\n--- TEST 2: Data Type Validation ---")
test("Product_ID is numeric", df['Product_ID'].dtype in ['int64', 'int32'])
test("Price is numeric", df['Price'].dtype in ['float64', 'float32'])
test("Sales_Volume is numeric", df['Sales_Volume'].dtype in ['int64', 'int32'])
test("Product_Position is string", df['Product_Position'].dtype in ['object', 'str', 'string'])

# ============================================================
# TEST 3: Value Range Validation
# ============================================================
print("\n--- TEST 3: Value Range Validation ---")
test("Price > 0", (df['Price'] > 0).all())
test("Competitor Price >= 0", (df['Competitors_Price'] >= 0).all())
test("Sales Volume > 0", (df['Sales_Volume'] > 0).all())
test("Price Difference calculated correctly", 
     (abs(df['Price_Difference'] - (df['Price'] - df['Competitors_Price'])) < 0.01).all())
test("Price Ratio calculated correctly",
     (abs(df['Price_Ratio'] - (df['Price'] / df['Competitors_Price'])) < 0.001).all())

# ============================================================
# TEST 4: Categorical Value Validation
# ============================================================
print("\n--- TEST 4: Categorical Values ---")
test("Product Position has 3 values", 
     set(df['Product_Position'].unique()) == {'Aisle', 'End-cap', 'Front of Store'})
test("Promotion has 2 values", 
     set(df['Promotion'].unique()) == {'Yes', 'No'})
test("Foot Traffic has 3 values", 
     set(df['Foot_Traffic'].unique()) == {'Low', 'Medium', 'High'})
test("Consumer Demographics has 4 values",
     set(df['Consumer_Demographics'].unique()) == {'Families', 'College students', 'Seniors', 'Young adults'})
test("Product Category has 3 values",
     set(df['Product_Category'].unique()) == {'Clothing', 'Electronics', 'Food'})
test("Seasonal has 2 values",
     set(df['Seasonal'].unique()) == {'Yes', 'No'})

# ============================================================
# TEST 5: Feature Engineering Validation
# ============================================================
print("\n--- TEST 5: Feature Engineering ---")
test("Price_Range categories valid", 
     set(df['Price_Range'].dropna().unique()).issubset({'Low', 'Medium', 'High'}))
test("Sales_Performance categories valid",
     set(df['Sales_Performance'].dropna().unique()).issubset({'Low', 'Medium', 'High'}))

# ============================================================
# TEST 6: Statistical Sanity Checks
# ============================================================
print("\n--- TEST 6: Statistical Sanity ---")
avg_sales = df['Sales_Volume'].mean()
test(f"Average sales in reasonable range (got {avg_sales:.0f})", 
     500 < avg_sales < 5000)

# Sales should be distributed across positions
for pos in ['Aisle', 'End-cap', 'Front of Store']:
    count = len(df[df['Product_Position'] == pos])
    test(f"{pos} has sufficient data ({count} records)", count > 100)

# ============================================================
# TEST 7: Cross-tabulation Consistency
# ============================================================
print("\n--- TEST 7: Cross-tabulation Consistency ---")
total_by_pos = df.groupby('Product_Position')['Sales_Volume'].sum().sum()
total_overall = df['Sales_Volume'].sum()
test("Position group totals match overall total", total_by_pos == total_overall)

total_by_cat = df.groupby('Product_Category')['Sales_Volume'].sum().sum()
test("Category group totals match overall total", total_by_cat == total_overall)

# ============================================================
# TEST 8: Visualization Data Consistency
# ============================================================
print("\n--- TEST 8: Visualization Data Accuracy ---")
# Verify the numbers that will appear in the Tableau dashboard
pos_avg = df.groupby('Product_Position')['Sales_Volume'].mean()
test("Aisle avg sales matches exploration", abs(pos_avg['Aisle'] - 1781) < 20)
test("End-cap avg sales matches exploration", abs(pos_avg['End-cap'] - 1754) < 20)
test("Front of Store avg sales matches exploration", abs(pos_avg['Front of Store'] - 1773) < 20)

# ============================================================
# SUMMARY
# ============================================================
print("\n" + "=" * 60)
print(f"PERFORMANCE TESTING RESULTS")
print(f"  Passed: {passed}")
print(f"  Failed: {failed}")
print(f"  Total:  {passed + failed}")
print(f"  Score:  {passed/(passed+failed)*100:.1f}%")
print("=" * 60)

if failed == 0:
    print("\n  ALL TESTS PASSED! Data is ready for Tableau.")
else:
    print(f"\n  WARNING: {failed} test(s) failed. Review before proceeding.")
