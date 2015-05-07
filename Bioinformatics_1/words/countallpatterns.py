#!/usr/bin/env python -tt

import numpy
from patterncount import subtext
from freqwords import builddict

def patterntonumber(pattern):

  """
  Computes the index of an array for a pattern
  The pattern must comprise A, C, G, and T.
  The array represents all patterns of length len(pattern), sorted
  lexicographically.  Such an array has 4^len(pattern) indices.
  
  Inputs:
  pattern -- a pattern
  
  Output:
  index -- the index of the pattern in a lexicographically sorted array of all
  possible patterns with length len(pattern)
  """

  charactertonumber = {'A': '0', 'C': '1', 'G': '2', 'T': '3'}

  character = []

  for char in pattern:
    character.append(charactertonumber[char])
    
  base4num = ''.join(character)
  
  index = int(base4num, base = 4)
  
#  print base4num
#  print index
  
  return(index)

def countallpatterns(text, klength):

  """
  Counts the number of occurrences of a substring in a string
  
  Inputs:
  text -- a string
  klength -- the length of the substring
  
  Outputs:
  A tuple comprising:
  numallpatterns -- an array of length 4^'klength'. The array represents all
  substrings of length 'klength', sorted lexicographically. Each value is the
  number of occurrences in 'text' of the substring. For instance, if 'klength'
  is 2 numallpatterns[0] corresponds to 'AA' and its value is the number of
  times 'AA' appears in 'text'.
  substrpatterns -- an array of length 4^'klength'. When numallpatterns[i] is
  greater than 0 substrpatterns[i] is the substring.
  dictpattern -- a dictionary in which each key is a substring from 'text' of
  length 'klength'. The array for each key contains the indices in 'text' where
  the substring begins.
  
  This routine is the basis for a method different from that of freqwords.
  freqwords extracts a substring from 'text' and checks that each substring of
  the same length from 'text' matches the extracted substring.  countallpatterns
  creates an array corresponding to a lexicographic sort of all substrings of
  length 'klength' and adds 1 to the array value for each substring in 'text'.
  
  The python way to do this is to replace numallpatterns and substrpatterns with
  a dictionary. However we will need to do the reverse operation---converting an
  index to a pattern---in short order and the pythonic way of doing that skips
  an interesting algorithm.
  """

  dictpattern = {}

  numallpatterns = numpy.zeros(4.**klength)
  substrpatterns = numpy.zeros(4.**klength, dtype = numpy.dtype((str, klength)))

  for i in xrange(0, len(text) - klength + 1):

    substring = subtext(text, i, klength)
    insert_index = patterntonumber(substring)
    numallpatterns[insert_index] = numallpatterns[insert_index] + 1
    substrpatterns[insert_index] = substring
    dictpattern = builddict(dictpattern, substring, i)
    
  return(numallpatterns, substrpatterns, dictpattern)

def main():

  print countallpatterns('ACGCGGCTCTGAAA', 2)[0]
  print countallpatterns('ACGCGGCTCTGAAA', 2)[1]
  print countallpatterns('ACGCGGCTCTGAAA', 2)[2]
  
#  f = open('dataset_2994_5.txt', 'r')
  
#  genome = f.readline()
  
#  genome = genome.strip()
  
#  f.close()
  
#  numpy.savetxt('t', countallpatterns(genome, 8)[0], fmt = '%i', newline = ' ')

#  print patterntonumber('CTGTTTGCAGTGCACGCAA')

if __name__ == "__main__":
  main()