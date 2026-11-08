import pandas as pd

file_path = r"C:\Users\SATHWIKA\Documents\Retail_Profitability_Optimization\data\superstore_cleaned.csv"

df = pd.read_csv(file_path)

total_sales = df["Sales"].sum()
total_profit = df["Profit"].sum()
total_orders = df["Order ID"].nunique()
total_customers = df["Customer ID"].nunique()
profit_margin = (total_profit / total_sales) * 100

print("Overall Business Performance")
print("---------------------------")
print(f"Total Sales: ${total_sales:,.2f}")
print(f"Total Profit: ${total_profit:,.2f}")
print(f"Total Orders: {total_orders}")
print(f"Total Customers: {total_customers}")
print(f"Profit Margin: {profit_margin:.2f}%")

print("\nCategory-wise Performance")

category_analysis = df.groupby("Category").agg(
    Sales=("Sales", "sum"),
    Profit=("Profit", "sum"),
    Quantity=("Quantity", "sum")
)

category_analysis["Profit Margin"] = (
    category_analysis["Profit"] / category_analysis["Sales"]
) * 100

print(category_analysis.round(2))