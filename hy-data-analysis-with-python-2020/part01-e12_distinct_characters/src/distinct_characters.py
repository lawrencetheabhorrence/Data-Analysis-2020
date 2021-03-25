#!/usr/bin/env python3

def distinct_characters(L):
    out = []
    L_c = []
    L_c.extend(L)

    for s in L_c:
      out.append((s, len(set(s))))

    return dict(out)

def main():
    print(distinct_characters(["check", "look", "try", "pop"]))

if __name__ == "__main__":
    main()
