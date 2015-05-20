#!/usr/bin/env python -tt

import patterncount

def builddict(dict, pattern, value_to_insert):

  """
  Builds a dictionary
  
  Inputs:
  dict -- a dictionary. Can be empty, can have data
  pattern -- the key
  value_to_insert -- the value to append for the 'pattern' key
  
  Output:
  dict
  """

  if dict.get(pattern):

    dict[pattern].append(value_to_insert)

  else:

    dict[pattern] = list([value_to_insert])
    
  return(dict)

def freqwords(string, klength):
  
  """
  Finds the most numerous substrings of a string
  
  Inputs:
  string -- a string
  klength -- the length of the substring
  
  Output:
  A dictionary containing the most numerous substrings of length 'klength' of
  'string'.  The values in the dictionary are the indices in 'string' where
  the substrings begin.
  
  This routine uses a naive method.  It extracts from 'string' a substring of
  length 'klength' and then proceeds to find the number of occurrences of the
  substring in 'string' by traversing 'string' character by character. It
  extracts the next substring by advancing one character.
  
  The number of occurrences are stored, the maximum number of occurrences found,
  and a dictionary is built.
  
  Example:
  see the examples in main()
  """
  
  freqpatterns = {}
  allpatterns = []
  num_occur = []
  
  for i in xrange(0, len(string) - klength + 1):
  
    allpatterns.append(patterncount.subtext(string, i, klength))
    
    num_occur.append(patterncount.patterncount(string, allpatterns[i]))

#  print allpatterns
#  print num_occur

  max_num_occur = max(num_occur)
  
  for j in xrange(0, len(string) - klength + 1):
  
    if num_occur[j] == max_num_occur:
    
#      print freqpatterns, allpatterns[j], j

      freqpatterns = builddict(freqpatterns, allpatterns[j], j)

#  print freqpatterns
  
  return(freqpatterns)

def main():

  print freqwords('ACAACTATGCATACTATCGGGAACTATCCT', 5)
  
  print freqwords('CGATATATCCATAG', 3)
  
  print freqwords('ACTGACTCCCACCCC', 3)
  
  print freqwords('ACGTTGCATGTCGCATGATGCATGAGAGCT', 4)
  
if __name__ == "__main__":
  main()