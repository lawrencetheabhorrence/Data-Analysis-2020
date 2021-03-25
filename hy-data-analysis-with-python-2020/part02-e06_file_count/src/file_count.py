#!/usr/bin/env python3

import sys

def file_count(filename):
    counts = {'lines': 0, 'words': 0, 'chars': 0}
    with open(filename, 'r') as f:
      for line in f:
        counts['lines'] += 1
        counts['words'] += len(line.split())
        counts['chars'] += len(line)
    return (counts['lines'], counts['words'], counts['chars'])


def main():
    for f in sys.argv[1:]:
      counts = file_count(f)
      print(f'{counts[0]}\t{counts[1]}\t{counts[2]}\t{f}')

if __name__ == "__main__":
    main()
