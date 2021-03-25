#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt
import math

def center(a):
    a_c = a.copy()
    x = (len(a_c[0]) - 1) / 2
    y = (len(a_c) - 1) / 2
    return (y,x)   # note the order: (center_y, center_x)

def radial_distance(a):
    a_c = a.copy()
    y, x = center(a_c)
    row = np.arange(len(a_c[0]))
    col = np.arange(len(a_c)).reshape(len(a_c), 1)
    return ((row - x) ** 2 + (col - y) ** 2) ** 0.5

def scale(a, tmin=0.0, tmax=1.0):
    """Returns a copy of array 'a' with its values scaled to be in the range
[tmin,tmax]."""
    a_c = a.copy()
    a_max = np.max(a_c)
    if(a_max > 0):
      max_s = tmax / a_max
      a_c =  a_c * (max_s)
    return np.clip(a_c, 0, 1)

def radial_mask(a):
    a_c = a.copy()
    return scale(1 - radial_distance(a_c))

def radial_fade(a):
    mask = radial_mask(a)
    a_c = a.copy()
    for i in range(0, len(a_c)):
      for j in range(0, len(a_c[0])):
        a_c[i][j] *= mask[i][j]
    return a_c

def main():
    print(radial_mask(np.array([[[0, 0, 0]]])))
    pic = plt.imread('src/painting.png')
    mask = radial_mask(pic)
    fade = radial_fade(pic)
    fig, ax = plt.subplots(3, 1)
    ax[0] = plt.imshow(pic)
    ax[1] = plt.imshow(mask)
    ax[2] = plt.imshow(fade)
    plt.show()

if __name__ == "__main__":
    main()
