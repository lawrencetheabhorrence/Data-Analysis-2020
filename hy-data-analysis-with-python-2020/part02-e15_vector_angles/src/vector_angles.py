#!/usr/bin/env python3

import numpy as np
import scipy.linalg
import math

def inner_product(X, Y):
  return np.sum(X * Y, axis = 1)

def norm (X):
  return inner_product(X, X) ** (1/2)

def vector_angles(X, Y):
    numerator = inner_product(X, Y)
    divisor = norm(X) * norm(Y)
    cos = np.clip(numerator / divisor, -1.0, 1.0)
    print(numerator, divisor, cos)
    return np.arccos(cos) * 180.0 / math.pi

def main():
    X = np.arange(10).reshape(5, 2)
    Y = np.arange(10, 20).reshape(5, 2)
    print(vector_angles(X, Y))

if __name__ == "__main__":
    main()
