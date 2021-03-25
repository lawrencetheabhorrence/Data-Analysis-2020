#!/usr/bin/env python3

import pandas as pd

def swedish_and_foreigners():
    df = pd.read_csv('src/municipal.tsv', sep='\t')
    df.index = df["Region 2018"]
    df.drop("Region 2018", axis=1)
    df = df["Akaa":"Äänekoski"]
    swf = df[(df["Share of Swedish-speakers of the population, %"] > 5) & (df["Share of foreign citizens of the population, %"] > 5)]
    return swf[["Population", "Share of Swedish-speakers of the population, %", "Share of foreign citizens of the population, %"]]

def main():
    print(swedish_and_foreigners())

if __name__ == "__main__":
    main()
