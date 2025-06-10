import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# Load and preprocess CSV
df = pd.read_csv("simplelinear.csv")

X = df.iloc[:, 0].values.reshape(-1, 1)
Y = df.iloc[:, 1].values

# Fit model
model = LinearRegression()
model.fit(X, Y)

# Predict
Y_pred = model.predict(X)

# Output
print("=== Simple Linear Regression ===")
print(f"Slope: {model.coef_[0]}")
print(f"Intercept: {model.intercept_}")

# Plot
plt.scatter(X, Y, color='blue', label='Actual')
plt.plot(X, Y_pred, color='red', label='Regression Line')
plt.xlabel("X")
plt.ylabel("Y")
plt.title("Simple Linear Regression")
plt.legend()
plt.grid(True)
plt.show()
