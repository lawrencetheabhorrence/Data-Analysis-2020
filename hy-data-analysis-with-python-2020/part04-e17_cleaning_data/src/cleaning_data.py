#!/usr/bin/env python3

import pandas as pd
import numpy as np


def cleaning_data():
    df = pd.read_csv('src/presidents.tsv', sep='\t')
    df.Seasons = df.Seasons.replace('two', 2).map(int)
    df.Last = df.Last.replace('-', np.nan).map(float)
    df.Start = df.Start.replace('2017 Jan', 2017).map(int)
    df.President = df.President.str.replace('Bush, George', 'George Bush')
    df.President = df.President.str.replace('Clinton, Bill', 'Bill Clinton')
    df['Vice-president'] = df['Vice-president'].str.replace('Cheney, dick', 'Dick Cheney').astype(object)
    df['Vice-president'] = df['Vice-president'].str.replace('gore, Al', 'Al Gore').str.title().astype(object)
    return df

def main():
    cleaning_data()

if __name__ == "__main__":
    main()
