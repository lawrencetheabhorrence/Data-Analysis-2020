#!/usr/bin/env python3

def merge(L1, L2):
  out = []
  list1 = []
  list2 = []

  for x in L1: list1.append(x)
  for x in L2: list2.append(x)

  for x in list1:
    if not (len(list2) == 0):
      i = 0
      while(i < len(list2)):
        if (list2[i] <= x):
          out.append(list2[i])
          list2.pop(i)
          continue
        i = i + 1
    out.append(x)

  if not (len(list2) == 0):
    for x in list2: out.append(x)

  return out

def main():
  l1 = [-99, -96, -96, -64, -52, -33, -16, -6, -4, -3, 8, 26, 31, 32, 48, 59, 79, 81, 92, 97]
  l2 = [-88, -2, 21, 21, 26, 38, 55, 57, 84, 98]
  print(merge(l1, l2))

if __name__ == "__main__":
    main()
