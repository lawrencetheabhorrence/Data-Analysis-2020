#!/usr/bin/env python3

import sys
from functools import reduce
import math

def sum(nums):
  return reduce(lambda x, y: x + y, nums, 0)

def avg(nums):
  return sum(nums) / len(nums)

def stddev(nums):
  numerator = reduce(lambda x, y: (y - avg(nums))*(y - avg(nums)) + x, nums, 0)
  return math.sqrt(numerator / (len(nums) - 1))

def summary(filename):
  nums = []
  with open(filename, 'r') as f:
    for line in f:
      try:
        nums.append(float(line))
      except ValueError:
        continue

  return (sum(nums), avg(nums), stddev(nums))

def main():
    filenames = sys.argv[1:]
    for f in filenames:
      s = summary(f)
      print(f'File: {f} Sum: {s[0]:.6f} Average: {s[1]:.6f} Stddev: {s[2]:.6f}')

if __name__ == "__main__":
    main()
