
import pandas as pd

# Create employee DataFrame
data = {
    "ID": [101, 102, 103, 104, 105],
    "Name": ["Amit", "Neha", "Rahul", "Priya", "Sneha"],
    "Age": [25, 30, 28, 35, 27],
    "Salary": [30000, 45000, 35000, 60000, 40000]
}

df = pd.DataFrame(data)

print("Original Employee Records:")
print(df)

# Sort employees by salary
print("\nEmployees Sorted by Salary:")
print(df.sort_values(by="Salary"))

# Filter employees with salary greater than 35000
print("\nEmployees with Salary > 35000:")
print(df[df["Salary"] > 35000])

# Update salary of employee with ID 103
df.loc[df["ID"] == 103, "Salary"] = 50000

print("\nRecords After Updating Salary:")
print(df)
