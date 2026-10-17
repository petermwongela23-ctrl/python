# ============================================
# STEP 5: PREDICT SCORES WITH MACHINE LEARNING
# ============================================

import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# Load the data
data = pd.read_csv("students.csv")

# --- Prepare the data ---
# X = the INPUT (what we use to predict) → study hours
# y = the OUTPUT (what we want to predict) → score
X = data[["study_hours"]]   # double brackets = table format (required)
y = data["score"]

# --- Create and train the model ---
model = LinearRegression()
model.fit(X, y)             # the model "learns" from the data

print("=== Model trained! ===")
print("Slope (points gained per study hour):", round(model.coef_[0], 2))
print("Base score (0 study hours):", round(model.intercept_, 2))

# --- Make predictions ---
print("\n=== Predictions ===")
for hours in [3.5, 6.5, 12]:
    predicted = model.predict([[hours]])[0]
    print(f"Study {hours} hours -> predicted score: {round(predicted, 1)}")

# --- Visualize the prediction line ---
plt.scatter(data["study_hours"], data["score"],
            color="green", s=100, label="Real students")

# Draw the model's prediction line
plt.plot(data["study_hours"], model.predict(X),
         color="red", linewidth=2, label="Prediction line")

plt.title("Study Hours vs Score (with Prediction Line)")
plt.xlabel("Study Hours")
plt.ylabel("Score")
plt.legend()
plt.grid(True)
plt.savefig("prediction_chart.png")
print("\nPrediction chart saved as 'prediction_chart.png'!")
plt.show()