
import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

# Read CSV file from the same folder as this program
file_path = Path(__file__).parent / "car_data.csv"
data = pd.read_csv(file_path)

print(data.head())

# Create scatter plot
plt.scatter(data["Car_Age"], data["Selling_Price"])

plt.xlabel("Car Age (Years)")
plt.ylabel("Selling Price")
plt.title("Car Age vs Selling Price")
plt.grid(True)

plt.show()
