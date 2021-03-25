#!/usr/bin/env python3

import pandas as pd
import numpy as np

def special_missing_values():
    df = pd.read_csv('src/UK-top40-1964-1-2.tsv', sep = '\t')
    df.index = df['LW']
    df.loc['New', 'LW'], df.loc['Re', 'LW'] = None, None
    df = df.dropna()
    df['LW'] = pd.to_numeric(df['LW'], errors="coerce")
    return df[df['LW'] < df['Pos']]

def main():
    print(special_missing_values())

if __name__ == "__main__":
    main()
