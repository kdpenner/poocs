#!/usr/bin/env python -tt

import patterncount
import freqwords

def findpattclump(genome, klength, windowlength, numoccur):

  clumpdict = {}

  subgenome = patterncount.subtext(genome, 0, windowlength)
  
  occurdict = freqwords.freqwords(subgenome, klength)

  for key in occurdict.iterkeys():

    numoccurkey = len(occurdict[key])

    if numoccurkey >= numoccur:

      freqwords.builddict(clumpdict, key, numoccurkey)

  for i in xrange(1, len(genome) - windowlength + 1):

    subgenome = patterncount.subtext(genome, i, windowlength)
    
    newpattern = subgenome[-(klength):]

    numoccurkey = patterncount.patterncount(subgenome, newpattern)

    if numoccurkey >= numoccur:

      freqwords.builddict(clumpdict, newpattern, numoccurkey)

  return(clumpdict)

def main():

#  print findpattclump('CGGACTCGACAGATGTGAAGAACGACAATGTGAAGACTCGACACGACAGAGTGAAGAGAAGAGGAAACATTGTAA', 5, 50, 4)
  
#  print findpattclump('CCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCAAAAAAAAAAAAAAAAAAAAAA', 5, 10, 2)

#  print ' '.join(findpattclump('CGGACTCGACAGATGTGAAGAACGACAATGTGAAGACTCGACACGACAGAGTGAAGAGAAGAGGAAACATTGTAA', 5, 50, 4).keys())

#  f = open('testgenome1.dat', 'r')
  
#  genome = f.readline()
  
#  genome = genome.strip()
  
#  f.close()
  
#  print ' '.join(findpattclump(genome, 11, 566, 18).keys())

#  f = open('testgenome2.dat', 'r')
  
#  genome = f.readline()
  
#  genome = genome.strip()
  
#  f.close()
  
#  print ' '.join(findpattclump(genome, 11, 536, 16).keys())

if __name__ == "__main__":
  main()
