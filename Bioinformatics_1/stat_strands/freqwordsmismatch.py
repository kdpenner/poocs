#!/usr/bin/env python -tt

from words.countallpatterns import countallpatterns
from words.countallpatterns import patterntonumber
from constrainedneighbors import constrainedneighbors
#from indapproxpattern import indapproxpattern
from words.reversecomp import reversecomp

def freqwordsmismatch(string, klength, nummismatch, reverse = False):
  
  freqpatternsmismatch = {}
  
  (numpattarr, strpattarr, strdict) = countallpatterns(string, klength)

#  print numpattarr
#  print strpattarr
#  print strdict
  
  misstrdict = {}
  
  for key in strdict.iterkeys():

    neighborhood = constrainedneighbors(key, nummismatch)

    foundindices = strdict[key]
    
    if reverse:
      reversekey = reversecomp(key)
      reverseneighborhood = constrainedneighbors(reversekey, nummismatch)
      neighborhood.extend(reverseneighborhood)
    
    for neighbor in neighborhood:

#      if neighbor not in misstrdict:
      
#        indices = indapproxpattern(neighbor, string, nummismatch)
      
#        misstrdict[neighbor] = list(indices)

#        index = patterntonumber(neighbor)
#        numpattarr[index] = len(indices)
#        strpattarr[index] = neighbor

# always always always remember the difference between a copy and a reference

      try:
        misstrdict[neighbor].extend(list(foundindices))
      except KeyError:
        misstrdict[neighbor] = list(foundindices)
        
      if neighbor != key:
        index = patterntonumber(neighbor)
        numpattarr[index] = numpattarr[index] + len(foundindices)
        strpattarr[index] = neighbor

#  for key in misstrdict.iterkeys():
#    index = patterntonumber(key)
#    if len(misstrdict[key]) != numpattarr[index]:
#      print 'Error'

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

  print freqwordsmismatch('ACGTTGCATGTCGCATGATGCATGAGAGCT', 4, 1, \
  reverse = True)
  
  print freqwordsmismatch('CTTGCCGGCGCCGATTATACGATCGCGGCCGCTTGCCTTCTTTATAATGCA'+
  'TCGGCGCCGCGATCTTGCTATATACGTACGCTTCGCTTGCATCTTGCGCGCATTACGTACTTATCGATTACTTAT'+
  'CTTCGATGCCGGCCGGCATATGCCGCTTTAGCATCGATCGATCGTACTTTACGCGTATAGCCGCTTCGCTTGCCG'+
  'TACGCGATGCTAGCATATGCTAGCGCTAATTACTTAT', 9, 3, reverse = True)

if __name__ == "__main__":
  main()
