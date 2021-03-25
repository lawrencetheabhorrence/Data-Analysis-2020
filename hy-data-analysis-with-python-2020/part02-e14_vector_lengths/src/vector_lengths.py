#!/usr/bin/env python3

import numpy as np
import scipy.linalg

def vector_lengths(a):
    a = a ** 2
    return a.sum(axis = 1) ** 0.5
def main():
    a = np.arange(15).reshape(5, 3)
    print(vector_lengths(a))

if __name__ == "__main__":
    main()
