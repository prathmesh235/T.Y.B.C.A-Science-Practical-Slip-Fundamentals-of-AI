
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# Create YouTube video dataset
data = {
    "Likes": [100, 200, 300, 400, 500, 600, 700, 800],
    "Views": [1000, 2200, 3000, 4200, 5100, 6300, 7100, 8500]
}

df = pd.DataFrame(data)

print("YouTube Video Dataset:")
print(df)

# Select predictor and target variables
X = df[["Likes"]]
y = df["Views"]

# Train Linear Regression model
model = LinearRegression()
model.fit(X, y)

# Predict views
predicted_views = model.predict(X)

print("\nPredicted Views for 500 Likes:")
print(round(model.predict(pd.DataFrame({"Likes": [500]}))[0]))

# Plot scatter plot and regression line
plt.scatter(df["Likes"], df["Views"], label="Actual Views")
plt.plot(df["Likes"], predicted_views, color="red",
         label="Regression Line")

plt.xlabel("Number of Likes")
plt.ylabel("Number of Views")
plt.title("YouTube Views Prediction using Linear Regression")
plt.legend()
plt.grid(True)
plt.show()
