
import pandas as pd
from sklearn.linear_model import LinearRegression

# Create a sample dataset
data = {
    "Area": [1000, 1200, 1500, 1800, 2000, 2200],
    "Bedrooms": [2, 2, 3, 3, 4, 4],
    "Price": [25, 30, 40, 45, 55, 60]
}

df = pd.DataFrame(data)

# Input features and target
X = df[["Area", "Bedrooms"]]
y = df["Price"]

# Train the Multiple Linear Regression model
model = LinearRegression()
model.fit(X, y)

# Take input from the user
area = float(input("Enter house area (sq.ft): "))
bedrooms = int(input("Enter number of bedrooms: "))

# Predict house price
new_house = pd.DataFrame({
    "Area": [area],
    "Bedrooms": [bedrooms]
})

predicted_price = model.predict(new_house)

print("Predicted House Price: ₹", round(predicted_price[0] * 100000, 2))
