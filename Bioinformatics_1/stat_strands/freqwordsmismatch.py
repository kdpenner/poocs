#!/usr/bin/env python -tt

from ..words import patterncount
from ..words.freqwords import builddict
from indapproxpattern import indapproxpattern

def freqwordsmismatch(string, klength, nummismatch):
  
  freqpatterns = {}
  mispatterns = []
  num_occur = []
  
  for i in xrange(0, len(string) - klength + 1):
  
    mispatterns.append(patterncount.subtext(string, i, klength))
    
    indices_approx = indapproxpattern(mispatterns[i], string, nummismatch)
    
    num_occur.append(len(indices_approx))

  max_num_occur = max(num_occur)
  
  for j in xrange(0, len(string) - klength + 1):
  
    if num_occur[j] == max_num_occur:
    
      freqpatterns = builddict(freqpatterns, mispatterns[j], j)

  return(freqpatterns)

def main():

#  print freqwordsmismatch('ACGTTGCATGTCGCATGATGCATGAGAGCT', 4, 1)

#  print freqwordsmismatch('CACAGTAGGCGCCGGCACACACAGCCCCGGGCCCCGGGCCGCCCCGGGCCGGCGGCCGCCGGCGCCGGCACACCGGCACAGCCGTACCGGCACAGTAGTACCGGCCGGCCGGCACACCGGCACACCGGGTACACACCGGGGCGCACACACAGGCGGGCGCCGGGCCCCGGGCCGTACCGGGCCGCCGGCGGCCCACAGGCGCCGGCACAGTACCGGCACACACAGTAGCCCACACACAGGCGGGCGGTAGCCGGCGCACACACACACAGTAGGCGCACAGCCGCCCACACACACCGGCCGGCCGGCACAGGCGGGCGGGCGCACACACACCGGCACAGTAGTAGGCGGCCGGCGCACAGCC', \
#  10, 2)

  f = open('/Users/kpenner/Downloads/dataset_9_7.txt', 'r')
  
  genome = f.readline()
  
  genome = genome.strip()
  
  f.close()

  print freqwordsmismatch(genome, 6, 3)


if __name__ == "__main__":
  main()
