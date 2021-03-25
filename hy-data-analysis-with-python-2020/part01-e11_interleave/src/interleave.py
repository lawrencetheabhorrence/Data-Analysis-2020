#!/usr/bin/env python3

def interleave(*lists):
    out = []
    for x in list(zip(*lists)):
      out.extend(x)
    return out

def main():
    print(interleave([1, 2, 3], [20, 30, 40], ['a', 'b', 'c']))

if __name__ == "__main__":
    main()
