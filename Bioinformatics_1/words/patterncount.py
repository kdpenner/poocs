#!/usr/bin/env python -tt

def subtext(text, start, num_characters):

  """
  Extracts a continuous substring from a string
  
  Inputs:
  text -- a string
  start -- the starting index in 'text' of the extraction
  num_characters -- the length of the extraction
  
  Output:
  The substring
  
  Example:
  subtext('ABCD', 1, 2) returns 'BC'
  """

#  print text[start:start+num_characters]

  return(text[start:start+num_characters])

def patterncount(text, pattern):

  """
  Counts the number of times a given pattern is found in a string
  
  Inputs:
  text -- a string
  pattern -- the given pattern
  
  Output:
  The count
  
  This routine uses a naive method. It extracts from 'text' a substring of
  length len(pattern); compares the substring to 'pattern'; and adds 1 to a
  counter if the two match. It advances through 'text' character by character.
  
  Example:
  see the examples in main()
  """

  count = 0
  
  for i in xrange(0, len(text) - len(pattern) + 1):
    
    if subtext(text, i, len(pattern)) == pattern:
    
      count += 1
      
  return(count)
  
def main():

  print patterncount('ACAACTATGCATACTATCGGGAACTATCCT', 'ACTAT')
  
  print patterncount('CGATATATCCATAG', 'ATA')
  
  print patterncount('GCGCG', 'GCG')

if __name__ == "__main__":
  main()