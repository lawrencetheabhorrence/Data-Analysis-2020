#!/usr/bin/env python3

def countwords(words, key):
  count = len(list(filter(lambda w: w == key, words)))
  return (key, count)

def getcounts(words):
  unique_words = list(set(words))

  tuples = list(map(lambda w: countwords(words, w), unique_words))
  dict_words = dict(tuples)
  return dict_words

def word_frequencies(filename):
    f = open(filename, 'r')
    words = ' '.join(f.readlines()).split()
    words = list(map(lambda w: w.strip("""!"#$%&'()*,-./:;?@[]_"""), words)) # remove punctuation
    return getcounts(words)


def format_frequencies(wordcounts):
  out = ''
  for word,count in wordcounts.items():
    out += f'{word}\t{count}\n'

  return out

def main():
    print(format_frequencies(word_frequencies('src/alice.txt')))

if __name__ == "__main__":
    main()
