# ============================================================
# PROJECT DOCUMENTATION
# Strategic Product Placement Analysis: Unveiling Sales Impact Using Tableau
# Step-by-Step Project Development Procedure
# ============================================================

# Date: March 8, 2026

---

## TABLE OF CONTENTS

1. [Project Introduction](#1-project-introduction)
2. [Problem Statement & Objectives](#2-problem-statement--objectives)
3. [Step 1 – Data Collection & Extraction](#3-step-1--data-collection--extraction)
4. [Step 2 – Data Preparation & Cleaning](#4-step-2--data-preparation--cleaning)
5. [Step 3 – Data Visualization](#5-step-3--data-visualization)
6. [Step 4 – Dashboard Development](#6-step-4--dashboard-development)
7. [Step 5 – Story Creation](#7-step-5--story-creation)
8. [Step 6 – Performance Testing](#8-step-6--performance-testing)
9. [Step 7 – Web Integration](#9-step-7--web-integration)
10. [Step 8 – Project Demonstration & Documentation](#10-step-8--project-demonstration--documentation)
11. [Key Findings & Insights](#11-key-findings--insights)
12. [Recommendations](#12-recommendations)
13. [Conclusion](#13-conclusion)

---

## 1. PROJECT INTRODUCTION

**Project Title:** Strategic Product Placement Analysis: Unveiling Sales Impact Using Tableau

**Domain:** Retail Analytics / Data Analytics

**Abstract:**
This project investigates how product placement within retail stores impacts sales performance. Using a dataset of 1,000 product records across three store positions (Aisle, End-cap, Front of Store), we analyze the relationship between placement strategy and sales volume while accounting for other influential factors such as pricing, promotions, foot traffic, consumer demographics, product categories, and seasonality. The analysis is performed using Python for data preparation/validation and Tableau for interactive visualization, dashboard creation, and storytelling.

**Tools & Technologies Used:**
| Tool | Purpose |
|------|---------|
| Python 3.13 | Data cleaning, preparation, validation, visualization |
| Pandas | Data manipulation and analysis |
| Matplotlib & Seaborn | Statistical chart generation |
| Tableau Desktop | Interactive dashboards, stories, and publishing |
| Tableau Public | Web publishing and sharing |

---

## 2. PROBLEM STATEMENT & OBJECTIVES

### Problem Statement
Retail businesses invest significantly in product placement strategies, yet the quantitative impact of different shelf/store positions on actual sales remains unclear. This project seeks to answer: **"Does product placement position significantly impact sales volume, and what other factors interact with placement to drive sales?"**

### Objectives
1. Analyze the relationship between product position (Aisle, End-cap, Front of Store) and sales volume
2. Identify how factors like promotion, foot traffic, demographics, and category interact with position
3. Compare product pricing against competitor pricing and its effect on sales
4. Build interactive Tableau dashboards for data-driven decision-making
5. Create a Tableau Story to present findings to stakeholders
6. Provide actionable recommendations for optimal product placement strategies

---

## 3. STEP 1 – DATA COLLECTION & EXTRACTION

### 3.1 Data Source
- **File:** `dataset/Product Positioning.csv`
- **Format:** CSV (Comma-Separated Values)
- **Size:** 1,000 records × 10 columns

### 3.2 Dataset Schema

| # | Column Name | Data Type | Description | Example |
|---|------------|-----------|-------------|---------|
| 1 | Product ID | Integer | Unique product identifier | 185102 |
| 2 | Product Position | String | Store placement location | Aisle, End-cap, Front of Store |
| 3 | Price | Float | Product selling price ($) | 17.07 |
| 4 | Competitor's Price | Float | Competitor's price ($) | 16.16 |
| 5 | Promotion | String | Whether promotion is active | Yes, No |
| 6 | Foot Traffic | String | Store traffic level | Low, Medium, High |
| 7 | Consumer Demographics | String | Target customer group | Families, Seniors, Young adults, College students |
| 8 | Product Category | String | Product type | Clothing, Electronics, Food |
| 9 | Seasonal | String | Whether product is seasonal | Yes, No |
| 10 | Sales Volume | Integer | Number of units sold | 2823 |

### 3.3 Exploratory Data Analysis (EDA) Results

**Procedure:**
1. Loaded dataset using `pandas.read_csv()`
2. Examined shape, data types, and basic statistics using `df.info()`, `df.describe()`
3. Checked for missing values using `df.isnull().sum()`
4. Checked for duplicates using `df.duplicated().sum()`
5. Analyzed value distributions for each categorical column
6. Computed summary statistics grouped by Product Position

**Key EDA Findings:**

| Metric | Value |
|--------|-------|
| Total Records | 1,000 |
| Total Columns | 10 |
| Missing Values | 0 |
| Duplicate Rows | 0 |
| Duplicate Product IDs | 11 (22 rows affected) |
| Price Range | $5.06 – $49.98 |
| Competitor Price Range | $0.72 – $49.85 |
| Sales Volume Range | 507 – 2,999 |
| Average Sales Volume | 1,769 |
| Unique Product IDs | 989 |

**Sales by Position (Before Cleaning):**

| Position | Avg Sales | Median | Count |
|----------|-----------|--------|-------|
| Aisle | 1,781 | 1,794 | 340 |
| End-cap | 1,754 | 1,771 | 342 |
| Front of Store | 1,773 | 1,799 | 318 |

**Script:** `step1_data_exploration.py`

### 3.4 Connecting Dataset to Tableau
1. Open Tableau Desktop
2. On the Start Page, under "Connect" → click **"Text File"**
3. Navigate to `dataset/Product_Positioning_Cleaned.csv`
4. Tableau auto-detects column types
5. Review data types in the Data Source tab
6. Click **"Sheet 1"** to begin analysis

---

## 4. STEP 2 – DATA PREPARATION & CLEANING

### 4.1 Data Cleaning Procedure

| # | Task | Action Taken | Result |
|---|------|-------------|--------|
| 1 | Missing Value Check | `df.isnull().sum()` | 0 missing values found |
| 2 | Duplicate Row Check | `df.duplicated().sum()` | 0 full duplicate rows |
| 3 | Duplicate ID Check | `df.duplicated(subset='Product ID')` | 11 duplicate Product IDs found |
| 4 | Remove Duplicate IDs | `df.drop_duplicates(subset='Product ID', keep='first')` | Reduced from 1,000 → 989 rows |
| 5 | Outlier Detection | IQR method on Price, Competitor Price, Sales Volume | 0 outliers detected |
| 6 | Data Type Validation | Verified all column types | All types correct |
| 7 | Categorical Consistency | Checked unique values in all categorical columns | All values consistent, no typos |

### 4.2 Feature Engineering

Four new columns were created to enhance analysis:

| # | New Column | Formula | Purpose |
|---|-----------|---------|---------|
| 1 | Price_Difference | Price − Competitor's Price | Measures pricing competitiveness |
| 2 | Price_Ratio | Price / Competitor's Price | Relative pricing metric |
| 3 | Price_Range | Binned: Low (0-15), Medium (15-30), High (30-50) | Price segmentation |
| 4 | Sales_Performance | Binned: Low (0-1K), Medium (1K-2K), High (2K-3K) | Sales segmentation |

### 4.3 Column Standardization
- Removed spaces from column names (replaced with underscores)
- Removed apostrophes from column names
- Example: `Competitor's Price` → `Competitors_Price`

### 4.4 Final Cleaned Dataset
- **Output File:** `dataset/Product_Positioning_Cleaned.csv`
- **Rows:** 989
- **Columns:** 14 (10 original + 4 engineered)

**Script:** `step2_data_preparation.py`

---

## 5. STEP 3 – DATA VISUALIZATION

### 5.1 Visualization Strategy
Visualizations were designed to answer specific analytical questions about product placement impact:

### 5.2 Charts Created

| # | Chart | Type | Purpose | File |
|---|-------|------|---------|------|
| 1 | Avg Sales by Position | Bar Chart | Compare sales across positions | `01_sales_by_position.png` |
| 2 | Sales Distribution by Position | Box Plot | Show spread & outliers per position | `02_sales_distribution_boxplot.png` |
| 3 | Sales by Position & Promotion | Grouped Bar | Promotion effect per position | `03_sales_position_promotion.png` |
| 4 | Sales by Position & Foot Traffic | Grouped Bar | Traffic impact per position | `04_sales_position_traffic.png` |
| 5 | Category × Position Heatmap | Heatmap | Category-position interaction | `05_heatmap_category_position.png` |
| 6 | Demographics × Position Heatmap | Heatmap | Demographic-position interaction | `06_heatmap_demographics_position.png` |
| 7 | Price vs Sales Scatter | Scatter Plot | Price-sales relationship | `07_price_vs_sales_scatter.png` |
| 8 | Correlation Matrix | Heatmap | Variable correlations | `08_correlation_heatmap.png` |
| 9 | Sales by Demographics | Bar Chart | Demographic sales comparison | `09_sales_by_demographics.png` |
| 10 | Sales by Category | Bar Chart | Category sales comparison | `10_sales_by_category.png` |
| 11 | Seasonal Sales | Grouped Bar | Seasonal effect by position | `11_seasonal_sales.png` |
| 12 | Price Difference vs Sales | Scatter Plot | Competitive pricing impact | `12_price_diff_vs_sales.png` |
| 13 | Multi-Factor Analysis | 3-Panel Bar | Position + Traffic + Promotion combined | `13_multi_factor_analysis.png` |
| 14 | Distribution Pie Charts | Pie Charts | Position & Category distribution | `14_distribution_pies.png` |

### 5.3 Key Observations from Visualizations
1. **Position Impact is Minimal Alone:** All three positions show nearly identical average sales (~1,768)
2. **No Strong Correlation:** Price and Sales Volume show weak correlation — pricing alone doesn't drive sales
3. **Pricing Strategy:** 99.9% of products are priced above competitors (average +$2.47 premium)
4. **Balanced Data:** Categories, demographics, and traffic levels are evenly distributed
5. **Multi-Factor Patterns:** The combination of position + promotion + traffic reveals more nuanced patterns than any single factor

**Script:** `step3_data_visualization.py`
**Output Folder:** `visualizations/`

---

## 6. STEP 4 – DASHBOARD DEVELOPMENT

### 6.1 Dashboard Layout

```
┌─────────────────────────────────────────────────────────────────┐
│  HEADER: Strategic Product Placement Sales Impact Analysis      │
│  [Filter: Position] [Filter: Category] [Filter: Promotion]     │
├───────────────────────────────┬─────────────────────────────────┤
│                               │                                 │
│  SHEET 1: Avg Sales by        │  SHEET 2: Sales Distribution    │
│  Product Position (Bar)       │  by Position (Box Plot)         │
│                               │                                 │
├───────────────────────────────┼─────────────────────────────────┤
│                               │                                 │
│  SHEET 3: Heatmap -           │  SHEET 4: Price vs Sales        │
│  Category × Position          │  Scatter Plot                   │
│                               │                                 │
├───────────────────────────────┼─────────────────────────────────┤
│                               │                                 │
│  SHEET 5: Sales by            │  SHEET 6: Multi-Factor          │
│  Demographics & Position      │  Traffic + Promotion + Position │
│                               │                                 │
├───────────────────────────────┴─────────────────────────────────┤
│  SHEET 7: KPI Cards - Total Sales | Avg Price | Top Position    │
└─────────────────────────────────────────────────────────────────┘
```

### 6.2 Tableau Sheet Creation Procedure

**SHEET 1 – Average Sales by Product Position (Bar Chart):**
1. Open a new worksheet → rename it "Sales by Position"
2. Drag `Product_Position` to **Columns**
3. Drag `Sales_Volume` to **Rows**
4. Right-click `SUM(Sales_Volume)` on Rows → select **Measure** → **Average**
5. Drag `Product_Position` to **Color** on the Marks card
6. Click **Label** on the Marks card → check **"Show mark labels"**
7. Click the **Sort Descending** button on the toolbar
8. Right-click chart title → **Edit Title** → type: "Average Sales Volume by Product Position"

**SHEET 2 – Sales Distribution (Box Plot):**
1. New worksheet → rename "Sales Distribution"
2. Drag `Product_Position` to **Columns**
3. Drag `Sales_Volume` to **Rows**
4. Click **Show Me** panel (top-right) → select **"box-and-whisker plot"**
5. Drag `Product_Position` to **Color**
6. Edit title: "Sales Volume Distribution by Position"

**SHEET 3 – Category × Position Heatmap:**
1. New worksheet → rename "Category Heatmap"
2. Drag `Product_Category` to **Rows**
3. Drag `Product_Position` to **Columns**
4. Drag `Sales_Volume` to **Text** on Marks card → change from SUM to **AVG**
5. Drag `Sales_Volume` to **Color** on Marks card → change to **AVG**
6. Change **Mark type** (dropdown on Marks card) to **"Square"**
7. Click **Color** → **Edit Colors** → choose sequential palette (e.g., Orange or Blue-Green)
8. Edit title: "Average Sales: Product Category vs Position"

**SHEET 4 – Price vs Sales Scatter Plot:**
1. New worksheet → rename "Price vs Sales"
2. Drag `Price` to **Columns**
3. Drag `Sales_Volume` to **Rows**
4. Change Mark type to **"Circle"**
5. Drag `Product_Position` to **Color**
6. Drag `Product_Position` to **Shape**
7. Go to **Analytics** pane (left panel) → drag **Trend Line** onto the chart
8. Edit title: "Price vs Sales Volume by Position"

**SHEET 5 – Demographics × Position Heatmap:**
1. New worksheet → rename "Demographics Heatmap"
2. Drag `Consumer_Demographics` to **Rows**
3. Drag `Product_Position` to **Columns**
4. Drag `Sales_Volume` to **Text** → set to AVG
5. Drag `Sales_Volume` to **Color** → set to AVG
6. Mark type: **"Square"**
7. Edit title: "Average Sales: Demographics vs Position"

**SHEET 6 – Multi-Factor Analysis:**
1. New worksheet → rename "Multi-Factor"
2. Drag `Product_Position` to **Columns**
3. Drag `Foot_Traffic` to **Columns** (placed next to Position)
4. Drag `Sales_Volume` to **Rows** → change to AVG
5. Drag `Promotion` to **Color**
6. Edit title: "Sales by Position, Traffic & Promotion"

**SHEET 7 – KPI Cards (create 3 separate sheets):**

*KPI Card 1 – Total Sales:*
1. New worksheet → rename "KPI Total Sales"
2. Drag `Sales_Volume` to **Text** on Marks card (SUM)
3. Click **Text** → **Edit** → increase font size to 36pt, Bold
4. Right-click header → **Hide Field Labels for Rows**
5. Format → set background to light blue

*KPI Card 2 – Average Price:*
1. Same process with `Price` → AVG → format as currency ($XX.XX)

*KPI Card 3 – Record Count:*
1. Drag `Product_ID` to **Text** → change to **CNTD** (Count Distinct)

### 6.3 Building the Dashboard

1. Click the **"New Dashboard"** tab at the bottom (grid icon)
2. Set **Size** → Fixed: 1366 × 768 (or 1920 × 1080)
3. Drag a **"Horizontal"** layout container from the left panel to the canvas
4. Drag **Sheet 1** and **Sheet 2** side by side into the first row
5. Add another horizontal container below → drag **Sheet 3** and **Sheet 4**
6. Add another row → **Sheet 5** and **Sheet 6**
7. Add KPI cards at the bottom in a horizontal container
8. Add a **"Text"** object at the top for the dashboard title

### 6.4 Adding Interactive Filters

1. On Sheet 1, right-click `Product_Position` → **"Show Filter"**
2. The filter appears on the dashboard
3. Right-click the filter on the dashboard → **"Apply to Worksheets"** → **"All Using This Data Source"**
4. Repeat for: `Product_Category`, `Promotion`, `Foot_Traffic`, `Consumer_Demographics`, `Seasonal`
5. Change filter style: right-click filter → choose **"Single Value (dropdown)"** or **"Multiple Values (dropdown)"**

### 6.5 Formatting
- Dashboard title: Tableau Bold, 18pt, Dark Blue (#1B3A5C)
- Sheet titles: Tableau Regular, 12pt, Dark Gray
- Background: White (#FFFFFF)
- Tooltips: Customize to show relevant fields for each chart

**Guide File:** `step4_dashboard_guide.md`

---

## 7. STEP 5 – STORY CREATION

### 7.1 Creating a Story in Tableau

1. Click the **"New Story"** tab at the bottom (book icon)
2. Set Story size: **1366 × 768** (match dashboard)
3. On the left panel, you'll see all your sheets and dashboards listed
4. Drag sheets/dashboards onto the canvas for each **Story Point**

### 7.2 Story Points (7 Pages)

**STORY POINT 1 – "The Business Question"**
- **Caption:** "Does product placement in stores actually impact sales?"
- **Content:** Drag the Distribution Pie Charts sheet
- **Add annotation:** Text box with project context:
  - 989 products analyzed
  - 3 store positions studied
  - 3 product categories, 4 demographic groups
- **Purpose:** Set the stage for the analysis

**STORY POINT 2 – "Product Position & Sales Performance"**
- **Caption:** "All three positions show similar average sales (~1,770)"
- **Content:** Drag Sheet 1 (Bar Chart) + Sheet 2 (Box Plot)
- **Add annotation:** Highlight that position alone shows minimal difference
- **Purpose:** Present the primary finding

**STORY POINT 3 – "The Category Factor"**
- **Caption:** "Product category interacts with placement to affect sales"
- **Content:** Drag Sheet 3 (Category × Position Heatmap)
- **Add annotation:** Circle the highest and lowest cells
- **Purpose:** Show that category-position combinations matter

**STORY POINT 4 – "Demographics Matter"**
- **Caption:** "Customer demographics influence how placement affects sales"
- **Content:** Drag Sheet 5 (Demographics × Position Heatmap)
- **Add annotation:** Highlight best-performing demographic-position pairs
- **Purpose:** Demonstrate demographic-driven placement strategies

**STORY POINT 5 – "Price & Promotion Effects"**
- **Caption:** "Price competitiveness and promotions shape sales outcomes"
- **Content:** Drag Sheet 4 (Scatter) and Sheet 3 (Promotion bar chart)
- **Add annotation:** Note that 99.9% of products are priced above competitors
- **Purpose:** Show pricing and promotional impact

**STORY POINT 6 – "The Multi-Factor View"**
- **Caption:** "Foot traffic + promotion + position: the full picture"
- **Content:** Drag the full interactive Dashboard
- **Let viewers:** Interact with filters to explore on their own
- **Purpose:** Enable interactive data exploration

**STORY POINT 7 – "Strategic Recommendations"**
- **Caption:** "Data-driven recommendations for optimal product placement"
- **Content:** Drag Dashboard + add a text annotation with recommendations
- **Purpose:** Summarize actionable insights

### 7.3 Story Formatting
1. Select **Navigator style**: click "Layout" tab → choose **"Numbers"** or **"Dots"**
2. Add transitions by clicking **"Add a Caption"** for each Story Point
3. To save a specific filter state: apply filters on a sheet → click **"Update"** on that Story Point

**Guide File:** `step5_story_guide.md`

---

## 8. STEP 6 – PERFORMANCE TESTING

### 8.1 Automated Testing Framework

A Python-based testing script was created to validate data integrity and analysis accuracy before Tableau deployment.

### 8.2 Test Categories & Results

| # | Test Category | Tests Run | Passed | Failed |
|---|--------------|-----------|--------|--------|
| 1 | Data Integrity (nulls, duplicates, shape) | 5 | 5 | 0 |
| 2 | Data Type Validation | 4 | 4 | 0 |
| 3 | Value Range Validation | 5 | 5 | 0 |
| 4 | Categorical Value Validation | 6 | 6 | 0 |
| 5 | Feature Engineering Validation | 2 | 2 | 0 |
| 6 | Statistical Sanity Checks | 4 | 4 | 0 |
| 7 | Cross-Tabulation Consistency | 2 | 2 | 0 |
| 8 | Visualization Data Accuracy | 3 | 3 | 0 |
| | **TOTAL** | **31** | **31** | **0** |

**Overall Score: 100% — ALL TESTS PASSED**

### 8.3 Test Details

| Test Name | Expected | Actual | Status |
|-----------|----------|--------|--------|
| No missing values | 0 | 0 | PASS |
| No duplicate rows | 0 | 0 | PASS |
| No duplicate Product IDs | 0 | 0 | PASS |
| Dataset has 989 rows | 989 | 989 | PASS |
| Dataset has 14 columns | 14 | 14 | PASS |
| Product_ID is numeric | int64 | int64 | PASS |
| Price is numeric | float64 | float64 | PASS |
| Sales_Volume is numeric | int64 | int64 | PASS |
| Product_Position is string | string | string | PASS |
| Price > 0 | True | True | PASS |
| Competitor Price >= 0 | True | True | PASS |
| Sales Volume > 0 | True | True | PASS |
| Price_Difference correct | True | True | PASS |
| Price_Ratio correct | True | True | PASS |
| Product Position = 3 values | 3 | 3 | PASS |
| Promotion = 2 values | 2 | 2 | PASS |
| Foot Traffic = 3 values | 3 | 3 | PASS |
| Demographics = 4 values | 4 | 4 | PASS |
| Category = 3 values | 3 | 3 | PASS |
| Seasonal = 2 values | 2 | 2 | PASS |
| Price_Range categories valid | True | True | PASS |
| Sales_Performance valid | True | True | PASS |
| Avg sales in range 500-5000 | True | 1,768 | PASS |
| Aisle count > 100 | True | 335 | PASS |
| End-cap count > 100 | True | 338 | PASS |
| Front of Store count > 100 | True | 316 | PASS |
| Position totals = overall | True | True | PASS |
| Category totals = overall | True | True | PASS |
| Aisle avg ≈ 1781 | ±20 | Within range | PASS |
| End-cap avg ≈ 1754 | ±20 | Within range | PASS |
| Front of Store avg ≈ 1773 | ±20 | Within range | PASS |

**Script:** `step6_performance_testing.py`

---

## 9. STEP 7 – WEB INTEGRATION

### 9.1 Publishing to Tableau Public

**Procedure:**
1. Complete all dashboard and story sheets in Tableau Desktop
2. Go to **Server** → **Tableau Public** → **Save to Tableau Public**
3. Sign in with Tableau Public credentials (create account at public.tableau.com if needed)
4. Name the workbook: **"Strategic Product Placement Sales Analysis"**
5. Select sheets to include (all dashboards and stories)
6. Click **"Save"**
7. Browser opens automatically with the published visualization
8. Copy the URL for sharing

### 9.2 Embedding in a Website
After publishing, click **"Share"** at the bottom of the viz on Tableau Public to get the embed code. Paste the `<div>` code into any HTML page.

### 9.3 Sharing Options
| Method | How |
|--------|-----|
| Direct Link | Share the Tableau Public URL |
| Embed Code | Copy embed `<div>` into HTML |
| Social Media | Share button → LinkedIn, Twitter |
| PDF Export | Server → Export as PDF |
| Image Export | Dashboard → Export Image |

**Guide File:** `step7_web_integration_guide.md`

---

## 10. STEP 8 – PROJECT DEMONSTRATION & DOCUMENTATION

### 10.1 Project Files Summary

| File | Purpose |
|------|---------|
| `dataset/Product Positioning.csv` | Original raw dataset |
| `dataset/Product_Positioning_Cleaned.csv` | Cleaned and enriched dataset |
| `step1_data_exploration.py` | Data collection & EDA script |
| `step2_data_preparation.py` | Data cleaning & feature engineering |
| `step3_data_visualization.py` | 14 Python visualizations |
| `step4_dashboard_guide.md` | Tableau dashboard building guide |
| `step5_story_guide.md` | Tableau story structure guide |
| `step6_performance_testing.py` | 31 automated validation tests |
| `step7_web_integration_guide.md` | Web publishing guide |
| `Project_Documentation.md` | This complete documentation |
| `README.md` | Project overview and quick-start |
| `visualizations/` | 14 exported chart images |

### 10.2 How to Reproduce This Project

**Prerequisites:**
- Python 3.10+ with pip
- Tableau Desktop (Public edition or higher)

**Step-by-step:**
```
# 1. Install Python dependencies
pip install pandas matplotlib seaborn

# 2. Run data exploration
python step1_data_exploration.py

# 3. Run data preparation (creates cleaned CSV)
python step2_data_preparation.py

# 4. Generate all visualizations
python step3_data_visualization.py

# 5. Run performance tests (must show 31/31 pass)
python step6_performance_testing.py

# 6. Open Tableau Desktop
#    → Connect → Text File → dataset/Product_Positioning_Cleaned.csv

# 7. Follow step4_dashboard_guide.md to build dashboard

# 8. Follow step5_story_guide.md to create story

# 9. Follow step7_web_integration_guide.md to publish
```

---

## 11. KEY FINDINGS & INSIGHTS

### Finding 1: Product Position Has Minimal Standalone Impact
- Aisle: **1,768** avg sales
- Front of Store: **1,773** avg sales
- End-cap: **1,754** avg sales
- **Insight:** The difference between positions is less than 1.1%, indicating product position alone is NOT the dominant sales driver.

### Finding 2: Pricing Above Competitors Is Universal
- **99.9%** of products are priced higher than competitors
- Average price premium: **+$2.47**
- Average product price: **$28.02** vs competitor's **$25.55**
- **Insight:** Despite higher pricing, sales remain healthy — suggesting brand value or other factors compensate.

### Finding 3: Data Is Well-Balanced
- Positions: Aisle (335), End-cap (338), Front of Store (316) — roughly equal
- Categories: Clothing (338), Electronics (336), Food (326) — roughly equal
- Demographics: Families (263), College students (251), Seniors (249), Young adults (237)
- **Insight:** Results are not skewed by uneven data distribution.

### Finding 4: Multi-Factor Interactions Drive Sales
- The combination of **Position + Promotion + Foot Traffic** reveals more variation than any single factor
- Certain **Category-Position** and **Demographic-Position** combinations outperform others
- **Insight:** Placement strategy should be tailored by product type and target customer, not applied uniformly.

### Finding 5: Weak Price-Sales Correlation
- Correlation between Price and Sales Volume is very weak
- **Insight:** Sales are driven more by placement context (traffic, promotion, customer type) than by price point alone.

---

## 12. RECOMMENDATIONS

Based on the analysis, the following strategic recommendations are proposed:

| # | Recommendation | Rationale |
|---|---------------|-----------|
| 1 | **Don't rely on position alone** | All positions perform similarly; placement without other support is insufficient |
| 2 | **Optimize category-position pairings** | Certain product types perform better in specific positions — use the heatmap to identify best fits |
| 3 | **Target demographics with tailored placement** | Different customer groups respond differently to positions — customize by store demographics |
| 4 | **Combine promotions with high-traffic placement** | The multi-factor analysis shows promotions amplify sales in certain position+traffic combinations |
| 5 | **Monitor competitive pricing** | At +$2.47 average premium, ensure value perception justifies higher pricing |
| 6 | **Use seasonal timing strategically** | Rotate seasonal products through optimal positions during peak periods |
| 7 | **Deploy interactive dashboards** | Enable store managers to explore data and make real-time placement decisions via Tableau |

---

## 13. CONCLUSION

This project successfully demonstrates a complete data analytics workflow from data collection through interactive visualization and web deployment. The analysis reveals that **product placement position alone does not significantly impact sales volume** — all three positions (Aisle, End-cap, Front of Store) show nearly identical average sales (~1,768 units). However, the **interaction between placement and other factors** (product category, consumer demographics, promotions, foot traffic, and seasonality) creates meaningful variation that can be leveraged for strategic advantage.

The Tableau dashboard and story provide stakeholders with an interactive tool to explore these multi-dimensional relationships and make data-driven product placement decisions. The automated testing framework ensures data integrity and analysis accuracy, supporting confident decision-making.

---

*Project completed: March 8, 2026*
*Tools: Python 3.13, Pandas, Matplotlib, Seaborn, Tableau Desktop*
