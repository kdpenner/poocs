#!/usr/bin/env python -tt

from words.freqwords import builddict
from words.countallpatterns import countallpatterns
from indapproxpattern import indapproxpattern
from numbertopattern import numbertopattern2

def freqwordsmismatch(string, klength, nummismatch):
  
  freqpatterns = {}
  
  (numpattarr, strpattarr, strdict) = countallpatterns(string, klength)

#  print strdict

  for i, numpatt in enumerate(numpattarr):
  
    if numpatt == 0:

      strtest = numbertopattern2(i, klength)
      
      indices = indapproxpattern(strtest, string, nummismatch)
      
      if len(indices):

        numpattarr[i] = len(indices)
        strpattarr[i] = strtest

        for index in indices:
        
          strdict = builddict(strdict, strtest, index)
        
#  print strdict

  max_num_occur = max(numpattarr)
  
  num_allwords = long(4.**klength)
  
  for j in xrange(0, num_allwords):
  
    if numpattarr[j] == max_num_occur:
    
      freqpatterns[strpattarr[j]] = strdict[strpattarr[j]]

  return(freqpatterns)

def main():

  print freqwordsmismatch('ACGTTGCATGTCGCATGATGCATGAGAGCT', 4, 1)

#  print freqwordsmismatch('CACAGTAGGCGCCGGCACACACAGCCCCGGGCCCCGGGCCGCCCCGGGCCGGCGGCCGCCGGCGCCGGCACACCGGCACAGCCGTACCGGCACAGTAGTACCGGCCGGCCGGCACACCGGCACACCGGGTACACACCGGGGCGCACACACAGGCGGGCGCCGGGCCCCGGGCCGTACCGGGCCGCCGGCGGCCCACAGGCGCCGGCACAGTACCGGCACACACAGTAGCCCACACACAGGCGGGCGGTAGCCGGCGCACACACACACAGTAGGCGCACAGCCGCCCACACACACCGGCCGGCCGGCACAGGCGGGCGGGCGCACACACACCGGCACAGTAGTAGGCGGCCGGCGCACAGCC', \
#  10, 2)

#  f = open('/Users/kpenner/Downloads/dataset_9_7.txt', 'r')
  
#  genome = f.readline()
  
#  genome = genome.strip()
  
#  f.close()

#  print freqwordsmismatch(genome, 6, 3)


if __name__ == "__main__":
  main()
