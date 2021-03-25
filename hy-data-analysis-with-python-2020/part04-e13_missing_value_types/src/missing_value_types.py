#!/usr/bin/env python3

import pandas as pd
import numpy as np

def missing_value_types():
    state = ['United Kingdom', 'Finland', 'USA', 'Sweden', 'Germany', 'Russia']
    year = [np.nan, 1917, 1776, 1523, np.nan,  1992]
    pres = [None, 'Niinistö', 'Trump', None, 'Steinmeiser', 'Putin']

    return pd.DataFrame({'Year of independence': year, 'President': pres}, index=state)

def main():
    print(missing_value_types())

if __name__ == "__main__":
    main()
