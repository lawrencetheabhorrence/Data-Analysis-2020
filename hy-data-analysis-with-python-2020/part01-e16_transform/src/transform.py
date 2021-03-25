#!/usr/bin/env python3

def transform(s1, s2):
    s1_c = list(map(int, s1.split()))
    s2_c = list(map(int, s2.split()))
    pairs = list(zip(s1_c, s2_c))
    return list(map(lambda x: x[0] * x[1], pairs))

def main():
    print(transform("1 5 3", "2 6 -1"))

if __name__ == "__main__":
    main()
