import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from pathlib import Path

# ---------------------------------------------------------
# 1. Project Setup
# ---------------------------------------------------------

INPUT_FILE = "train.csv"
OUTPUT_DIR = Path("outputs")
OUTPUT_DIR.mkdir(exist_ok=True)

# ---------------------------------------------------------
# 2. Load Dataset
# ---------------------------------------------------------

df = pd.read_csv(INPUT_FILE)

print("=" * 60)
print("DATA VISUALIZATION PROJECT")
print("=" * 60)

print(f"\nDataset Shape: {df.shape}")

print("\nColumn Names:")
print(df.columns.tolist())

# ---------------------------------------------------------
# 3. Data Cleaning and Preparation
# ---------------------------------------------------------

df["Order Date"] = pd.to_datetime(df["Order Date"], dayfirst=True)
df["Ship Date"] = pd.to_datetime(df["Ship Date"], dayfirst=True)

# Check missing values
print("\nMissing Values:")
print(df.isnull().sum())

# Remove duplicate rows
duplicates = df.duplicated().sum()
print(f"\nDuplicate Rows: {duplicates}")

df = df.drop_duplicates()

# Create useful date columns
df["Year"] = df["Order Date"].dt.year
df["Month"] = df["Order Date"].dt.to_period("M").astype(str)

# ---------------------------------------------------------
# 4. Basic Summary
# ---------------------------------------------------------

print("\nSales Summary:")
print(df["Sales"].describe())

print("\nTotal Sales:", round(df["Sales"].sum(), 2))

print("\nAverage Order Sales:", round(df["Sales"].mean(), 2))

# ---------------------------------------------------------
# 5. Sales by Category
# ---------------------------------------------------------

category_sales = (
    df.groupby("Category")["Sales"]
    .sum()
    .sort_values(ascending=False)
)

plt.figure(figsize=(10, 6))
category_sales.plot(kind="bar")

plt.title("Total Sales by Category")
plt.xlabel("Category")
plt.ylabel("Sales")
plt.xticks(rotation=0)
plt.tight_layout()

plt.savefig(OUTPUT_DIR / "sales_by_category.png", dpi=300)
plt.close()

# ---------------------------------------------------------
# 6. Sales by Region
# ---------------------------------------------------------

region_sales = (
    df.groupby("Region")["Sales"]
    .sum()
    .sort_values(ascending=False)
)

plt.figure(figsize=(10, 6))
region_sales.plot(kind="bar")

plt.title("Total Sales by Region")
plt.xlabel("Region")
plt.ylabel("Sales")
plt.xticks(rotation=0)
plt.tight_layout()

plt.savefig(OUTPUT_DIR / "sales_by_region.png", dpi=300)
plt.close()

# ---------------------------------------------------------
# 7. Monthly Sales Trend
# ---------------------------------------------------------

monthly_sales = (
    df.groupby("Month")["Sales"]
    .sum()
)

plt.figure(figsize=(14, 6))
monthly_sales.plot(kind="line", marker="o")

