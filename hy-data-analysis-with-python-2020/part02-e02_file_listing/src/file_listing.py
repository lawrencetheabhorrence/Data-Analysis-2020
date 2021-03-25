#!/usr/bin/env python3

import re

def get_info(line):
  line = re.sub(r"^((-)?.* \d jttoivon hyad-all)", "", line).strip() # strips string to leave only filesize, date, time, and filename
  line = line.split() # splits into fields

  date = int(line[0])
  month = line[1]
  day = int(line[2])

  time = line[3].split(':')
  hours = int(time[0])
  minutes = int(time[1])

  filename = line[4]

  return (date, month, day, hours, minutes, filename)


def file_listing(filename="src/listing.txt"):
    f = open(filename, 'r')
    lines = f.readlines()
    return list(map(get_info, lines))

def main():
    line = "-rw------- 1 jttoivon hyad-all 1207075 Nov 28 16:02 face.png"
    print(file_listing())

if __name__ == "__main__":
    main()
