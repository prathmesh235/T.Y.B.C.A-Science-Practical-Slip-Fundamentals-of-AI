
# Scatter Plot of Iris Dataset

import matplotlib.pyplot as plt
from sklearn.datasets import load_iris

# Load the Iris dataset
iris = load_iris()

# Extract petal length and petal width
petal_length = iris.data[:, 2]
petal_width = iris.data[:, 3]

# Plot scatter plot
plt.scatter(petal_length, petal_width)

# Add labels and title
plt.xlabel("Petal Length (cm)")
plt.ylabel("Petal Width (cm)")
plt.title("Petal Length vs Petal Width - Iris Dataset")

# Display the plot
plt.show()
