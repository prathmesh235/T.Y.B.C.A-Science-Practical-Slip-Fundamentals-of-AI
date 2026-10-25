
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split

# Load the Iris dataset
iris = load_iris()

# Features
X = iris.data

# Split into training and testing sets (80:20)
X_train, X_test, y_train, y_test = train_test_split(
    X, iris.target, test_size=0.2, random_state=42
)

# Print shapes
print("Shape of X_train:", X_train.shape)
print("Shape of X_test:", X_test.shape)
