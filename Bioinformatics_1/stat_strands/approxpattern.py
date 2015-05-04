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
  
def lenapproxpattern(pattern, string, mismatch):

  indices = indapproxpattern(pattern, string, mismatch)
  
  return(len(indices))

def main():

#  print ' '.join(indapproxpattern('ATTCTGGA', \
#  'CGCCCGAATCCAGAACGCATTCCCATATTTCGGGACCACTGGCCTCCACGGTACGGACGTCAATCAAAT', \
#  3))

#  f = open('/Users/kpenner/Downloads/dataset_9_4.txt', 'r')
  
#  string1 = f.readline()
  
#  string1 = string1.strip()

#  f.close()

#  print ' '.join(indapproxpattern('AAGGGACAGGA', string1, 4))

#  print lenapproxpattern('AAAAA', 'AACAAGCTGATAAACATTTAAAGAG', 2)
  
#  print lenapproxpattern('GAGG', 'TTTAGAGCCTTCAGAGG', 2)

  f = open('/Users/kpenner/Downloads/dataset_9_6.txt', 'r')
  
  string = f.readline()
  
  string = string.strip()

  f.close()

  print lenapproxpattern('ACTAAA', string, 2)

if __name__ == "__main__":
  main()
