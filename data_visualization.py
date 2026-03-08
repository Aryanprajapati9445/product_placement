"""
Step 3: Data Visualization
Strategic Product Placement Analysis: Unveiling Sales Impact
Generates all key charts and saves them as images
"""
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Setup
sns.set_theme(style="whitegrid", palette="Set2")
os.makedirs("visualizations", exist_ok=True)

df = pd.read_csv("dataset/Product_Positioning_Cleaned.csv")

print("=" * 60)
print("STEP 3: DATA VISUALIZATION")
print("=" * 60)

# ============================================================
# Chart 1: Sales Volume by Product Position (Bar Chart)
# ============================================================
fig, ax = plt.subplots(figsize=(8, 5))
order = df.groupby('Product_Position')['Sales_Volume'].mean().sort_values(ascending=False).index
sns.barplot(data=df, x='Product_Position', y='Sales_Volume', order=order, 
            estimator='mean', errorbar='sd', ax=ax, palette='viridis')
ax.set_title('Average Sales Volume by Product Position', fontsize=14, fontweight='bold')
ax.set_xlabel('Product Position', fontsize=12)
ax.set_ylabel('Average Sales Volume', fontsize=12)
for p in ax.patches:
    ax.annotate(f'{p.get_height():.0f}', (p.get_x() + p.get_width()/2., p.get_height()),
                ha='center', va='bottom', fontsize=11, fontweight='bold')
plt.tight_layout()
plt.savefig('visualizations/01_sales_by_position.png', dpi=150)
plt.close()
print("  Saved: 01_sales_by_position.png")

# ============================================================
# Chart 2: Sales Distribution by Position (Box Plot)
# ============================================================
fig, ax = plt.subplots(figsize=(8, 5))
sns.boxplot(data=df, x='Product_Position', y='Sales_Volume', ax=ax, palette='Set2')
ax.set_title('Sales Volume Distribution by Product Position', fontsize=14, fontweight='bold')
ax.set_xlabel('Product Position')
ax.set_ylabel('Sales Volume')
plt.tight_layout()
plt.savefig('visualizations/02_sales_distribution_boxplot.png', dpi=150)
plt.close()
print("  Saved: 02_sales_distribution_boxplot.png")

# ============================================================
# Chart 3: Sales by Position and Promotion (Grouped Bar)
# ============================================================
fig, ax = plt.subplots(figsize=(10, 6))
sns.barplot(data=df, x='Product_Position', y='Sales_Volume', hue='Promotion',
            estimator='mean', errorbar='sd', ax=ax, palette='coolwarm')
ax.set_title('Sales Volume by Position & Promotion Status', fontsize=14, fontweight='bold')
ax.set_xlabel('Product Position')
ax.set_ylabel('Average Sales Volume')
ax.legend(title='Promotion')
plt.tight_layout()
plt.savefig('visualizations/03_sales_position_promotion.png', dpi=150)
plt.close()
print("  Saved: 03_sales_position_promotion.png")

# ============================================================
# Chart 4: Sales by Position and Foot Traffic (Grouped Bar)
# ============================================================
fig, ax = plt.subplots(figsize=(10, 6))
sns.barplot(data=df, x='Product_Position', y='Sales_Volume', hue='Foot_Traffic',
            hue_order=['Low', 'Medium', 'High'],
            estimator='mean', errorbar='sd', ax=ax, palette='YlOrRd')
ax.set_title('Sales Volume by Position & Foot Traffic', fontsize=14, fontweight='bold')
ax.set_xlabel('Product Position')
ax.set_ylabel('Average Sales Volume')
ax.legend(title='Foot Traffic')
plt.tight_layout()
plt.savefig('visualizations/04_sales_position_traffic.png', dpi=150)
plt.close()
print("  Saved: 04_sales_position_traffic.png")

# ============================================================
# Chart 5: Heatmap - Average Sales by Position & Category
# ============================================================
fig, ax = plt.subplots(figsize=(8, 5))
pivot = df.pivot_table(values='Sales_Volume', index='Product_Category', 
                        columns='Product_Position', aggfunc='mean')
