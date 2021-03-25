#!/usr/bin/env python3

import pandas as pd
from sklearn.linear_model import LinearRegression
import numpy as np

def mystery_data():
    df = pd.read_csv('src/mystery_data.tsv', sep='\t')
    df = df.astype(float)
    x1 = df['X1'].to_numpy()
    x2 = df['X2'].to_numpy()
    x3 = df['X3'].to_numpy()
    x4 = df['X4'].to_numpy()
    x5 = df['X5'].to_numpy()
    y = df['Y'].to_numpy()

    model = LinearRegression(fit_intercept=False)
    x = np.vstack([x1, x2, x3, x4, x5])
    model.fit(x.T, y)
    return model.coef_

def main():
    coefficients = mystery_data()
    # print the coefficients here

    for x in range(1, 6):
        print(f'Coefficient of X{x} is {coefficients[x-1]}')

if __name__ == "__main__":
    main()
