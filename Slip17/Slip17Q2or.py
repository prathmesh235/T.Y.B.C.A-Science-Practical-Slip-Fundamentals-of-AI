
import pandas as pd
from sklearn.linear_model import LinearRegression

# Create a sample dataset
data = {
    "YearsExperience": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    "Salary": [25000, 30000, 35000, 40000, 45000,
               50000, 55000, 60000, 65000, 70000]
}

df = pd.DataFrame(data)

# Select input and output
X = df[["YearsExperience"]]
y = df["Salary"]

# Train the model
model = LinearRegression()
model.fit(X, y)

# Take user input
years = float(input("Enter years of experience: "))

# Predict salary
predicted_salary = model.predict(
    pd.DataFrame({"YearsExperience": [years]})
)

print("Predicted Salary:", round(predicted_salary[0], 2))
