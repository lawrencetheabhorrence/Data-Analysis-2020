#!/usr/bin/env python3
import re

def getextension(fname):
  if '.' not in fname: return None
  return fname.split('.')[-1].strip('\n')

def getfileswithext(files, ext):
  return [file.strip('\n') for file in files if ext == getextension(file)]

def file_extensions(filename):
    f = open(filename, 'r')
    fnames = f.readlines()
    exts = list(set(map(getextension, fnames)))

    out = [(ext, getfileswithext(fnames, ext)) for ext in exts if not ext == None]
    nones = [fname.strip('\n') for fname in fnames if getextension(fname) == None]

    return (nones, dict(out))

def main():
    fcounts = file_extensions('src/filenames.txt')
    print(f'{len(fcounts[0])} files with no extension')
    for ext, files in fcounts[1].items(): print(f'{ext} {len(files)}')

if __name__ == "__main__":
    main()
