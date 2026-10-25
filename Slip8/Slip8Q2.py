
# Diabetes Prediction using Logistic Regression

from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler

# Sample dataset:
# [Fasting Sugar, Post-Meal Sugar, Age, BMI]
X = [
    [80, 110, 22, 21],
    [85, 120, 25, 23],
    [90, 125, 28, 24],
    [78, 115, 24, 22],
    [88, 130, 30, 25],
    [95, 135, 32, 26],
    [82, 118, 27, 23],
    [92, 128, 29, 24],
    [110, 180, 45, 30],
    [125, 200, 50, 32],
    [140, 220, 55, 35],
    [130, 210, 60, 34],
    [115, 190, 48, 31],
    [150, 240, 65, 36],
    [135, 215, 58, 33],
    [120, 195, 52, 30],
    [86, 122, 26, 22],
    [145, 230, 62, 37],
    [105, 170, 42, 29],
    [155, 250, 68, 38]
]

# 0 = Non-Diabetic, 1 = Diabetic
y = [
    0, 0, 0, 0, 0, 0, 0, 0,
    1, 1, 1, 1, 1, 1, 1, 1,
    0, 1, 1, 1
]

# Create and train the model
model = make_pipeline(
    StandardScaler(),
    LogisticRegression(random_state=0)
)

model.fit(X, y)

# New persons to predict
persons = [
    [82, 115, 24, 22],
    [130, 210, 55, 34],
    [95, 140, 35, 26],
    [145, 235, 62, 36]
]

print("Diabetes Prediction Results")
print("-" * 35)

for i, person in enumerate(persons, start=1):
    prediction = model.predict([person])[0]

    if prediction == 1:
        status = "Diabetic"
    else:
        status = "Non-Diabetic"

    print("Person", i, ":", status)
