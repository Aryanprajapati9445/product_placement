# STEP 4: TABLEAU DASHBOARD DESIGN GUIDE
# Strategic Product Placement Analysis: Unveiling Sales Impact

## ===================================================================
## DASHBOARD LAYOUT BLUEPRINT
## ===================================================================

## Dashboard Name: "Strategic Product Placement Sales Impact Dashboard"
## Recommended Size: 1366 x 768 (Laptop) or 1920 x 1080 (Desktop)

## ===================================================================
## CONNECTING DATA TO TABLEAU
## ===================================================================

### Method:
1. Open Tableau Desktop
2. Click "Connect" → "Text File" 
3. Navigate to: dataset/Product_Positioning_Cleaned.csv
4. Click "Open"
5. Tableau will auto-detect data types
6. Go to "Sheet 1" to start building

## ===================================================================
## DASHBOARD LAYOUT (3-SECTION DESIGN)
## ===================================================================

### ┌─────────────────────────────────────────────────────────────────┐
### │  HEADER: Strategic Product Placement Sales Impact Analysis     │
### │  [Filter: Position] [Filter: Category] [Filter: Promotion]    │
### ├───────────────────────────────┬─────────────────────────────────┤
### │                               │                                 │
### │  SHEET 1: Avg Sales by        │  SHEET 2: Sales Distribution    │
### │  Product Position (Bar)       │  by Position (Box Plot)         │
### │                               │                                 │
### ├───────────────────────────────┼─────────────────────────────────┤
### │                               │                                 │
### │  SHEET 3: Heatmap -           │  SHEET 4: Price vs Sales        │
### │  Category × Position          │  Scatter Plot                   │
### │                               │                                 │
### ├───────────────────────────────┼─────────────────────────────────┤
### │                               │                                 │
### │  SHEET 5: Sales by            │  SHEET 6: Multi-Factor          │
### │  Demographics & Position      │  Traffic + Promotion + Position │
### │                               │                                 │
### ├───────────────────────────────┴─────────────────────────────────┤
### │  SHEET 7: KPI Cards - Total Sales | Avg Price | Top Position   │
### └─────────────────────────────────────────────────────────────────┘

## ===================================================================
## SHEET-BY-SHEET TABLEAU INSTRUCTIONS
## ===================================================================

### SHEET 1: Average Sales by Product Position (Bar Chart)
### ─────────────────────────────────────────────────────
- Drag "Product Position" → Columns
- Drag "Sales Volume" → Rows
- Right-click "Sales Volume" → Measure → Average
- Drag "Product Position" → Color (Marks card)
- Click "Label" on Marks card → Show mark labels
- Sort descending by Sales Volume

### SHEET 2: Sales Distribution by Position (Box Plot)
### ─────────────────────────────────────────────────────
- Drag "Product Position" → Columns
- Drag "Sales Volume" → Rows
- Click "Show Me" → Select "Box-and-whisker plot"
- Drag "Product Position" → Color

### SHEET 3: Heatmap - Category × Position
### ─────────────────────────────────────────────────────
- Drag "Product Category" → Rows
- Drag "Product Position" → Columns
- Drag "Sales Volume" → Text (Marks card) → set to AVG
- Drag "Sales Volume" → Color (Marks card) → set to AVG
- Change Mark type to "Square"
- Edit colors: Sequential palette (Orange or Blue-Green)

### SHEET 4: Price vs Sales Scatter Plot
### ─────────────────────────────────────────────────────
- Drag "Price" → Columns
- Drag "Sales Volume" → Rows
- Drag "Product Position" → Color
- Drag "Product Position" → Shape
- Change Mark type to "Circle"
- Add Trend Line: Analytics pane → Trend Line → drag to chart

### SHEET 5: Sales by Demographics & Position
### ─────────────────────────────────────────────────────
- Drag "Consumer Demographics" → Rows
- Drag "Product Position" → Columns
- Drag "Sales Volume" → Text & Color → AVG
- Mark type: "Square" (Heatmap)

### SHEET 6: Multi-Factor Analysis
### ─────────────────────────────────────────────────────
- Drag "Product Position" → Columns
- Drag "Foot Traffic" → Columns (next to Position)
- Drag "Sales Volume" → Rows (AVG)
- Drag "Promotion" → Color

### SHEET 7: KPI Summary Cards
### ─────────────────────────────────────────────────────
- Create 3 separate sheets:
  - KPI 1: SUM(Sales Volume) → Text, large font
  - KPI 2: AVG(Price) → Text, formatted as currency
  - KPI 3: Top Position by AVG Sales → Calculated field

## ===================================================================
## INTERACTIVE FILTERS (Add to Dashboard)
## ===================================================================
1. Product Position (Dropdown filter)
2. Product Category (Dropdown filter)  
3. Promotion (Yes/No toggle)
4. Foot Traffic (Multi-select)
5. Consumer Demographics (Multi-select)
6. Seasonal (Yes/No toggle)

### How to add filters:
- On any sheet, right-click a dimension → "Show Filter"
- On dashboard, right-click filter → "Apply to Worksheets" → "All Using This Data Source"

## ===================================================================
## FORMATTING GUIDELINES
## ===================================================================
- Title Font: Tableau Bold, 18pt, Dark Blue (#1B3A5C)
- Subtitle Font: Tableau Regular, 12pt, Gray
- Background: White (#FFFFFF) or Light Gray (#F5F5F5)
- Gridlines: Light gray, thin
- Color Palette: Tableau 10 or custom blue-orange diverging
- Tooltips: Customize to show Position, Category, Sales Volume, Price
