# STEP 7: WEB INTEGRATION GUIDE
# Strategic Product Placement Analysis: Unveiling Sales Impact

## ===================================================================
## PUBLISHING TO TABLEAU PUBLIC (Free)
## ===================================================================

### Prerequisites:
### - Tableau Desktop (Public edition or higher)
### - Tableau Public account: https://public.tableau.com/

### Steps:
### 1. Finalize your dashboard and story in Tableau Desktop
### 2. Go to: Server → Tableau Public → Save to Tableau Public
### 3. Sign in with your Tableau Public credentials
### 4. Name your workbook: "Strategic Product Placement Sales Analysis"
### 5. Click "Save"
### 6. Your browser will open with the published visualization
### 7. Copy the URL for sharing

## ===================================================================
## EMBEDDING IN A WEBSITE
## ===================================================================

### After publishing to Tableau Public, get the embed code:
### 1. Open your published viz on Tableau Public
### 2. Click the "Share" button (bottom of viz)
### 3. Copy the "Embed Code"
### 4. Paste into your HTML page

### Actual Embed Code (from Tableau Public):
### Workbook: product_placement / Dashboard1
### Viz ID: viz1773026387135
### URL: https://public.tableau.com/views/product_placement/Dashboard1
###
### Web Integration File: ../index.html
### - Fully responsive HTML page with embedded Tableau dashboard
### - Includes all 7 story scenes with interactive navigation
### - Key findings summary cards
### - Open index.html in a browser to view the complete integration

## ===================================================================
## SHARING OPTIONS
## ===================================================================

### 1. Direct Link: Share the Tableau Public URL
### 2. Embed: Use embed code in any HTML/website
### 3. Social: Share directly from Tableau Public to LinkedIn, Twitter
### 4. Download: Allow viewers to download data/image from viz
### 5. PDF Export: Server → Export as PDF (for offline sharing)

## ===================================================================
## BEST PRACTICES FOR WEB PUBLISHING
## ===================================================================

### Performance:
### - Keep dataset under 15M rows for Tableau Public
### - Use extracts instead of live connections
### - Minimize the number of sheets per dashboard
### - Use integer/float instead of string where possible

### Responsiveness:
### - Set dashboard to "Automatic" or "Range" sizing
### - Test on different screen sizes
### - Use device-specific layouts (Desktop, Tablet, Phone)

### Security (Tableau Public):
### - Data is PUBLIC - do not upload sensitive/private data
### - Anyone can download the underlying data
### - For private data, use Tableau Server or Tableau Cloud instead
