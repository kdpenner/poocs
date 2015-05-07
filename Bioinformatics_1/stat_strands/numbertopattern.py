#!/usr/bin/env python -tt

def numbertopattern1(index, klength):

  """
  Computes the pattern for an index of an array
  The array represents all patterns of length 'klength', sorted
  lexicographically.  Such an array has 4^'klength' indices.  This routine does
  the reverse of patterntonumber (which is in countallpatterns).
  
  Inputs:
  index -- an index
  klength -- the length of the array for which index is valid
  
  Output:
  The pattern
  
  (This version calls itself and confuses me. The version that I understand at
  a glance is numbertopattern2.)
  """


  numbertocharacter = {0: 'A', 1: 'C', 2: 'G', 3: 'T'}
  
  if klength == 1:
  
    return numbertocharacter[index]
    
  prefixindex = index/4
  
  remainder = index % 4

#  print prefixindex
#  print remainder
#  print numbertocharacter[remainder]

  prefixpattern = numbertopattern1(prefixindex, klength - 1)
  
  symbol = numbertocharacter[remainder]
  
  build = prefixpattern+symbol
  
  return(build)
  
def numbertopattern2(index, klength):

  """
  Computes the pattern for an index of an array
  The array represents all patterns of length 'klength', sorted
  lexicographically.  Such an array has 4^'klength' indices.  This routine does
  the reverse of patterntonumber (which is in countallpatterns).
  
  Inputs:
  index -- an index
  klength -- the length of the array for which index is valid
  
  Output:
  The pattern
  
  (I understand this version at a glance.)
  """


  numbertocharacter = {0: 'A', 1: 'C', 2: 'G', 3: 'T'}
  
  pattern = ''
  
  for i in xrange(0, klength):
  
    prefixindex = index/4
    remainder = index % 4
    
    pattern = numbertocharacter[remainder] + pattern
    
    index = prefixindex
    
  return(pattern)

def main():

  print numbertopattern1(45, 4)
  print numbertopattern2(45, 4)

  print numbertopattern1(5408, 9)
  print numbertopattern2(5408, 9)


if __name__ == "__main__":
  main()
