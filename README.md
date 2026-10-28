# CodeAlpha Data Visualization

## Project Overview

This project was completed as part of the **CodeAlpha Data Analytics Internship**.

The objective of this project is to analyze a retail sales dataset and create meaningful visualizations that help identify sales patterns, category performance, regional performance, customer segments, and monthly sales trends.

The project uses **Python, Pandas, Matplotlib, and Seaborn** for data processing and visualization.

---

## Dataset

**Dataset:** Superstore Sales Dataset

The dataset contains **9,800 records and 18 columns** related to retail orders and sales.

### Main Dataset Fields

- Row ID
- Order ID
- Order Date
- Ship Date
- Ship Mode
- Customer ID
- Customer Name
- Segment
- Country
- City
- State
- Postal Code
- Region
- Product ID
- Category
- Sub-Category
- Product Name
- Sales

---

## Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- VS Code

---

## Data Preparation

The project includes the following data preparation steps:

- Loaded the CSV dataset using Pandas
- Converted Order Date and Ship Date into datetime format
- Checked missing values
- Checked duplicate records
- Removed duplicate rows where applicable
- Created Year and Month fields from Order Date
- Prepared grouped datasets for visualization
- Exported a cleaned dataset for further use

---

## Visualizations Created

The project generates the following visualizations:

1. **Sales by Category**
2. **Sales by Region**
3. **Monthly Sales Trend**
4. **Top 10 Products by Sales**
5. **Sales by Sub-Category**
6. **Sales by Customer Segment**
7. **Sales Distribution**
8. **Category and Region Heatmap**
9. **Sales by Ship Mode**

All visualizations are saved as high-resolution PNG files in the `outputs` folder.

---

## Key Findings

The analysis produced several useful business insights:

- **Technology** was the highest-selling category.
- **West** was the highest-performing region by sales.
- **Consumer** was the customer segment generating the highest sales.
- **November 2018** recorded the highest monthly sales.
- The dataset contains **9,800 records**.
- Total recorded sales were approximately **$2.26 million**.
- The average recorded sale was approximately **$230.77**.
- No duplicate rows were found in the dataset.

---

## Data Quality

The dataset was checked for missing values and duplicate records.

- Duplicate rows: **0**
- Missing Postal Code values: **11**
- Other major fields contained no missing values.

The missing postal code values do not affect the sales visualizations because postal code is not required for the primary analysis.

---

## Project Structure

```text
CodeAlpha_DataVisualization/
│
├── train.csv
├── visualization_analysis.py
├── requirements.txt
├── README.md
│
└── outputs/
    ├── category_region_heatmap.png
    ├── cleaned_sales_data.csv
    ├── monthly_sales_trend.png
    ├── sales_by_category.png
    ├── sales_by_region.png
    ├── sales_by_segment.png
    ├── sales_by_ship_mode.png
    ├── sales_by_subcategory.png
    ├── sales_distribution.png
    ├── top_10_products.png
    └── visualization_summary.md
```

---

## How to Run the Project

### 1. Clone or download the repository

```bash
git clone <YOUR_GITHUB_REPOSITORY_URL>
```

### 2. Open the project folder

```bash
cd CodeAlpha_DataVisualization
```

### 3. Install the required libraries

```bash
pip install -r requirements.txt
```

### 4. Run the visualization script

```bash
python visualization_analysis.py
```

The generated charts and analysis files will be saved automatically in the `outputs` folder.

---

## Internship

**Program:** CodeAlpha Data Analytics Internship

**Task:** Task 3 - Data Visualization

**Project Type:** Retail Sales Data Visualization

---

## Conclusion

This project demonstrates how Python-based data visualization can be used to transform raw retail sales data into meaningful business insights.

The visualizations provide a clear understanding of category performance, regional sales, customer segments, product performance, sales trends, and other important patterns within the dataset.