sns.heatmap(pivot, annot=True, fmt='.0f', cmap='YlGnBu', ax=ax, linewidths=0.5)
ax.set_title('Avg Sales Volume: Product Category vs Position', fontsize=14, fontweight='bold')
plt.tight_layout()
plt.savefig('visualizations/05_heatmap_category_position.png', dpi=150)
plt.close()
print("  Saved: 05_heatmap_category_position.png")

# ============================================================
# Chart 6: Heatmap - Avg Sales by Demographics & Position
# ============================================================
fig, ax = plt.subplots(figsize=(8, 5))
pivot2 = df.pivot_table(values='Sales_Volume', index='Consumer_Demographics',
                         columns='Product_Position', aggfunc='mean')
sns.heatmap(pivot2, annot=True, fmt='.0f', cmap='RdYlGn', ax=ax, linewidths=0.5)
ax.set_title('Avg Sales Volume: Demographics vs Position', fontsize=14, fontweight='bold')
plt.tight_layout()
plt.savefig('visualizations/06_heatmap_demographics_position.png', dpi=150)
plt.close()
print("  Saved: 06_heatmap_demographics_position.png")

# ============================================================
# Chart 7: Price vs Sales Volume Scatter Plot
# ============================================================
fig, ax = plt.subplots(figsize=(10, 6))
sns.scatterplot(data=df, x='Price', y='Sales_Volume', hue='Product_Position',
                style='Product_Position', alpha=0.6, ax=ax, palette='deep')
ax.set_title('Price vs Sales Volume by Product Position', fontsize=14, fontweight='bold')
ax.set_xlabel('Price ($)')
ax.set_ylabel('Sales Volume')
ax.legend(title='Position')
plt.tight_layout()
plt.savefig('visualizations/07_price_vs_sales_scatter.png', dpi=150)
plt.close()
print("  Saved: 07_price_vs_sales_scatter.png")

# ============================================================
# Chart 8: Correlation Heatmap
# ============================================================
fig, ax = plt.subplots(figsize=(8, 6))
numeric_cols = ['Price', 'Competitors_Price', 'Sales_Volume', 'Price_Difference', 'Price_Ratio']
corr = df[numeric_cols].corr()
sns.heatmap(corr, annot=True, cmap='coolwarm', center=0, ax=ax, 
            fmt='.3f', linewidths=0.5, vmin=-1, vmax=1)
ax.set_title('Correlation Matrix', fontsize=14, fontweight='bold')
plt.tight_layout()
plt.savefig('visualizations/08_correlation_heatmap.png', dpi=150)
plt.close()
print("  Saved: 08_correlation_heatmap.png")

# ============================================================
# Chart 9: Sales by Consumer Demographics (Bar)
# ============================================================
fig, ax = plt.subplots(figsize=(8, 5))
order = df.groupby('Consumer_Demographics')['Sales_Volume'].mean().sort_values(ascending=False).index
sns.barplot(data=df, x='Consumer_Demographics', y='Sales_Volume', order=order,
            estimator='mean', errorbar='sd', ax=ax, palette='muted')
ax.set_title('Average Sales Volume by Consumer Demographics', fontsize=14, fontweight='bold')
ax.set_xlabel('Consumer Demographics')
ax.set_ylabel('Average Sales Volume')
for p in ax.patches:
    ax.annotate(f'{p.get_height():.0f}', (p.get_x() + p.get_width()/2., p.get_height()),
                ha='center', va='bottom', fontsize=11, fontweight='bold')
plt.tight_layout()
plt.savefig('visualizations/09_sales_by_demographics.png', dpi=150)
plt.close()
print("  Saved: 09_sales_by_demographics.png")

# ============================================================
# Chart 10: Sales by Product Category (Bar)
# ============================================================
fig, ax = plt.subplots(figsize=(8, 5))
order = df.groupby('Product_Category')['Sales_Volume'].mean().sort_values(ascending=False).index
sns.barplot(data=df, x='Product_Category', y='Sales_Volume', order=order,
            estimator='mean', errorbar='sd', ax=ax, palette='pastel')
ax.set_title('Average Sales Volume by Product Category', fontsize=14, fontweight='bold')
ax.set_xlabel('Product Category')
ax.set_ylabel('Average Sales Volume')
for p in ax.patches:
    ax.annotate(f'{p.get_height():.0f}', (p.get_x() + p.get_width()/2., p.get_height()),
                ha='center', va='bottom', fontsize=11, fontweight='bold')
