#!/usr/bin/env python3

import pandas as pd

def read_series():
    vals = []
    idx = []
    while True:
      s = input()
      if s == '' or s == '\n': break
      s = s.split()
      if not len(s) == 2: raise ValueError('malformatted input')
      vals.append(s[1])
      idx.append(s[0])

    return pd.Series(vals, index=idx)


def main():
    read_series()

if __name__ == "__main__":
    main()
