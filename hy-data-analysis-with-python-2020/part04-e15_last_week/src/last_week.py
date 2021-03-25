#!/usr/bin/env python3

import pandas as pd
import numpy as np

def last_week():
    df = pd.read_csv('src/UK-top40-1964-1-2.tsv', sep='\t')
    df = df[~((df['LW'] == 'New') | (df['LW'] == 'Re'))]
    df['LW'] = pd.to_numeric(df['LW'])
    df.loc[(df['Pos'] == df['Peak Pos']) & (df['Pos'] < df['LW']), 'Peak Pos'] = np.nan
    df['Pos'] = df['LW']
    df['LW'] = np.nan
    df = df.sort_values(by=['Pos'])
    df['WoC'] = df['WoC'] - 1
    df = df.drop_duplicates(subset=['Pos'])
    top = pd.DataFrame({'Pos': np.arange(1, 41)}, columns=['Pos', 'LW', 'Title', 'Artist', 'Publisher', 'Peak Pos', 'WoC'])
    df = top.append(df).sort_values(by=['Title']).drop_duplicates(subset=['Pos']).sort_values(by=['Pos'])
    return df

def main():
    df = last_week()
    print("Shape: {}, {}".format(*df.shape))
    print("dtypes:", df.dtypes)
    print(df)


if __name__ == "__main__":
    main()
