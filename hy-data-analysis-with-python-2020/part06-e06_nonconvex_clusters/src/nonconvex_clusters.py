#!/usr/bin/env python3

import pandas as pd
import numpy as np
import scipy
from sklearn.cluster import DBSCAN
from sklearn.metrics import accuracy_score


def find_permutation(n_clusters, real_labels, labels):
    permutation = []
    for i in range(n_clusters):
        idx = (labels == i)
        new_label = scipy.stats.mode(real_labels[idx])[0][0]
        permutation.append(new_label)
    return permutation


def nonconvex_clusters():
    df = pd.read_csv('src/data.tsv', sep='\t')
    X = df[['X1', 'X2']]
    y = df['y']
    results = []
    for eps in np.arange(0.05, 0.2, 0.05):
        model = DBSCAN(eps)
        model.fit(X)
        outliers = (model.labels_ == -1)
        n_clusters = max(model.labels_) + 1
        if n_clusters == len(y.unique()):
            permutation = find_permutation(n_clusters, y[~outliers],
                                           model.labels_[~outliers])
            fixed_labels = [permutation[label] for label in
                            model.labels_[~outliers]]
            acc = accuracy_score(y[~outliers], fixed_labels)
        else:
            acc = np.nan
        results.append([eps, acc, n_clusters, len(model.labels_[outliers])])
    return pd.DataFrame(data=results, columns=['eps', 'Score', 'Clusters',
                                               'Outliers'], dtype='float')


def main():
    print(nonconvex_clusters())


if __name__ == "__main__":
    main()
