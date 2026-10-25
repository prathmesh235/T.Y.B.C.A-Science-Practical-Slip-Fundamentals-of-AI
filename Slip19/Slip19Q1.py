
import pandas as pd

# Create a DataFrame
data = {
    "Name": ["Amit", "Priya", "Rahul", "Sneha", "Neha"],
    "Age": [25, 20, 30, 22, 27]
}

df = pd.DataFrame(data)

print("Original DataFrame:")
print(df)

# Sort by Age in ascending order
sorted_df = df.sort_values(by="Age", ascending=True)

print("\nDataFrame Sorted by Age:")
print(sorted_df)
