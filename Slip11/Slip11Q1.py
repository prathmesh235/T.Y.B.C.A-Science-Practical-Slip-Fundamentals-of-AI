
import pandas as pd
from sklearn.linear_model import LinearRegression
from pathlib import Path

# Read CSV from the same folder as this Python file
file_path = Path(__file__).parent / "salary_data.csv"
data = pd.read_csv(file_path)

print("Salary Dataset:")
print(data.head())

X = data[["YearsExperience"]]
y = data["Salary"]

model = LinearRegression()
model.fit(X, y)

experience = float(input("\nEnter years of experience: "))

predicted_salary = model.predict(
    pd.DataFrame({"YearsExperience": [experience]})
)

print("Predicted Salary:", round(predicted_salary[0], 2))
