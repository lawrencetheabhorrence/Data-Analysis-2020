#!/usr/bin/env python3


def main():
  for row in range(10):
    for col in range(10):
      print('{:4d}'.format((col + 1) * (row + 1)), end="")
    print()

if __name__ == "__main__":
    main()
