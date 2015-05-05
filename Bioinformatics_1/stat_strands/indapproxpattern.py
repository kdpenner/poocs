#!/usr/bin/env python -tt

from ..words import patterncount
from hammingdist import hammingdist

def indapproxpattern(pattern, string, nummismatch):

  indarr = []
  numchars = len(pattern)

  for i in xrange(0, len(string) - numchars + 1):
  
    substring = patterncount.subtext(string, i, numchars)
    
    if hammingdist(pattern, substring) <= nummismatch:
    
      indarr.append(i)
      
  return indarr
  
def main():

  print len(indapproxpattern('AAAAA', 'AACAAGCTGATAAACATTTAAAGAG', 2))
  
  print len(indapproxpattern('GAGG', 'TTTAGAGCCTTCAGAGG', 2))

if __name__ == "__main__":
  main()
