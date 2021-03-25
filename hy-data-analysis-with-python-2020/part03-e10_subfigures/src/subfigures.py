#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt

def subfigures(a):
    x, y, c, s = a[:, 0], a[:, 1], a[:, 2], a[:, 3]
    fig, ax = plt.subplots(1, 2)
    ax[0].plot(x, y)
    ax[1].scatter(x, y, c=c, s=s)
    plt.show()


def main():
    a = np.array(([1, 3, 5, 2], [3, 5, 2, 5], [5, 6, 4, 3], [23, 13, 12, 15]))
    a = np.transpose(a)
    print(a)
    subfigures(a)

if __name__ == "__main__":
    main()
