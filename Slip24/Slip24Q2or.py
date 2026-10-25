
from sklearn.ensemble import RandomForestClassifier

# Training dataset
# Features: Age, Exercise Hours per Week
X = [
    [20, 6],
    [25, 5],
    [30, 4],
    [35, 3],
    [40, 2],
    [45, 1],
    [22, 7],
    [28, 6],
    [50, 1],
    [55, 2]
]

# Labels: 1 = FIT, 0 = UNFIT
y = [1, 1, 1, 0, 0, 0, 1, 1, 0, 0]

# Train the Random Forest model
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X, y)

# Predict for multiple people
n = int(input("Enter number of people: "))

for i in range(n):
    print("\nPerson", i + 1)

    age = int(input("Enter age: "))
    exercise = float(input("Enter exercise hours per week: "))

    prediction = model.predict([[age, exercise]])

    if prediction[0] == 1:
        print("Fitness Status: FIT")
    else:
        print("Fitness Status: UNFIT")
