
import pandas as pd
from sklearn.linear_model import LogisticRegression

# Create sample transaction dataset
data = {
    "Amount": [500, 1000, 20000, 30000, 800,
               15000, 600, 25000, 1200, 40000],
    "CardAge": [5, 4, 1, 0.5, 6, 1, 7, 0.2, 3, 0.1],
    "Time": [14, 12, 2, 3, 16, 1, 11, 2, 15, 0],
    "LocationMatch": [95, 90, 20, 10, 98,
                      30, 92, 15, 85, 5],
    "Online": [0, 1, 1, 1, 0, 1, 0, 1, 0, 1],
    "Fraud": [0, 0, 1, 1, 0, 1, 0, 1, 0, 1]
}

df = pd.DataFrame(data)

# Separate features and target
X = df[["Amount", "CardAge", "Time",
        "LocationMatch", "Online"]]
y = df["Fraud"]

# Train the Logistic Regression model
model = LogisticRegression(max_iter=1000)
model.fit(X, y)

# Get transaction details from user
amount = float(input("Enter transaction amount: "))
age = float(input("Enter card age in years: "))
time = int(input("Enter transaction time (0-23): "))
location = float(input("Enter location match score (0-100): "))
online = int(input("Online transaction? (0=No, 1=Yes): "))

# Validate input
if amount < 0 or age < 0 or not 0 <= time <= 23:
    print("Invalid amount, card age, or transaction time.")
elif not 0 <= location <= 100 or online not in [0, 1]:
    print("Invalid location score or online status.")
else:
    # Predict transaction status
    transaction = pd.DataFrame(
        [[amount, age, time, location, online]],
        columns=["Amount", "CardAge", "Time",
                 "LocationMatch", "Online"]
    )

    prediction = model.predict(transaction)[0]

    if prediction == 1:
        print("Prediction: Fraudulent Transaction (1)")
    else:
        print("Prediction: Legitimate Transaction (0)")
