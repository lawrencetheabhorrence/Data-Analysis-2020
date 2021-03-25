#!/usr/bin/env python3

import numpy as np
from functools import reduce

def matrix_power(a, n):
    if n == 0: return np.eye(len(a))
    if n < 0: a, n = np.linalg.inv(a), n * -1

    a_l = ( a for b in range(0, n) )
    return reduce(lambda x, y: x @ y, a_l, np.eye(len(a)))

def main():
    a = np.arange(0,9).reshape(3, 3)
    print(matrix_power(a, 3))

if __name__ == "__main__":
    main()
