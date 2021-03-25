#!/usr/bin/env python3

import math

def solve_quadratic(a, b, c):
    return((b*-1 + math.sqrt(b*b - 4 * a * c))/(2 * a), (b*-1 - math.sqrt(b*b - 4 * a * c))/(2 * a))


def main():
    while True:
      a = int(input('a: '))
      b = int(input('b: '))
      c = int(input('c: '))
      print(solve_quadratic(a, b, c))

if __name__ == "__main__":
    main()
