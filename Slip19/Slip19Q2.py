
import pandas as pd
from sklearn.datasets import load_diabetes

# Load the built-in Diabetes dataset
diabetes = load_diabetes()

# Convert the dataset into a DataFrame
df = pd.DataFrame(
    diabetes.data,
    columns=diabetes.feature_names
)

# Display first 7 rows
print("First 7 Rows of Diabetes Dataset:")
print(df.head(7))

# Display shape
print("\nShape of Dataset:", df.shape)
