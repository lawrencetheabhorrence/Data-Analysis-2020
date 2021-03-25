#!/usr/bin/env python3

import numpy as np

def multiplication_table(n):
    X = np.arange(n)
    Y = np.arange(n).reshape(n, 1)
    return X * Y

def main():
    print(multiplication_table(4))

if __name__ == "__main__":
    main()
