# Decision Tree Regression

# Importing the libraries
import os
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.tree import DecisionTreeRegressor


def main():
    # Importing the dataset (resolve path relative to this script)
    script_dir = os.path.dirname(os.path.abspath(__file__))
    csv_path = os.path.join(script_dir, "Position_Salaries.csv")
    dataset = pd.read_csv(csv_path)
    X = dataset.iloc[:, 1:2].values
    y = dataset.iloc[:, 2].values

    # Fitting Decision Tree Regression to the dataset
    regressor = DecisionTreeRegressor(random_state=0)
    regressor.fit(X, y)

    # Predicting a new result (predict expects a 2D array)
    y_pred = regressor.predict([[6.5]])
    print(f"Predicted salary for level 6.5: {y_pred[0]:,.0f}")

    # Visualising the Decision Tree Regression results (higher resolution)
    X_grid = np.arange(min(X), max(X), 0.01)
    X_grid = X_grid.reshape((len(X_grid), 1))
    plt.scatter(X, y, color="red")
    plt.plot(X_grid, regressor.predict(X_grid), color="blue")
    plt.title("Truth or Bluff (Decision Tree Regression)")
    plt.xlabel("Position level")
    plt.ylabel("Salary")
    plt.show()


if __name__ == "__main__":
    main()
