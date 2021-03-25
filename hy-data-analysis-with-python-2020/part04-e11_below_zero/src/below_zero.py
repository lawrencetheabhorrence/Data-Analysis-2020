#!/usr/bin/env python3

import pandas as pd

def below_zero():
    df = pd.read_csv('src/kumpula-weather-2017.csv')
    temp = df['Air temperature (degC)']
    temp = temp[temp < 0]
    return temp.count()

def main():
    print(f'Number of days below zero: {below_zero()}')

if __name__ == "__main__":
    main()
