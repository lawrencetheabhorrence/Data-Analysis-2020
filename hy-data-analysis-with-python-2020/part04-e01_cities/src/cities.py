#!/usr/bin/env python3

import pandas as pd

def cities():
    c1 = pd.Series([643272, 279044, 231853, 223027, 201810], index=['Helsinki', 'Espoo', 'Tampere', 'Vantaa', 'Oulu'])
    c2 = pd.Series([715.48, 528.03, 689.59, 240.35, 3817.52], index=['Helsinki', 'Espoo', 'Tampere', 'Vantaa', 'Oulu'])
    return pd.DataFrame({ 'Population': c1, 'Total area': c2 })

def main():
    print(cities())

if __name__ == "__main__":
    main()
