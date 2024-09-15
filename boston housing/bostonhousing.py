
# all required libraries
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import StandardScaler, PolynomialFeatures
from sklearn.metrics import mean_squared_error, r2_score
import matplotlib.pyplot as plt

# Load the dataset
data = pd.read_csv('/home/shray/Computer Vision/Codes/boston housing/boston-housing-dataset/train.csv')
# data

# drop ID column
data.drop(columns=['ID'], inplace = True)

# Split features and target
X = data.drop(columns=['medv'])
y = data['medv']

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=42)

# Create the linear regression model
model = LinearRegression()

# Train the model
model.fit(X_train, y_train)

model.score(X_test,y_test)

# Make predictions
y_pred = model.predict(X_test)

# Evaluate the model (error and goodness of the model)
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

# print total error and goodness of the model
print(f'Mean Squared Error: {mse}')
print(f'R-squared: {r2}')

# Visualize the predictions vs true values
# plt.scatter(y_test, y_pred)
# plt.xlabel("True Values")
# plt.ylabel("Predictions")
# plt.title("True vs Predicted Prices")
# plt.show()

