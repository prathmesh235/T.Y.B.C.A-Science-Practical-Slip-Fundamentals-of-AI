
import pandas as pd
from sklearn.linear_model import LinearRegression

# Create DataFrame
data = {
    'Temperature': [20, 22, 25, 28, 30, 32, 35],
    'IceCreams_Sold': [100, 120, 150, 180, 200, 220, 250]
}

df = pd.DataFrame(data)

print("Ice Cream Sales Data:")
print(df)

# Train Linear Regression Model
X = df[['IceCreams_Sold']]
y = df['Temperature']

model = LinearRegression()
model.fit(X, y)

# Predict temperature
sales = int(input("\nEnter number of ice creams sold: "))
prediction = model.predict([[sales]])

print("Predicted Temperature:", round(prediction[0], 2), "°C")
