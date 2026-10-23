
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris

# Load Iris dataset
iris = load_iris()

sepal_length = iris.data[:, 0]
sepal_width = iris.data[:, 1]
species = iris.target

# Create scatter plot
for i, name in enumerate(iris.target_names):
    plt.scatter(
        sepal_length[species == i],
        sepal_width[species == i],
        label=name
    )

# Add title and labels
plt.title("Sepal Length vs Sepal Width - Iris Dataset")
plt.xlabel("Sepal Length (cm)")
plt.ylabel("Sepal Width (cm)")
plt.legend(title="Iris Species")
plt.grid(True)

# Display plot
plt.show()
