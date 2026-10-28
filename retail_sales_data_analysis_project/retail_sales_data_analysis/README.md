# Retail Sales Data Analysis (Portfolio Starter Project)

## Overview
This project demonstrates a small end-to-end retail analytics workflow in Python: data cleaning, feature creation, summary analysis, and chart generation.

**Dataset note:** `data/retail_sales.csv` is a synthetic practice dataset created for this project. It is not real company data. Results describe this generated dataset only.

## Questions explored
- How do monthly net sales change over time?
- Which products generate the most net sales?
- Which regions have the highest net sales?
- What is the estimated profit after discounts and estimated product costs?

## Tools
- Python
- Pandas
- Matplotlib

## Project structure
```text
retail_sales_data_analysis/
├── data/
│   └── retail_sales.csv
├── notebooks/
│   └── analysis_walkthrough.ipynb
├── outputs/
│   ├── monthly_sales.png
│   ├── product_sales.png
│   ├── region_sales.png
│   └── summary CSV files (generated when run)
├── analysis.py
├── requirements.txt
└── README.md
```

## Run the project
1. Install Python 3.10+.
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run:
   ```bash
   python analysis.py
   ```

The script prints summary metrics and saves charts and CSV summaries in `outputs/`.

## Data cleaning decisions
- Standardizes the order date.
- Removes duplicate rows.
- Trims extra spaces from product names.
- Labels missing regions as `Unknown` so those rows remain available for sales analysis.
- Removes rows missing required date, product, quantity, price, or cost values.
- Excludes non-positive quantities.
- Calculates gross sales, net sales after discount, estimated cost, and estimated profit.

## Limitations
- The data is synthetic and designed for learning.
- Each row represents a transaction line, so the average net sales per row is not necessarily the same as average order value if an order contains multiple lines.
- Costs and discounts are generated for demonstration; profit is an estimate, not audited financial reporting.
- This project currently focuses on descriptive analysis, not forecasting or causal inference.

## Suggested next improvements
- Add SQL queries using SQLite.
- Add unit tests for data-cleaning rules.
- Add a dashboard using Power BI or Streamlit.
- Compare discount levels with estimated profit, carefully noting that correlation does not establish causation.

