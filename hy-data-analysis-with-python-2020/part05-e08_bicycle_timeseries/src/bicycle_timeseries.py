#!/usr/bin/env python3

import pandas as pd

def split_date(df):
    df = df.dropna(axis=0, how='all').dropna(axis=1, how='all')
    date = df['Päivämäärä'].str.split(expand=True).rename({0: "Weekday", 1: "Day", 2: "Month", 3: "Year", 4: "Time"}, axis=1)
    date['Weekday'] = date['Weekday'].map({"ma": "Mon", "ti": "Tue", "ke": "Wed", "to": "Thu", "pe": "Fri", "la": "Sat", "su": "Sun"})
    date['Month'] = date['Month'].map({"tammi": 1, "helmi": 2, "maalis": 3, "huhti": 4, "touko": 5, "kesä": 6, "heinä": 7, "elo": 8, "syys": 9, "loka": 10, "marras": 11, "joulu": 12}).astype(int, errors='ignore')
    return date


def split_date_continues():
    df = pd.read_csv('src/Helsingin_pyorailijamaarat.csv', sep=';')
    date = split_date(df)
    df = df.drop([ 'Unnamed: 21'], axis=1)
    df = pd.concat([date, df], axis=1)
    df = df.dropna(axis=0, how='all').dropna(axis=1, how='all')
    df['Päivämäärä'] = date['Year'].map(str) + ' ' +  date['Month'].map(str) + ' ' + date['Day'].map(str) + ' ' + date['Time'].map(str)
    return df


def bicycle_timeseries():
    df = split_date_continues()
    date = pd.to_datetime(df['Päivämäärä'], format="%Y-%m-%d %H:%M")
    df = df.drop(columns = ['Year', 'Month', 'Day', 'Weekday', 'Time', 'Päivämäärä'])
    df = df.set_index(date)
    return df
    


def main():
    print(bicycle_timeseries())

if __name__ == "__main__":
    main()
