#!/usr/bin/env python3

def detect_ranges(L):
    L_copy = []
    for x in L: L_copy.append(x)
    L_copy.sort()

    holder = []
    out = []
    for x in L_copy:
      if (len(holder) == 0 or holder[len(holder) - 1] == x - 1): holder.append(x)
      else:
        if len(holder) == 1: out.append(holder[0])
        if len(holder) > 1: out.append((holder[0], holder[len(holder) - 1] + 1))
        holder = [x]

    if not len(holder) == 0:
      if len(holder) == 1: out.append(holder[0])
      else: out.append((holder[0], holder[len(holder) - 1] + 1))

    return out

def main():
    L = [2, 5, 4, 8, 12, 6, 7, 10, 13]
    result = detect_ranges(L)
    print(L)
    print(result)

if __name__ == "__main__":
    main()
