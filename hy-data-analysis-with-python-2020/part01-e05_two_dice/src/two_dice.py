#!/usr/bin/env python3

def main():
    for d1 in range(6):
      for d2 in range(6):
        if (d1 + d2 == 3): print('({}, {})'.format(d1 + 1, d2 + 1))

if __name__ == "__main__":
    main()
