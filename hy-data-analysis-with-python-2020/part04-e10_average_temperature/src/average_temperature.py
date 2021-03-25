#!/usr/bin/env python3

import pandas as pd

def average_temperature():
    df = pd.read_csv('src/kumpula-weather-2017.csv')
    df.index = df.m
    temp_j = df.loc[7, 'Air temperature (degC)']
    return temp_j.mean()

def main():
    print(f'Average temperature in July: {average_temperature():.1f}')

if __name__ == "__main__":
    main()
