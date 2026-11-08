import pandas as pd
import mysql.connector

file_path = r"C:\Users\SATHWIKA\Documents\Retail_Profitability_Optimization\data\superstore_cleaned.csv"

df = pd.read_csv(file_path)

df["Order Date"] = pd.to_datetime(df["Order Date"]).dt.strftime("%Y-%m-%d")
df["Ship Date"] = pd.to_datetime(df["Ship Date"]).dt.strftime("%Y-%m-%d")

connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="YOUR_PASSWORD",
    database="retail_analysis"
)

cursor = connection.cursor()

placeholders = ", ".join(["%s"] * len(df.columns))
query = f"INSERT INTO superstore VALUES ({placeholders})"

for row in df.itertuples(index=False, name=None):
    cursor.execute(query, row)

connection.commit()

print("Dataset imported successfully!")

cursor.close()
connection.close()