
# Employee Salary Increment using Pandas

import pandas as pd

# Create employee DataFrame
data = {
    "Employee": ["Amit", "Priya", "Rahul", "Sneha"],
    "Salary": [30000, 40000, 50000, 35000],
    "Experience": [2, 5, 3, 1]
}

df = pd.DataFrame(data)

print("Original Employee DataFrame:")
print(df)

# Increase salary based on experience
df["Salary"] = df.apply(
    lambda row: row["Salary"] * 1.10
    if row["Experience"] < 3
    else row["Salary"] * 1.05,
    axis=1
)

# Display updated DataFrame
df["Salary"] = df["Salary"].astype(int)

print("\nUpdated Employee DataFrame:")
print(df)
