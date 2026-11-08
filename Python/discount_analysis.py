import pandas as pd

file_path = r"C:\Users\SATHWIKA\Documents\Retail_Profitability_Optimization\data\superstore_cleaned.csv"

df = pd.read_csv(file_path)

discount_analysis = df.groupby("Discount").agg(
    Sales=("Sales", "sum"),
    Profit=("Profit", "sum"),
    Orders=("Order ID", "nunique")
)

discount_analysis["Profit Margin"] = (
    discount_analysis["Profit"] / discount_analysis["Sales"]
) * 100

print("Discount-wise Business Performance")
print(discount_analysis.round(2))

print("\nAverage Profit by Discount:")
print(df.groupby("Discount")["Profit"].mean().round(2))