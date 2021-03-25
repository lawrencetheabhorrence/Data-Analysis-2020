#!/usr/bin/env python3

def reverse_dictionary(d):
    d_c = d.copy()
    out = []
    for x in d_c.values():
      for y in x: out.extend(x)
    out = set(out)
    out = dict.fromkeys(out, [])

    for key, val in d_c.items():
      new_val = []
      for x in val:
        new_val.extend(out[x])
        if not (key in out[x]): new_val.append(key)
        out.update({x: new_val})
        new_val = []

    return out


def main():
    print(reverse_dictionary({'move': ['liikuttaa'], 'hide': ['piilottaa', 'salata'], 'six': ['kuusi'], 'fir': ['kuusi']}))

if __name__ == "__main__":
    main()
