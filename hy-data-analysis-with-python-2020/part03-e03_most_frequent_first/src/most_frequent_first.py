#!/usr/bin/env python3

import numpy as np

def most_frequent_first(a, c):
    a_c = a[:, :] # copies the array
    column = a_c[:, c]

    counts = np.unique(column, return_counts = True) # returns unique elems and count of elems as separate array

    counts = np.stack((counts[0], counts[1]), axis = 1) # join the two arrays into a 2d array
    print(counts)
    counts_sorted_i = np.argsort(counts[:, 1], axis = 0) # find the indexes of the sorted counts
    counts_sorted_i = np.flip(counts_sorted_i)
    print(counts_sorted_i)

    aux = np.zeros((len(counts), len(counts[0])), dtype = int)
    for x in counts_sorted_i:
      aux[x][0], aux[x][1] = counts[counts_sorted_i[x]]
    counts = aux

    print(counts)

    parts = []
    for n in range(0, len(counts)):
      parts.append(np.full((counts[n][1], 1), fill_value=counts[n][0])) # create arrays based on the frequency

    parts = np.concatenate(tuple(parts))
    parts = parts.reshape(1, len(parts))
    a_c[:, c] = parts
    return a_c

def main():
    a = np.array([[5, 0, 3, 3, 7, 9, 3, 5, 2, 4],
        [7, 6, 8, 8, 1, 6, 7, 7, 8, 1],
        [5, 9, 8, 9, 4, 3, 0, 3, 5, 0],
        [2, 3, 8, 1, 3, 3, 3, 7, 0, 1],
        [9, 9, 0, 4, 7, 3, 2, 7, 2, 0]])
    print(most_frequent_first(a, -1))

if __name__ == "__main__":
    main()
