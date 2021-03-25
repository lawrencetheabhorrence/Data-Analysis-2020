#!/usr/bin/env python3

import pandas as pd

def split_date(df):
  df = df.dropna(axis=0, how='all').dropna(axis=1, how='all')
  date = df['Päivämäärä'].str.split(expand=True).rename({0: "Weekday", 1: "Day", 2: "Month", 3: "Year", 4: "Hour"}, axis=1)
  date['Weekday'] = date['Weekday'].map({"ma": "Mon", "ti": "Tue", "ke": "Wed", "to": "Thu", "pe": "Fri", "la": "Sat", "su": "Sun"})
  date['Month'] = date['Month'].map({"tammi": 1, "helmi": 2, "maalis": 3, "huhti": 4, "touko": 5, "kesä": 6, "heinä": 7, "elo": 8, "syys": 9, "loka": 10, "marras": 11, "joulu": 12}).astype(int, errors='ignore')
  date['Day'] = date['Day'].map(int)
  date['Year'] = date['Year'].map(int)
  date['Hour'] = date['Hour'].str.split(expand=True, pat=":")[0].rename("Hour").map(int)
  return date

def cycling():
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

def cycling_weather():
    cycling_data = cycling()
    weather = pd.read_csv('src/kumpula-weather-2017.csv')
    merge = pd.merge(cycling_data, weather, left_on=['Year', 'Month', 'Day'], right_on=['Year', 'm', 'd']).drop(['m', 'd', 'Time zone', 'Time'], axis=1)
    return merge

def main():
    print(cycling_weather())

if __name__ == "__main__":
    main()
