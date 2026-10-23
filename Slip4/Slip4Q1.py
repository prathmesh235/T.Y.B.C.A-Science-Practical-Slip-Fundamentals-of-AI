
# Voting Eligibility using Logistic Classification

from math import exp

# Training data: Age and voting eligibility
ages = [10, 15, 17, 18, 20, 25, 30, 40, 60]
labels = [0, 0, 0, 1, 1, 1, 1, 1, 1]

# Sigmoid function
def sigmoid(z):
    return 1 / (1 + exp(-z))

# Simple logistic classification model
def predict(age):
    probability = sigmoid(age - 18)
    if probability >= 0.5:
        return "Eligible to Vote"
    else:
        return "Not Eligible to Vote"

# Accept age from user
age = int(input("Enter person's age: "))

if age < 0:
    print("Invalid age")
else:
    print("Prediction:", predict(age))
