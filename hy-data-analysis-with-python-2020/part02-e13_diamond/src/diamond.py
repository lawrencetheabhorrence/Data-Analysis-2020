#!/usr/bin/env python3

import numpy as np

def diamond(n):
    eye = np.eye(n, dtype = int)
    eyef = eye[::-1]

    tleft = eyef
    tright = eye[:, 1:]
    bleft = eye[1:]
    bright = eyef[1:, 1:]

    top = np.concatenate((tleft, tright), axis=1)
    bottom = np.concatenate((bleft, bright), axis=1)
    return np.concatenate((top, bottom))

def main():
    print(diamond(3))
    print(diamond(1))

if __name__ == "__main__":
    main()
