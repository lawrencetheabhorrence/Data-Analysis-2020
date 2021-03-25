#!/usr/bin/env python3

import pandas as pd

def municipalities_of_finland():
    df = pd.read_csv('src/municipal.tsv', sep='\t')
    print(df)
    df.index = df["Region 2018"]
    df=df[["Population", "Population change from the previous year, %", "Share of Swedish-speakers of the population, %", "Share of foreign citizens of the population, %", "Proportion of the unemployed among the labour force, %", "Proportion of pensioners of the population, %"]]
    return df["Akaa":"Äänekoski"]

def main():
    print(municipalities_of_finland())

if __name__ == "__main__":
    main()
