#!/usr/bin/env python3

import pandas as pd

def suicide_fractions():
    df = pd.read_csv('src/who_suicide_statistics.csv', sep=',')
    df['means'] = df['suicides_no'] / df['population']
    countries = df.groupby('country')
    means = countries['means'].mean()
    return means

def suicide_weather():
    ser = pd.read_html('src/List_of_countries_by_average_yearly_temperature.html', index_col=0, header=0)
    ser = pd.concat(ser)
    temps = ser['Average yearly temperature (1961–1990, degrees Celsius)'].str.replace('\u2212', '-').map(float)
    suicides = suicide_fractions()
    corr = suicides.corr(temps, method='spearman')
    return (suicides.size, temps.size, pd.merge(temps, suicides, left_index=True, right_index=True).size // 2, corr)

def main():
    suicides, temps, common, corr = suicide_weather()
    print(f'Suicide DataFrame has {suicides} rows')
    print(f'Temperature DataFrame has {temps} rows')
    print(f'Common DataFrame has {common} rows')
    print(f'Spearman correlation: {corr:.1f}')

if __name__ == "__main__":
    main()
