# ============================================
# STEP 2: LOAD & EXPLORE DATA WITH PANDAS
# ============================================

import pandas as pd

# Load the CSV file into a DataFrame (a smart table)
data = pd.read_csv("students.csv")

# --- Explore the data ---
print("=== First 5 rows ===")
print(data.head())

print("\n=== Shape (rows, columns) ===")
print(data.shape)        # e.g. (10, 4) = 10 rows, 4 columns

print("\n=== Column names ===")
print(data.columns.tolist())

print("\n=== Quick statistics ===")
print(data.describe())   # count, mean, min, max for number columns

print("\n=== Average score ===")
print("Mean score:", data["score"].mean())

print("\n=== Highest scoring student ===")
top = data[data["score"] == data["score"].max()]
print(top)

print("\n=== Students who scored above 80 ===")
high_scorers = data[data["score"] > 80]
print(high_scorers[["name", "score"]])