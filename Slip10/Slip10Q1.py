
# Separate Features and Target, Then Split the Dataset

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split

# Load the Iris dataset
iris = load_iris()

# Separate features and target variable
X = iris.data
y = iris.target

# Split dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Display dataset shapes
print("Original Dataset Shape:", X.shape)
print("Target Variable Shape:", y.shape)

print("\nTraining Dataset Shape:", X_train.shape)
print("Training Target Shape:", y_train.shape)

print("\nTesting Dataset Shape:", X_test.shape)
print("Testing Target Shape:", y_test.shape)
