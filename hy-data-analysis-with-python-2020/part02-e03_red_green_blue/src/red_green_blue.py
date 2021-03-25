#!/usr/bin/env python3

import re

def getinfo(line):
  rgb = re.findall(r'\b\d+\b', line)
  colorname = ' '.join(re.findall(r'\b[a-zA-Z]+\b', line))
  rgb.append(colorname)
  return '\t'.join(rgb)

def red_green_blue(filename="src/rgb.txt"):
    f = open(filename, 'r')
    lines = f.readlines()
    lines = lines[1:]
    return list(map(getinfo, lines))


def main():
    print(red_green_blue("part02-e03_red_green_blue/src/rgb.txt"))

if __name__ == "__main__":
    main()
