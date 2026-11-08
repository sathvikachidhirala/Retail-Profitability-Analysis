import pandas as pd

file_path = r"C:\Users\SATHWIKA\Documents\Retail_Profitability_Optimization\data\superstore_cleaned.csv"

df = pd.read_csv(file_path)

regional_analysis = df.groupby("Region").agg(
    Sales=("Sales", "sum"),
    Profit=("Profit", "sum"),
    Orders=("Order ID", "nunique"),
    Customers=("Customer ID", "nunique")
)

regional_analysis["Profit Margin"] = (
    regional_analysis["Profit"] / regional_analysis["Sales"]
) * 100

regional_analysis = regional_analysis.sort_values(
    by="Profit", ascending=False
)

print("Regional Business Performance")
print(regional_analysis.round(2))