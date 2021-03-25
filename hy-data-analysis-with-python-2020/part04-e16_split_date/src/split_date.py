#!/usr/bin/env python3

import pandas as pd
import numpy as np


def split_date():
    # cleaning the data by dropping empty values
    df = pd.read_csv('src/Helsingin_pyorailijamaarat.csv', sep=';')
    df = df.dropna(axis=0, how='all').dropna(axis=1, how='all')
    date = df['Päivämäärä'].str.split(expand=True).rename({0: "Weekday", 1: "Day", 2: "Month", 3: "Year", 4: "Hour"}, axis=1)
    date['Weekday'] = date['Weekday'].map({"ma": "Mon", "ti": "Tue", "ke": "Wed", "to": "Thu", "pe": "Fri", "la": "Sat", "su": "Sun"})
    date['Month'] = date['Month'].map({"tammi": 1, "helmi": 2, "maalis": 3, "huhti": 4, "touko": 5, "kesä": 6, "heinä": 7, "elo": 8, "syys": 9, "loka": 10, "marras": 11, "joulu": 12}).astype(int, errors='ignore')
    date['Day'] = date['Day'].map(int)
    date['Year'] = date['Year'].map(int)
    date['Hour'] = date['Hour'].str.split(expand=True, pat=":")[0].rename("Hour").map(int)
    # df = date.join(df.drop('Päivämäärä', axis=1), sort=False)
    return date

def main():
    print(split_date(), int("00"))

if __name__ == "__main__":
    main()
