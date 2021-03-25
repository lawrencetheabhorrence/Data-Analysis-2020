#!/usr/bin/env python3

import pandas as pd

def create_series(L1, L2):
    if not len(L1) == 3 or not len(L2) == 3: raise ValueError('Lists must have a length of 3!')
    return (pd.Series(L1, index=list('abc')), pd.Series(L2, index=list('abc')))

def modify_series(s1, s2):
    s1['d'] = s2['b']
    del s2['b']
    return (s1, s2)

def main():
    s1, s2 = create_series(range(0, 3), range(4, 7))
    print(s1, s2, sep='\n')
    z1, z2 = modify_series(s1, s2)
    print(z1, z2, sep='\n')
    print(z1 + z2)

if __name__ == "__main__":
    main()
