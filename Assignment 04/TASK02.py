import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score, mean_squared_error, mean_absolute_error
import numpy as np


data = pd.read_csv("weight-height.csv")
X = data[["Height"]].values
y = data["Weight"].values


plt.scatter(X, y, color="blue")
plt.xlabel("Height")
plt.ylabel("Weight")
plt.title("Scatter Plot")
plt.show()

model = LinearRegression()
model.fit(X, y)
y_pred = model.predict(X)

yhat = model.intercept_ + model.coef_[0] * X



plt.scatter(X, y, color="blue", label="Data")
plt.plot(X, y_pred, color="green", label=f"Regression Line ")
plt.xlabel("HEIGHT")
plt.ylabel(" WEIGHT")
plt.title("Linear Regression of Height vs Weight")
plt.legend()
plt.show()

RSS = np.sum((y - y_pred) ** 2)
MSE = mean_squared_error(y, y_pred)
RMSE = np.sqrt(MSE)
MAE = mean_absolute_error(y, y_pred)
R2 = r2_score(y, y_pred)

# print(data.head())
# print(data.columns)


print("Intercept :", model.intercept_)
print("Coefficient or slope  :", model.coef_[0])
# print("Values of Yhat:", y_pred)
# print("Residual Sum of Squares (RSS):", RSS)
# print("Mean Squared Error (MSE):", MSE)
print("Root Mean Squared Error (RMSE):", RMSE)
print("Mean Absolute Error (MAE):", MAE)
print("R-squared (R²):", R2)

