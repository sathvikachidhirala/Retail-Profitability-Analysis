import pandas as pd

file_path = r"C:\Users\SATHWIKA\Documents\Retail_Profitability_Optimization\data\superstore.xls"

df = pd.read_excel(file_path)

df["Profit Margin"] = (df["Profit"] / df["Sales"]) * 100

df.to_csv(
    r"C:\Users\SATHWIKA\Documents\Retail_Profitability_Optimization\data\superstore_cleaned.csv",
    index=False
)

print("Cleaned dataset saved successfully!")

print("\nProfit Margin:")
print(df[["Sales", "Profit", "Profit Margin"]].head())

print("\nNegative profit records:", (df["Profit"] < 0).sum())

print("\nOverall Sales:", df["Sales"].sum())
print("Overall Profit:", df["Profit"].sum())