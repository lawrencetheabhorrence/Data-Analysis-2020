#!/usr/bin/env python3

def main():
    twoDice = ( f'({a}, {b})'  for a in range(1, 5)
                            for b in range(1, 5)
                            if a + b == 5)
    for x in twoDice:
      print(x)

if __name__ == "__main__":
    main()
