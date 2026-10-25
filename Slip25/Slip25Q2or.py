
from sklearn.tree import DecisionTreeClassifier

# Features: [Weight in grams, Texture]
# Texture: Smooth = 0, Rough = 1

X = [
    [150, 0],
    [170, 0],
    [140, 0],
    [180, 1],
    [200, 1],
    [220, 1]
]

# Labels: Apple or Orange
y = ["Apple", "Apple", "Apple", "Orange", "Orange", "Orange"]

# Train the Decision Tree model
model = DecisionTreeClassifier(random_state=0)
model.fit(X, y)

# Accept input from the user
weight = float(input("Enter fruit weight (in grams): "))
texture = int(input("Enter texture (Smooth = 0, Rough = 1): "))

# Predict fruit type
prediction = model.predict([[weight, texture]])

print("Predicted Fruit:", prediction[0])
