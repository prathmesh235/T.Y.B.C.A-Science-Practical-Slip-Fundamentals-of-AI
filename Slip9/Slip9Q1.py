
# Sort DataFrame by Age in Ascending Order

import pandas as pd

# Create DataFrame
data = {
    "Name": ["Rahul", "Amit", "Priya", "Sneha", "Rohit"],
    "Age": [25, 20, 30, 22, 18]
}

df = pd.DataFrame(data)

print("Original DataFrame:")
print(df)

# Sort by Age in ascending order
sorted_df = df.sort_values(by="Age", ascending=True)

print("\nDataFrame Sorted by Age:")
print(sorted_df)
