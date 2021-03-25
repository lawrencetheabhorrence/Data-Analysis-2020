#!/usr/bin/env python3

import pandas as pd
import matplotlib.pyplot as plt

def split_date(df):
    df = df.dropna(axis=0, how='all').dropna(axis=1, how='all')
    date = df['Päivämäärä'].str.split(expand=True).rename({0: "Weekday", 1: "Day", 2: "Month", 3: "Year", 4: "Time"}, axis=1)
    date['Weekday'] = date['Weekday'].map({"ma": 1, "ti": 2, "ke": 3, "to": 4, "pe": 5, "la": 6, "su": 7})
    date['Month'] = date['Month'].map({"tammi": 1, "helmi": 2, "maalis": 3, "huhti": 4, "touko": 5, "kesä": 6, "heinä": 7, "elo": 8, "syys": 9, "loka": 10, "marras": 11, "joulu": 12}).astype(int, errors='ignore')
    return date


def split_date_continues():
    df = pd.read_csv('src/Helsingin_pyorailijamaarat.csv', sep=';')
    date = split_date(df)
    df = df.drop([ 'Unnamed: 21'], axis=1)
    df = pd.concat([date, df], axis=1)
    df = df.dropna(axis=0, how='all').dropna(axis=1, how='all')
    df['Päivämäärä'] = date['Year'].map(str) + ' ' +  date['Month'].map(str) + ' ' + date['Day'].map(str) + ' ' + date['Time'].map(str)
    print(df)
    return df


def bicycle_timeseries():
    df = split_date_continues()
    date = pd.to_datetime(df['Päivämäärä'], format="%Y-%m-%d %H:%M")
    print(date)
    df = df.drop(columns = ['Year', 'Month', 'Day', 'Time', 'Päivämäärä'])
    df = df.set_index(date)
    return df

def commute():
    df = bicycle_timeseries()
    df = df.loc['2017-08-01': '2017-08-31'].groupby(df['Weekday']).sum()
    df = df.drop(columns=['Weekday'])
    print(df)
    return df

def main():
    df = commute()
    print(df.values.sum())
    plt.plot(df)
    plt.xticks(df.index)
    plt.show()


if __name__ == "__main__":
    main()
