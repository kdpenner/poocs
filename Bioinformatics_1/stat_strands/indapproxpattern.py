#!/usr/bin/env python -tt

from words import patterncount
from hammingdist import hammingdist

def indapproxpattern(pattern, string, nummismatch):

  """
  Find the indices of an altered pattern in string
  
  The number of alterations must be less than or equal to nummismatch
  """

  indarr = []
#  substringarr = []
  numchars = len(pattern)

  for i in xrange(0, len(string) - numchars + 1):
  
    substring = patterncount.subtext(string, i, numchars)
    
    if hammingdist(pattern, substring) <= nummismatch:
    
      indarr.append(i)
#      substringarr.append(substring)
      
  return indarr
  
def main():

  print len(indapproxpattern('AAAAA', 'AACAAGCTGATAAACATTTAAAGAG', 2))
  
  print len(indapproxpattern('GAGG', 'TTTAGAGCCTTCAGAGG', 2))

  print len(indapproxpattern('AAA', 'GGGGGGGG', 1))
  
  print indapproxpattern('GAGG', 'TTTAGAGCCTTCAGAGG', 2)

if __name__ == "__main__":
  main()
