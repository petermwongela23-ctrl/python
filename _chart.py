# ============================================
# STEP 4: MAKE CHARTS WITH MATPLOTLIB
# ============================================

import pandas as pd  # pyright: ignore[reportMissingModuleSource]
import matplotlib.pyplot as plt  # pyright: ignore[reportMissingModuleSource]

# Load the data
data = pd.read_csv("students.csv")

# Create a figure with 2 charts side by side
fig, (chart1, chart2) = plt.subplots(1, 2, figsize=(12, 5))

# --- CHART 1: Bar chart of each student's score ---
chart1.bar(data["name"], data["score"], color="skyblue")
chart1.set_title("Exam Score by Student")
chart1.set_xlabel("Student")
chart1.set_ylabel("Score")
chart1.tick_params(axis="x", rotation=45)   # tilt names so they fit

# --- CHART 2: Scatter plot (study hours vs score) ---
chart2.scatter(data["study_hours"], data["score"], color="green", s=100)
chart2.set_title("Study Hours vs Score")
chart2.set_xlabel("Study Hours")
chart2.set_ylabel("Score")

# Add a grid for easier reading
chart2.grid(True)

# Adjust spacing so labels don't overlap
plt.tight_layout()

# Save the chart as an image file
plt.savefig("my_first_chart.png")
print("Chart saved as 'my_first_chart.png'!")

# Show the chart in a window
plt.show()