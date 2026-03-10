import os
import pandas as pd

print("Starting ETL pipeline...")

# Determine project root (one level up from this script's directory)
script_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.dirname(script_dir)

# Build paths
input_file = os.path.join(project_root, "data", "Sample - Superstore.csv")
output_file = os.path.join(project_root, "output", "clean_superstore_sales.csv")

print("Input file:", input_file)

# -------------------
# EXTRACT
# -------------------
df = pd.read_csv(input_file, encoding="latin1")
print("Data extracted successfully")
print("Rows:", df.shape[0])
print("Columns:", df.shape[1])

# -------------------
# TRANSFORM
# -------------------
print("Transforming data...")

df = df.drop_duplicates()

if "Order Date" in df.columns:
    df["Order Date"] = pd.to_datetime(df["Order Date"], errors="coerce")

if "Profit" in df.columns and "Sales" in df.columns:
    df["Profit Margin"] = df["Profit"] / df["Sales"]

print("Transformation complete")

# -------------------
# LOAD
# -------------------
os.makedirs(os.path.dirname(output_file), exist_ok=True)
df.to_csv(output_file, index=False)

print("Cleaned data saved to:", output_file)
print("ETL pipeline finished successfully")