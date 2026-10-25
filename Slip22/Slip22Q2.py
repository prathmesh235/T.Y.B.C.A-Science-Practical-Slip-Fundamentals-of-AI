
import pandas as pd
from pathlib import Path

# Load CSV from the same folder as this Python file
file_path = Path(__file__).parent / "employee.csv"
data = pd.read_csv(file_path)

# a. Display first four rows
print("First Four Rows:")
print(data.head(4))

# b. Print dataset shape
print("\nShape of Dataset:")
print(data.shape)

# c. Show column names
print("\nColumn Names:")
print(data.columns.tolist())

# d. Identify missing values
print("\nMissing Values:")
print(data.isnull().sum())

# e. Display dataset information
print("\nDataset Information:")
data.info()
