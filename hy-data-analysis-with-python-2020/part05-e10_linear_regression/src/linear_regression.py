#!/usr/bin/env python3

import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

def fit_line(x, y):
    model = LinearRegression(fit_intercept=True)
    x = x.reshape(-1, 1)
    model.fit(x, y)
    return (model.coef_[0], model.intercept_)

def main():
    x = np.array([0, 4, 5, 6])
    y = np.array([2, 3, 5, 7])
    slope, intercept = fit_line(x, y)
    print(f'Slope: {slope}')
    print(f'Intercept: {intercept}')
    xfit = x
    yfit = slope * x + intercept
    plt.plot(xfit, yfit, color="black")
    plt.plot(x, y, 'o')
    plt.show()

if __name__ == "__main__":
    main()
