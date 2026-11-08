import pandas as pd

file_path = r"C:\Users\SATHWIKA\Documents\Retail_Profitability_Optimization\data\superstore_cleaned.csv"

df = pd.read_csv(file_path)

subcategory_analysis = df.groupby("Sub-Category").agg(
    Sales=("Sales", "sum"),
    Profit=("Profit", "sum"),
    Quantity=("Quantity", "sum")
)

subcategory_analysis["Profit Margin"] = (
    subcategory_analysis["Profit"] / subcategory_analysis["Sales"]
) * 100

subcategory_analysis = subcategory_analysis.sort_values(
    by="Profit", ascending=True
)

print("Subcategory Profitability Analysis")
print(subcategory_analysis.round(2))

print("\nLoss-making Subcategories:")
print(subcategory_analysis[subcategory_analysis["Profit"] < 0].round(2))