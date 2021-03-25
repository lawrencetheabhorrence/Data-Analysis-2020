#!/usr/bin/env python3

def extract_numbers(s):
    out = []
    for x in s.split():
      try: out.append(int(x))
      except ValueError:
        try: out.append(float(x))
        except ValueError: continue
    return out

def main():
    print(extract_numbers("abd 123 1.2 test 13.2 -1"))

if __name__ == "__main__":
    main()
