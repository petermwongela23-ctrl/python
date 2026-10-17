# ============================================
# STEP 3: NUMBER CRUNCHING WITH NUMPY
# ============================================

import numpy as np
import pandas as pd

# Load the data
data = pd.read_csv("students.csv")

# Turn the score column into a NumPy array
scores = np.array(data["score"])
study = np.array(data["study_hours"])

print("=== Scores array ===")
print(scores)

print("\n=== NumPy Statistics ===")
print("Mean (average):", scores.mean())
print("Max:", scores.max())
print("Min:", scores.min())
print("Standard deviation:", round(scores.std(), 2))

print("\n=== Math on ALL values at once ===")
# Add 5 bonus points to every score (no loop needed!)
bonus_scores = scores + 5
print("With +5 bonus:", bonus_scores)

print("\n=== Correlation (do study hours relate to scores?) ===")
# Value close to 1.0 means strong positive relationship
correlation = np.corrcoef(study, scores)[0, 1]
print("Study vs Score correlation:", round(correlation, 2))