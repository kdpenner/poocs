#!/usr/bin/env python -tt

from countallpatterns import countallpatterns

def freqwords_allwords(string, klength):

  freqpatterns = {}

  (count_allwords, words, dictwords) = countallpatterns(string, klength)
  
#  print count_allwords
#  print words
#  print dictwords
  
  max_num_occur = max(count_allwords)
  
  num_allwords = long(4.**klength)
  
  for j in xrange(0, num_allwords):
  
    if count_allwords[j] == max_num_occur:
    
      freqpatterns[words[j]] = dictwords[words[j]]

#  print freqpatterns
  
  return(freqpatterns)

def main():

  print freqwords_allwords('ACGCGGCTCTGAAA', 2)

if __name__ == "__main__":
  main()