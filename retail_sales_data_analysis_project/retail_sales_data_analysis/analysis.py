from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt

ROOT = Path(__file__).resolve().parent
DATA_PATH = ROOT / "data" / "retail_sales.csv"
OUTPUT_DIR = ROOT / "outputs"
OUTPUT_DIR.mkdir(exist_ok=True)

def load_and_clean(path=DATA_PATH):
    df = pd.read_csv(path)
    df["order_date"] = pd.to_datetime(df["order_date"], errors="coerce")
    df["product"] = df["product"].astype("string").str.strip()
    df["region"] = df["region"].fillna("Unknown")
    df["quantity"] = pd.to_numeric(df["quantity"], errors="coerce")
    df["unit_price"] = pd.to_numeric(df["unit_price"], errors="coerce")
    df["discount_pct"] = pd.to_numeric(df["discount_pct"], errors="coerce").fillna(0)
    df["unit_cost"] = pd.to_numeric(df["unit_cost"], errors="coerce")
    df = df.drop_duplicates()
    df = df.dropna(subset=["order_date", "product", "quantity", "unit_price", "unit_cost"])
    df = df[df["quantity"] > 0].copy()
    df["gross_sales"] = df["quantity"] * df["unit_price"]
    df["net_sales"] = df["gross_sales"] * (1 - df["discount_pct"])
    df["total_cost"] = df["quantity"] * df["unit_cost"]
    df["profit_estimate"] = df["net_sales"] - df["total_cost"]
    df["month"] = df["order_date"].dt.to_period("M").astype(str)
    return df

def main():
    df = load_and_clean()
    print("CLEANED DATA SUMMARY")
    print(f"Rows after cleaning: {len(df):,}")
    print(f"Net sales: ${df['net_sales'].sum():,.2f}")
    print(f"Estimated profit: ${df['profit_estimate'].sum():,.2f}")
    print(f"Average order value (row-level): ${df['net_sales'].mean():,.2f}")

    monthly = df.groupby("month", as_index=False)["net_sales"].sum()
    monthly.to_csv(OUTPUT_DIR / "monthly_sales_summary.csv", index=False)
    top_products = df.groupby("product", as_index=False)["net_sales"].sum().sort_values("net_sales", ascending=False)
    top_products.to_csv(OUTPUT_DIR / "product_sales_summary.csv", index=False)
    region = df.groupby("region", as_index=False)["net_sales"].sum().sort_values("net_sales", ascending=False)
    region.to_csv(OUTPUT_DIR / "region_sales_summary.csv", index=False)

    plt.figure(figsize=(10, 5))
    plt.plot(monthly["month"], monthly["net_sales"], marker="o")
    plt.title("Monthly Net Sales")
    plt.xlabel("Month")
    plt.ylabel("Net sales ($)")
    plt.xticks(rotation=45, ha="right")
    plt.tight_layout()
    plt.savefig(OUTPUT_DIR / "monthly_sales.png", dpi=150)
    plt.close()

    plt.figure(figsize=(9, 5))
    plt.barh(top_products["product"], top_products["net_sales"])
    plt.title("Net Sales by Product")
    plt.xlabel("Net sales ($)")
    plt.tight_layout()
    plt.savefig(OUTPUT_DIR / "product_sales.png", dpi=150)
    plt.close()

    plt.figure(figsize=(8, 5))
    plt.bar(region["region"], region["net_sales"])
    plt.title("Net Sales by Region")
    plt.xlabel("Region")
    plt.ylabel("Net sales ($)")
    plt.tight_layout()
    plt.savefig(OUTPUT_DIR / "region_sales.png", dpi=150)
    plt.close()

    print("\\nTop products by net sales:")
    print(top_products.head(5).to_string(index=False))
    print("\\nSales by region:")
    print(region.to_string(index=False))
    print(f"\\nCharts and summary CSVs saved in: {OUTPUT_DIR}")

if __name__ == "__main__":
    main()
