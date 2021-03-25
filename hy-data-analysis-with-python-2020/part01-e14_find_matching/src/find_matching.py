#!/usr/bin/env python3

def find_matching(L, pattern):
    L_c = []
    L_c.extend(L)

    out = []

    for i, x in enumerate(L_c):
      if(pattern in x): out.append(i)

    return out

def main():
    print(find_matching(["sensitive", "engine", "rubbish", "comment"], "en"))

if __name__ == "__main__":
    main()