plt.title("Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.xticks(rotation=45)
plt.grid(True, alpha=0.3)
plt.tight_layout()

plt.savefig(OUTPUT_DIR / "monthly_sales_trend.png", dpi=300)
plt.close()

# ---------------------------------------------------------
# 8. Top 10 Products by Sales
# ---------------------------------------------------------

top_products = (
    df.groupby("Product Name")["Sales"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
    .sort_values()
)

plt.figure(figsize=(12, 7))
top_products.plot(kind="barh")

plt.title("Top 10 Products by Sales")
plt.xlabel("Sales")
plt.ylabel("Product")

plt.tight_layout()

plt.savefig(OUTPUT_DIR / "top_10_products.png", dpi=300)
plt.close()

# ---------------------------------------------------------
# 9. Sales by Sub-Category
# ---------------------------------------------------------

subcategory_sales = (
    df.groupby("Sub-Category")["Sales"]
    .sum()
    .sort_values(ascending=False)
)

plt.figure(figsize=(11, 6))
subcategory_sales.plot(kind="bar")

plt.title("Sales by Sub-Category")
plt.xlabel("Sub-Category")
plt.ylabel("Sales")
plt.xticks(rotation=45)

plt.tight_layout()

plt.savefig(OUTPUT_DIR / "sales_by_subcategory.png", dpi=300)
plt.close()

# ---------------------------------------------------------
# 10. Sales by Customer Segment
# ---------------------------------------------------------

segment_sales = (
    df.groupby("Segment")["Sales"]
    .sum()
    .sort_values(ascending=False)
)

plt.figure(figsize=(9, 6))
segment_sales.plot(kind="bar")

plt.title("Sales by Customer Segment")
plt.xlabel("Customer Segment")
plt.ylabel("Sales")
plt.xticks(rotation=0)

plt.tight_layout()

plt.savefig(OUTPUT_DIR / "sales_by_segment.png", dpi=300)
plt.close()

# ---------------------------------------------------------
# 11. Sales Distribution
# ---------------------------------------------------------

plt.figure(figsize=(10, 6))

sns.histplot(
    df["Sales"],
    bins=40,
    kde=True
)

plt.title("Sales Distribution")
plt.xlabel("Sales")
plt.ylabel("Frequency")

plt.tight_layout()

plt.savefig(OUTPUT_DIR / "sales_distribution.png", dpi=300)
plt.close()

# ---------------------------------------------------------
# 12. Category and Region Heatmap
# ---------------------------------------------------------

category_region = pd.pivot_table(
    df,
    values="Sales",
    index="Category",
    columns="Region",
    aggfunc="sum"
)

plt.figure(figsize=(10, 6))

sns.heatmap(
    category_region,
    annot=True,
    fmt=".0f"
)

plt.title("Sales by Category and Region")
plt.xlabel("Region")
plt.ylabel("Category")

plt.tight_layout()

plt.savefig(OUTPUT_DIR / "category_region_heatmap.png", dpi=300)
plt.close()

# ---------------------------------------------------------
# 13. Ship Mode Analysis
# ---------------------------------------------------------

ship_mode_sales = (
    df.groupby("Ship Mode")["Sales"]
    .sum()
    .sort_values(ascending=False)
)

plt.figure(figsize=(10, 6))
ship_mode_sales.plot(kind="bar")

plt.title("Sales by Ship Mode")
plt.xlabel("Ship Mode")
plt.ylabel("Sales")
plt.xticks(rotation=0)

plt.tight_layout()

plt.savefig(OUTPUT_DIR / "sales_by_ship_mode.png", dpi=300)
plt.close()

# ---------------------------------------------------------
# 14. Save Cleaned Dataset
# ---------------------------------------------------------

df.to_csv(
    OUTPUT_DIR / "cleaned_sales_data.csv",
    index=False
)

# ---------------------------------------------------------
# 15. Generate Summary
# ---------------------------------------------------------

highest_category = category_sales.idxmax()
highest_category_sales = category_sales.max()

highest_region = region_sales.idxmax()
highest_region_sales = region_sales.max()

highest_segment = segment_sales.idxmax()
highest_segment_sales = segment_sales.max()

highest_month = monthly_sales.idxmax()
highest_month_sales = monthly_sales.max()

summary = f"""
# Data Visualization Summary

## Dataset
- Rows after cleaning: {len(df):,}
- Columns: {len(df.columns)}
- Total Sales: ${df["Sales"].sum():,.2f}
- Average Sale: ${df["Sales"].mean():,.2f}

## Key Insights

### Category
The highest-selling category was **{highest_category}**
with total sales of **${highest_category_sales:,.2f}**.

### Region
The highest-performing region was **{highest_region}**
with total sales of **${highest_region_sales:,.2f}**.

### Customer Segment
The customer segment generating the highest sales was
**{highest_segment}**, with sales of **${highest_segment_sales:,.2f}**.

### Monthly Trend
The month with the highest sales was **{highest_month}**
with sales of **${highest_month_sales:,.2f}**.

## Visualizations Created

1. Sales by Category
2. Sales by Region
3. Monthly Sales Trend
4. Top 10 Products
5. Sales by Sub-Category
6. Sales by Customer Segment
7. Sales Distribution
8. Category and Region Heatmap
9. Sales by Ship Mode
"""

with open(OUTPUT_DIR / "visualization_summary.md", "w", encoding="utf-8") as file:
    file.write(summary)

print("\n" + "=" * 60)
print("VISUALIZATION PROJECT COMPLETED SUCCESSFULLY")
print("=" * 60)

print("\nOutput files saved in:", OUTPUT_DIR)

print("\nKey Insights:")
print(f"Highest Sales Category: {highest_category}")
print(f"Highest Sales Region: {highest_region}")
print(f"Highest Sales Segment: {highest_segment}")
print(f"Highest Sales Month: {highest_month}")

print("\nAll visualizations have been saved successfully.")