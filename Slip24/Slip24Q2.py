
from sklearn.tree import DecisionTreeClassifier

# Features:
# Is leafy vegetable? (1 = Yes, 0 = No)
# Grows from flower? (1 = Yes, 0 = No)

X = [
    [1, 0],  # Spinach
    [1, 0],  # Cabbage
    [1, 0],  # Lettuce
    [0, 1],  # Tomato
    [0, 1],  # Brinjal
    [0, 1]   # Capsicum
]

# Labels: 0 = Leafy, 1 = Fruit Vegetable
y = [0, 0, 0, 1, 1, 1]

# Create and train the Decision Tree model
model = DecisionTreeClassifier(random_state=0)
model.fit(X, y)

# Take input from the user
leafy = int(input("Is it a leafy vegetable? (1 = Yes, 0 = No): "))
flower = int(input("Does it grow from a flower? (1 = Yes, 0 = No): "))

# Predict the vegetable type
prediction = model.predict([[leafy, flower]])

if prediction[0] == 0:
    print("Predicted Type: Leafy Vegetable")
else:
    print("Predicted Type: Fruit Vegetable")
