#!/usr/bin/env python3
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA

def explained_variance():
    df = pd.read_csv('src/data.tsv', sep='\t')
    X = df.to_numpy(dtype=float)
    print(X.shape)
    model = PCA()
    model.fit(X)
    return np.var(X, axis=0), model.explained_variance_

def main():
    v, ev = explained_variance()
    print('The variances are:', *list(map(lambda x: f'{0:.3f}'.format(x), v)))
    print('The explained variances after PCA are:' , *list(map(lambda x:
                                                               f'{0:.3f}'.format(x),
                                                               ev)))
    plt.plot(np.arange(1, 11), np.cumsum(ev))
    plt.show()
    #print(sum(v), sum(ev))

if __name__ == "__main__":
    main()
