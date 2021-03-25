#!/usr/bin/env python3

def triple(n): return 3 * n

def square(n): return n * n

def main():
    for x in range(10):
      sq = square(x + 1)
      tr = triple(x + 1)
      if (sq > tr): break
      print('triple({0})=={1} square({0})=={2}'.format(x + 1, tr, sq))

if __name__ == "__main__":
    main()
