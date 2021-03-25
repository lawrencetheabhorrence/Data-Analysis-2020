#!/usr/bin/env python3

from collections import Counter
import urllib.request
from lxml import etree

import numpy as np

from sklearn.naive_bayes import MultinomialNB
from sklearn.model_selection import cross_val_score
from sklearn import model_selection
from sklearn.feature_extraction.text import CountVectorizer

alphabet="abcdefghijklmnopqrstuvwxyzäö-"
alphabet_set = set(alphabet)

# Returns a list of Finnish words
def load_finnish():
    finnish_url="https://www.cs.helsinki.fi/u/jttoivon/dap/data/kotus-sanalista_v1/kotus-sanalista_v1.xml"
    filename="src/kotus-sanalista_v1.xml"
    load_from_net=False
    if load_from_net:
        with urllib.request.urlopen(finnish_url) as data:
            lines=[]
            for line in data:
                lines.append(line.decode('utf-8'))
        doc="".join(lines)
    else:
        with open(filename, "rb") as data:
            doc=data.read()
    tree = etree.XML(doc)
    s_elements = tree.xpath('/kotus-sanalista/st/s')
    return list(map(lambda s: s.text, s_elements))

def load_english():
    with open("src/words", encoding="utf-8") as data:
        lines=map(lambda s: s.rstrip(), data.readlines())
    return lines

def get_features(a):
    features = np.zeros((len(a), len(alphabet)))
    for i, w in enumerate(a):
        counts = Counter(w)
        for j, l in enumerate(alphabet):
            features[i, j] = counts[l]

    return features

def contains_valid_chars(s):
    x = set(s)
    return x.issubset(alphabet)


def get_features_and_labels():
    f = load_finnish()
    f = np.array(list(filter(contains_valid_chars, map(lambda s: s.lower(), f))))
    e = load_english()
    e = np.array(list(filter(contains_valid_chars, map(lambda s: s.lower(), filter(lambda s: s[0].islower(), e)))))

    X = np.vstack((get_features(f), get_features(e)))

    y = np.hstack(([0]*len(f), [1]*len(e)))

    return (X, y)


def word_classification():
    X, y = get_features_and_labels()
    model = MultinomialNB()
    model.fit(X, y)
    score = cross_val_score(model, X, y, cv = model_selection.KFold(n_splits=5, shuffle=True, random_state=0))
    return score


def main():
    print(get_features(load_finnish()).shape, len(load_finnish()))
    print("Accuracy scores are:", word_classification())

if __name__ == "__main__":
    main()
