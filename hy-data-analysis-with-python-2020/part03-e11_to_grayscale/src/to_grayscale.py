#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt

def to_grayscale(pic):
  pic_c = pic.copy()
  weights = np.array([0.2126, 0.7152, 0.0722])
  pic_c = pic * weights
  return pic_c.sum(axis = 2)

def to_red(pic):
  pic_c = pic.copy()
  weights = np.array([1, 0, 0])
  return pic * weights

def to_green(pic):
  pic_c = pic.copy()
  weights = np.array([0, 1, 0])
  return pic * weights

def to_blue(pic):
  pic_c = pic.copy()
  weights = np.array([0, 0, 1])
  return pic * weights

def main():
    pic = plt.imread('src/painting.png')
    gray = to_grayscale(pic)
    plt.imshow(gray, cmap='gray')

    fig, ax = plt.subplots(1, 3)
    ax[0].imshow(to_red(pic))
    ax[1].imshow(to_green(pic))
    ax[2].imshow(to_blue(pic))
    plt.show()

if __name__ == "__main__":
    main()
