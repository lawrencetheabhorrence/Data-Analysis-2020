#!/usr/bin/env python3

import numpy as np

def first_half_second_half(a):
    m = len(a[0]) // 2
    c = np.sum(a[:, :m], axis = 1) > np.sum(a[:, m:], axis = 1)
    return a[c]


def main():
    a = np.array([[1, 3, 4, 2],
                  [2, 2, 1, 2]])
    print(first_half_second_half(a))

if __name__ == "__main__":
    main()
