#!/usr/bin/env python3

import pandas as pd

def best_record_company():
    df = pd.read_csv('src/UK-top40-1964-1-2.tsv', sep='\t')
    pubs = df.groupby('Publisher')
    best = pubs['WoC'].sum().max()
    return pubs.filter(lambda df: df['WoC'].sum().max() == best)

def main():
    print(best_record_company())
    

if __name__ == "__main__":
    main()
