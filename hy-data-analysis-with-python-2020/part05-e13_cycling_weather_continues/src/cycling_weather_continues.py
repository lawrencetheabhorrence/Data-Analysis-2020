#!/usr/bin/env python3
import pandas as pd
import numpy as np
from sklearn import linear_model

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
  df.index = pd.to_datetime(df[['Year', 'Month', 'Day']], format='%Y-%m-%d')
  df = df.drop(columns=['Year', 'Month', 'Day', 'Hour'])
  df = df['2017-01-01':'2017-12-31']
  df = df.groupby(by=df.index).sum()
  return df

def cycling_weather():
    cycling_data = cycling()
    weather = pd.read_csv('src/kumpula-weather-2017.csv')
    weather = weather.rename(columns={'m': 'Month', 'd': 'Day'})
    weather.index = pd.to_datetime(weather[['Year', 'Month', 'Day']], format='%Y-%m-%d')
    weather = weather.drop(columns=['Year', 'Month', 'Day', 'Time', 'Time zone'])
    merge = pd.merge(left=cycling_data, right=weather, left_index=True, right_index=True)
    return merge.fillna(method='ffill')


def cycling_weather_continues(station):
    df = cycling_weather()
    rain = df['Precipitation amount (mm)'].to_numpy()
    snow = df['Snow depth (cm)'].to_numpy()
    temp = df['Air temperature (degC)'].to_numpy()
    station = df[station].to_numpy()
    x = np.vstack([rain, snow, temp])
    model = linear_model.LinearRegression(fit_intercept=True)
    model.fit(x.T, station)
    score = model.score(x.T, station)
    return ((model.coef_[0], model.coef_[1], model.coef_[2]), score)

def main():
    station = 'Auroransilta'
    data = cycling_weather_continues(station)
    print(f'Measuring station: {station}')
    print(f"Regression coefficient for variable 'precipitation': {data[0][0]:.1f}")
    print(f"Regression coefficient for variable 'snow depth': {data[0][1]:.1f}")
    print(f"Regression coefficient for variable 'temperature': {data[0][2]:.1f}")
    print(f'Score: {data[1]:.2f}')

if __name__ == "__main__":
    main()
