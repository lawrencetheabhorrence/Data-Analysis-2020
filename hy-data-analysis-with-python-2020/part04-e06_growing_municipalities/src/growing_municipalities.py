#!/usr/bin/env python3

import pandas as pd

def growing_municipalities(df):
    pop_c = df["Population change from the previous year, %"]
    pop_c_grow = pop_c[pop_c > 0]
    return pop_c_grow.size / pop_c.size

def main():
    df = pd.read_csv('src/municipal.tsv', sep='\t')
    df.index = df["Region 2018"]
    df.drop("Region 2018", axis=1)
    df = df["Akaa":"Äänekoski"]
    print(f'Proportion of growing municipalities: {growing_municipalities(df):.1%}')

if __name__ == "__main__":
    main()
