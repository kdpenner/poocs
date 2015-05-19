#!/usr/bin/env python -tt

from words.countallpatterns import countallpatterns
from words.countallpatterns import patterntonumber
from constrainedneighbors import constrainedneighbors
from indapproxpattern import indapproxpattern

def freqwordsmismatch(string, klength, nummismatch):
  
  freqpatternsmismatch = {}
  
  (numpattarr, strpattarr, strdict) = countallpatterns(string, klength)

#  print numpattarr
#  print strpattarr
#  print strdict
  
  misstrdict = {}
  
  for key in strdict.iterkeys():

    neighborhood = constrainedneighbors(key, nummismatch)
    
    for neighbor in neighborhood:

      if neighbor not in misstrdict:
      
        indices = indapproxpattern(neighbor, string, nummismatch)
      
# always always always remember the difference between a copy and a reference

        misstrdict[neighbor] = list(indices)

        index = patterntonumber(neighbor)
        numpattarr[index] = len(indices)
        strpattarr[index] = neighbor

  max_num_occur = max(numpattarr)
  
  num_allwords = long(4.**klength)
  
  for j in xrange(0, num_allwords):
  
    if numpattarr[j] == max_num_occur:
    
      freqpatternsmismatch[strpattarr[j]] = list(misstrdict[strpattarr[j]])
      
#  print freqpatternsmismatch

  return(freqpatternsmismatch)

def main():

  print freqwordsmismatch('AACAAGCTGATAAACATTTAAAGAG', 5, 1)

  print freqwordsmismatch('ACGTTGCATGTCGCATGATGCATGAGAGCT', 4, 1)

  print freqwordsmismatch('CACAGTAGGCGCCGGCACACACAGCCCCGGGCCCCGGGCCGCCCCGGGCCG'+
  'GCGGCCGCCGGCGCCGGCACACCGGCACAGCCGTACCGGCACAGTAGTACCGGCCGGCCGGCACACCGGCACACC'+
  'GGGTACACACCGGGGCGCACACACAGGCGGGCGCCGGGCCCCGGGCCGTACCGGGCCGCCGGCGGCCCACAGGCG'+
  'CCGGCACAGTACCGGCACACACAGTAGCCCACACACAGGCGGGCGGTAGCCGGCGCACACACACACAGTAGGCGC'+
  'ACAGCCGCCCACACACACCGGCCGGCCGGCACAGGCGGGCGGGCGCACACACACCGGCACAGTAGTAGGCGGCCG'+
  'GCGCACAGCC', 10, 2)

if __name__ == "__main__":
  main()
