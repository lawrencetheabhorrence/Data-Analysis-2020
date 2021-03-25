#!/usr/bin/env python3

import math

def inputShape():
  shape = ''
  while True:
    shape = input('Choose a shape (triangle, rectangle, circle): ')
    if shape == '': return 0
    if not (shape == 'triangle' or shape == 'rectangle' or shape == 'circle'):
      shape = ''
      print('Unknown shape!')
    else: break

  if (shape == 'triangle'): inputTri()
  if (shape == 'rectangle'): inputRec()
  if (shape == 'circle'): inputCirc()

def areaTri(b, h): return 0.5 * b * h
def areaRec(w, h): return w * h
def areaCirc(r): return math.pi * r * r

def inputTri():
  b = int(input('Give base of the triangle: '))
  h = int(input('Give height of the triangle: '))
  print('The area is', areaTri(b, h))

def inputRec():
  w = int(input('Give width of the rectangle: '))
  h = int(input('Give height of the rectangle: '))
  print('The area is', areaRec(w, h))

def inputCirc():
  r = int(input('Give radius of the circle: '))
  print('The area is', areaCirc(r))

def main():
  while True:
    i = inputShape()
    if (i == 0): break


if __name__ == "__main__":
    main()
