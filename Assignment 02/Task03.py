import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("weight-height.csv")

length_in = data["Height"]
weight_lb = data["Weight"]

length_cm = length_in * 2.54
weight_kg = weight_lb * 0.453592

print("Mean length (cm):", length_cm.mean())
print("Mean weight (kg):", weight_kg.mean())

plt.hist(length_cm, bins=20, color='skyblue', edgecolor='black')
plt.title("Histogram of Student Heights (cm)")
plt.xlabel("Height (cm)")
plt.ylabel("Frequency")
plt.grid(True)
plt.show()
