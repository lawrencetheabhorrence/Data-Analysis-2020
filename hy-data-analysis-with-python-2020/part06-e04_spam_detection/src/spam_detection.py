#!/usr/bin/env python3
import gzip
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split

def spam_detection(random_state=0, fraction=1.0):
    ham, spam = gzip.open('src/ham.txt.gz').read(), gzip.open('src/spam.txt.gz').read()
    ham_data, spam_data = []
    for x in range(0, int(len(ham) * fraction)):
        ham_data.append(x)
    for x in range(0, int(len(spam)*fraction)):
        spam_data.append(x)

    features = CountVectorizer.fit_transform(ham_data, spam_data)
    X_train, X_test, y_train, y_test = train_test_split(features)
    return 0.0, 0, 0

def main():
    accuracy, total, misclassified = spam_detection()
    print("Accuracy score:", accuracy)
    print(f"{misclassified} messages miclassified out of {total}")

if __name__ == "__main__":
    main()
