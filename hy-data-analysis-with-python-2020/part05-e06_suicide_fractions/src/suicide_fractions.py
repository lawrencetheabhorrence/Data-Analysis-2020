#!/usr/bin/env python3

import pandas as pd

def suicide_fractions():
    df = pd.read_csv('src/who_suicide_statistics.csv', sep=',')
    df['means'] = df['suicides_no'] / df['population']
    countries = df.groupby('country')
    return countries['means'].mean()

def main():
    print(suicide_fractions())

if __name__ == "__main__":
    main()
