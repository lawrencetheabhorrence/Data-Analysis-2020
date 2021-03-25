#!/usr/bin/env python3

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def split_date(df):
    df = df.dropna(axis=0, how='all').dropna(axis=1, how='all')
    date = df['Päivämäärä'].str.split(expand=True).rename({0: "Weekday", 1: "Day", 2: "Month", 3: "Year", 4: "Hour"}, axis=1)
    date['Weekday'] = date['Weekday'].map({"ma": "Mon", "ti": "Tue", "ke": "Wed", "to": "Thu", "pe": "Fri", "la": "Sat", "su": "Sun"})
    date['Month'] = date['Month'].map({"tammi": 1, "helmi": 2, "maalis": 3, "huhti": 4, "touko": 5, "kesä": 6, "heinä": 7, "elo": 8, "syys": 9, "loka": 10, "marras": 11, "joulu": 12}).astype(int, errors='ignore')
    date['Hour'] = date['Hour'].str.split(expand=True, pat=":")[0].rename("Hour")
    return date


def split_date_continues():
    df = pd.read_csv('src/Helsingin_pyorailijamaarat.csv', sep=';')
    date = split_date(df)
    df = df.drop(['Päivämäärä', 'Unnamed: 21'], axis=1)
    df = pd.concat([date, df], axis=1)
    df = df.dropna(axis=0, how='all').dropna(axis=1, how='all')
    df['Month'] = df['Month'].map(int)
    df['Day'] = df['Day'].map(int)
    df['Year'] = df['Year'].map(int)
    df['Hour'] = df['Hour'].map(int)
    return df


def cyclists_per_day():
    cyclists = split_date_continues().drop(['Hour', 'Weekday'], axis=1)
    days = cyclists.groupby(['Year', 'Month', 'Day']).sum()
    return days

def main():
    daily = cyclists_per_day()
    aug_eight = daily.loc[2017, 8]
    plt.plot(aug_eight)
    plt.xticks(np.arange(1, 32))
    plt.show()

if __name__ == "__main__":
    main()