plt.tight_layout()
plt.savefig('visualizations/10_sales_by_category.png', dpi=150)
plt.close()
print("  Saved: 10_sales_by_category.png")

# ============================================================
# Chart 11: Seasonal vs Non-Seasonal Sales
# ============================================================
fig, ax = plt.subplots(figsize=(8, 5))
sns.barplot(data=df, x='Seasonal', y='Sales_Volume', hue='Product_Position',
            estimator='mean', errorbar='sd', ax=ax, palette='Set1')
ax.set_title('Sales Volume: Seasonal vs Non-Seasonal by Position', fontsize=14, fontweight='bold')
ax.set_xlabel('Seasonal Product')
ax.set_ylabel('Average Sales Volume')
plt.tight_layout()
plt.savefig('visualizations/11_seasonal_sales.png', dpi=150)
plt.close()
print("  Saved: 11_seasonal_sales.png")

# ============================================================
# Chart 12: Price Difference Impact on Sales
# ============================================================
fig, ax = plt.subplots(figsize=(10, 6))
sns.scatterplot(data=df, x='Price_Difference', y='Sales_Volume', hue='Product_Position',
                alpha=0.6, ax=ax, palette='dark')
ax.set_title('Price Difference (vs Competitor) Impact on Sales', fontsize=14, fontweight='bold')
ax.set_xlabel('Price Difference ($) [Positive = Higher than Competitor]')
ax.set_ylabel('Sales Volume')
ax.axvline(x=0, color='red', linestyle='--', alpha=0.5, label='Equal Pricing')
ax.legend(title='Position')
plt.tight_layout()
plt.savefig('visualizations/12_price_diff_vs_sales.png', dpi=150)
plt.close()
print("  Saved: 12_price_diff_vs_sales.png")

# ============================================================
# Chart 13: Multi-factor Analysis - Position + Traffic + Promotion
# ============================================================
fig, axes = plt.subplots(1, 3, figsize=(18, 5), sharey=True)
for idx, position in enumerate(['Aisle', 'End-cap', 'Front of Store']):
    subset = df[df['Product_Position'] == position]
    sns.barplot(data=subset, x='Foot_Traffic', y='Sales_Volume', hue='Promotion',
                order=['Low', 'Medium', 'High'], estimator='mean', 
                ax=axes[idx], palette='coolwarm')
    axes[idx].set_title(f'{position}', fontsize=13, fontweight='bold')
    axes[idx].set_xlabel('Foot Traffic')
    if idx == 0:
        axes[idx].set_ylabel('Avg Sales Volume')
    else:
        axes[idx].set_ylabel('')
    axes[idx].legend(title='Promotion', loc='upper left')
fig.suptitle('Multi-Factor Analysis: Position + Traffic + Promotion', fontsize=15, fontweight='bold', y=1.02)
plt.tight_layout()
plt.savefig('visualizations/13_multi_factor_analysis.png', dpi=150, bbox_inches='tight')
plt.close()
print("  Saved: 13_multi_factor_analysis.png")

# ============================================================
# Chart 14: Pie Chart - Product Position Distribution
# ============================================================
fig, axes = plt.subplots(1, 2, figsize=(14, 5))
# Position distribution
pos_counts = df['Product_Position'].value_counts()
axes[0].pie(pos_counts, labels=pos_counts.index, autopct='%1.1f%%', 
            colors=sns.color_palette('Set2'), startangle=90)
axes[0].set_title('Product Position Distribution', fontsize=13, fontweight='bold')

# Category distribution
cat_counts = df['Product_Category'].value_counts()
axes[1].pie(cat_counts, labels=cat_counts.index, autopct='%1.1f%%',
            colors=sns.color_palette('pastel'), startangle=90)
axes[1].set_title('Product Category Distribution', fontsize=13, fontweight='bold')
plt.tight_layout()
plt.savefig('visualizations/14_distribution_pies.png', dpi=150)
plt.close()
print("  Saved: 14_distribution_pies.png")

print(f"\n  Total visualizations created: 14")
print(f"  All saved in: visualizations/")

print("\n" + "=" * 60)
print("Data Visualization COMPLETE")
print("=" * 60)
