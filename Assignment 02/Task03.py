import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("../Assignment 04/weight-height.csv")

length_in = data["Height"]
weight_lb = data["Weight"]

length_cm = length_in * 2.54
weight_kg = weight_lb * 0.453592

print("Mean length in cm is:", length_cm.mean())
print("Mean weight in kg is:", weight_kg.mean())

plt.hist(length_cm, bins=20, color='Red', edgecolor='Blue')
plt.title("Student Height Histogram")
plt.xlabel("Height (cm)")
plt.ylabel("Frequency")
plt.grid(True)
plt.show()
