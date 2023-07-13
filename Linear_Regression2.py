import numpy as np
from sklearn.linear_model import LinearRegression

# Sample input features (X) and target values (y)
X = np.array([[1], [2], [3], [4], [5]])
y = np.array([2, 4, 6, 8, 10])

# Create and fit the linear regression model
model = LinearRegression()
model.fit(X, y)

# Predict target values for new input features
X_new = np.array([[6], [7]])
y_pred = model.predict(X_new)

# Print the predicted values
for i in range(len(X_new)):
    print("Predicted value for X = {}: {}".format(X_new[i][0], y_pred[i]))
