#!/usr/bin/env python3
from functools import reduce

def sum_equation(L):
    if len(L) == 0: return "0 = 0"

    sum = reduce(lambda x, y: x + y, L, 0)
    showSum = reduce(lambda x, y: "{} + {}".format(x, y), L)
    return "{} = {}".format(showSum, sum)

def main():
    print(sum_equation([1,5,7]))

if __name__ == "__main__":
    main()
