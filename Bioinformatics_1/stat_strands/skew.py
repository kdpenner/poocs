#!/usr/bin/env python -tt

import numpy

def skew(genome):

  skewarr = numpy.zeros(len(genome)+1)
  
  for i, base in enumerate(genome, start = 1):
  
#    print i, base
  
    if base == 'A' or base == 'T':
      skewarr[i] = skewarr[i-1]
    elif base == 'C':
      skewarr[i] = skewarr[i-1]-1
    elif base == 'G':
      skewarr[i] = skewarr[i-1]+1

  return(skewarr)

def main():

  print skew('CATGGGCATCGGCCATACGCC')
  
  print skew('GAGCCACCGCGATA')

if __name__ == "__main__":
  main()
