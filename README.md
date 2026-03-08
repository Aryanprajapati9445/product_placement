# Strategic Product Placement Analysis: Unveiling Sales Impact

## Project Overview
This data analytics project analyzes the impact of product positioning (Aisle, End-cap, Front of Store) on sales volume, considering factors like pricing, promotions, foot traffic, consumer demographics, product categories, and seasonality.

**Tool Used:** Tableau Desktop + Python (for data preparation & validation)

---

## Dataset Description

| Column | Type | Description |
|--------|------|-------------|
| Product_ID | Integer | Unique product identifier |
| Product_Position | Categorical | Aisle, End-cap, Front of Store |
| Price | Float | Product price ($5.06 - $49.98) |
| Competitors_Price | Float | Competitor's price ($0.72 - $49.85) |
| Promotion | Categorical | Yes / No |
| Foot_Traffic | Categorical | Low / Medium / High |
| Consumer_Demographics | Categorical | Families, College students, Seniors, Young adults |
| Product_Category | Categorical | Clothing, Electronics, Food |
| Seasonal | Categorical | Yes / No |
| Sales_Volume | Integer | Units sold (507 - 2,999) |

**Engineered Features:**
| Column | Description |
|--------|-------------|
| Price_Difference | Price - Competitor's Price |
| Price_Ratio | Price / Competitor's Price |
| Price_Range | Low (0-15), Medium (15-30), High (30-50) |
| Sales_Performance | Low (0-1K), Medium (1K-2K), High (2K-3K) |

**Records:** 989 (after removing 11 duplicate Product IDs)

---

## Project Steps Completed

### Step 1: Data Collection & Exploration
- **File:** `step1_data_exploration.py`
- Loaded CSV dataset (1,000 rows, 10 columns)
- Examined data types, distributions, and summary statistics
- Identified: zero missing values, 11 duplicate Product IDs
- Key finding: Sales fairly evenly distributed across positions

### Step 2: Data Preparation & Cleaning
- **File:** `step2_data_preparation.py`
- **Output:** `dataset/Product_Positioning_Cleaned.csv`
- Removed 11 duplicate Product IDs (989 rows remain)
- Validated all data types and value ranges
- No outliers detected (IQR method)
- Created 4 engineered features
- Standardized column names

### Step 3: Data Visualization
- **File:** `step3_data_visualization.py`
- **Output:** 14 charts in `visualizations/` folder
- Charts created:
  1. Average Sales by Position (Bar)
  2. Sales Distribution by Position (Box Plot)
  3. Sales by Position & Promotion (Grouped Bar)
  4. Sales by Position & Foot Traffic (Grouped Bar)
  5. Heatmap: Category × Position
  6. Heatmap: Demographics × Position
  7. Price vs Sales Scatter Plot
  8. Correlation Matrix
  9. Sales by Demographics (Bar)
  10. Sales by Category (Bar)
  11. Seasonal vs Non-Seasonal Sales
  12. Price Difference Impact on Sales
  13. Multi-Factor Analysis (Position + Traffic + Promotion)
  14. Distribution Pie Charts

### Step 4: Tableau Dashboard Design
- **File:** `step4_dashboard_guide.md`
- 7-sheet dashboard blueprint with layout diagram
- Sheet-by-sheet Tableau instructions
- Interactive filter configuration
- Formatting guidelines

### Step 5: Tableau Story Structure
- **File:** `step5_story_guide.md`
- 7 Story Points designed:
  1. The Business Question
  2. Product Position & Sales Performance
  3. The Category Factor
  4. Demographics Matter
  5. Price & Promotion Effects
  6. The Multi-Factor View
  7. Strategic Recommendations

### Step 6: Performance Testing
- **File:** `step6_performance_testing.py`
- 31 automated tests covering:
  - Data integrity (missing values, duplicates)
  - Data type validation
  - Value range validation
  - Categorical consistency
  - Feature engineering accuracy
  - Statistical sanity checks
  - Cross-tabulation consistency
  - Visualization data accuracy
- **Result: 31/31 PASSED (100%)**

### Step 7: Web Integration
- **File:** `step7_web_integration_guide.md`
- Tableau Public publishing instructions
- Website embedding guide
- Sharing options & best practices

### Step 8: Project Documentation
- **File:** `README.md` (this file)

---

## Key Findings

1. **Position Impact:** All three positions show similar average sales (~1,768), suggesting position alone is not the primary sales driver
2. **Pricing:** 99.9% of products are priced higher than competitors (avg +$2.47)
3. **Data Balance:** Categories, demographics, and traffic levels are well-distributed across the dataset
4. **Multi-Factor:** The interaction between position, promotion, foot traffic, and demographics creates nuanced patterns that require multi-dimensional analysis

---

## Project Structure

```
DA_project/
├── dataset/
│   ├── Product Positioning.csv          # Original dataset
│   └── Product_Positioning_Cleaned.csv  # Cleaned dataset
├── visualizations/
│   ├── 01_sales_by_position.png
│   ├── 02_sales_distribution_boxplot.png
│   ├── 03_sales_position_promotion.png
│   ├── 04_sales_position_traffic.png
│   ├── 05_heatmap_category_position.png
│   ├── 06_heatmap_demographics_position.png
│   ├── 07_price_vs_sales_scatter.png
│   ├── 08_correlation_heatmap.png
│   ├── 09_sales_by_demographics.png
│   ├── 10_sales_by_category.png
│   ├── 11_seasonal_sales.png
│   ├── 12_price_diff_vs_sales.png
│   ├── 13_multi_factor_analysis.png
│   └── 14_distribution_pies.png
├── step1_data_exploration.py
├── step2_data_preparation.py
├── step3_data_visualization.py
├── step4_dashboard_guide.md
├── step5_story_guide.md
├── step6_performance_testing.py
├── step7_web_integration_guide.md
└── README.md
```

---

## How to Reproduce

1. Install Python dependencies: `pip install pandas matplotlib seaborn`
2. Run steps in order:
   ```
   python step1_data_exploration.py
   python step2_data_preparation.py
   python step3_data_visualization.py
   python step6_performance_testing.py
   ```
3. Open `dataset/Product_Positioning_Cleaned.csv` in Tableau
4. Follow `step4_dashboard_guide.md` to build dashboard
5. Follow `step5_story_guide.md` to build story
6. Follow `step7_web_integration_guide.md` to publish

---

**Date:** March 8, 2026  
**Tool:** Tableau Desktop + Python 3.13
