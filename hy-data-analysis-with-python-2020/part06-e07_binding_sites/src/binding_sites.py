#!/usr/bin/env python3

import pandas as pd
import numpy as np
import scipy
from sklearn.cluster import AgglomerativeClustering
from sklearn.metrics import accuracy_score
from sklearn.metrics import pairwise_distances

from matplotlib import pyplot as plt

import seaborn as sns
sns.set(color_codes=True)
import scipy.spatial as sp
import scipy.cluster.hierarchy as hc

def toint(x):
    return {'A': 0, 'C': 1, 'G': 2, 'T': 3}[x]

def get_features_and_labels(filename):
    df = pd.read_csv(filename, sep="\t")
    X = df['X']
    features = []
    for chro in X:
        features.append([toint(c) for c in chro])
    return (np.array(features), df['y'].to_numpy())

# def plot(distances, method='average', affinity='euclidean'):
#     mylinkage = hc.linkage(sp.distance.squareform(distances), method=method)
#     g=sns.clustermap(distances, row_linkage=mylinkage, col_linkage=mylinkage )
#     g.fig.suptitle(f"Hierarchical clustering using {method} linkage and {affinity} affinity")
#     plt.show()

def find_permutation(n_clusters, real_labels, labels):
    permutation = []
    for i in range(n_clusters):
        idx = (labels == i)
        new_label = scipy.stats.mode(real_labels[idx])[0][0]
        permutation.append(new_label)

    return permutation

def cluster_euclidean(filename):
    features, labels = get_features_and_labels(filename)
    model = AgglomerativeClustering(n_clusters=2,
                                    affinity='euclidean',
                                    linkage='average')
    model.fit(features)
    permutation = find_permutation(2, labels, model.labels_)
    fixed_labels = [ permutation[label] for label in model.labels_ ]


    return accuracy_score(labels, fixed_labels)

def cluster_hamming(filename):
    features, labels = get_features_and_labels(filename)
    affinity = pairwise_distances(features, metric='hamming')
    model = AgglomerativeClustering(n_clusters=2,
                                    affinity='precomputed',
                                    linkage='average')
    model.fit(affinity)
    permutation = find_permutation(2, labels, model.labels_)
    fixed_labels = [ permutation[label] for label in model.labels_ ]

    return accuracy_score(labels, fixed_labels)

def main():
    print("Accuracy score with Euclidean affinity is", cluster_euclidean("src/data.seq"))
    print("Accuracy score with Hamming affinity is", cluster_hamming("src/data.seq"))

if __name__ == "__main__":
    main()
