#!/usr/bin/env python3

import pandas as pd
from sklearn import linear_model
import numpy as np


def coefficient_of_determination():
    df = pd.read_csv('src/mystery_data.tsv', sep='\t')
    df = df.astype(float)
    x1 = df['X1'].to_numpy()
    x2 = df['X2'].to_numpy()
    x3 = df['X3'].to_numpy()
    x4 = df['X4'].to_numpy()
    x5 = df['X5'].to_numpy()
    y = df['Y'].to_numpy()

    model = linear_model.LinearRegression(fit_intercept=True)
    x = np.vstack([x1, x2, x3, x4, x5])
    scores = []
    model.fit(x.T, y)
    scores.append(model.score(x.T, y))
    model.fit(x1.reshape(-1, 1), y)
    scores.append(model.score(x1.reshape(-1, 1), y))
    model.fit(x2.reshape(-1, 1), y)
    scores.append(model.score(x2.reshape(-1, 1), y))
    model.fit(x3.reshape(-1, 1), y)
    scores.append(model.score(x3.reshape(-1, 1), y))
    model.fit(x4.reshape(-1, 1), y)
    scores.append(model.score(x4.reshape(-1, 1), y))
    model.fit(x5.reshape(-1, 1), y)
    scores.append(model.score(x5.reshape(-1, 1), y))
    return scores

def main():
    scores = coefficient_of_determination()
    for i, x in enumerate(scores):
        if (i == 0):
            print(f'R2-score with feature(s) X: {x}')
            continue
        print(f'R2-score with feature(s) X{i}: {x}')

if __name__ == "__main__":
    main()
