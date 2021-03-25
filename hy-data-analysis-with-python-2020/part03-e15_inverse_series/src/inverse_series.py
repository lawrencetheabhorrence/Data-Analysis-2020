#!/usr/bin/env python3

import pandas as pd

def inverse_series(s):
    val = s.index
    idx = s.values
    return pd.Series(val, index=idx)

def main():
    print(inverse_series(pd.Series(range(0, 5), index=list('abcde'))))

if __name__ == "__main__":
    main()
