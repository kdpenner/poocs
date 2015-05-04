#!/usr/bin/env python -tt

import skew
import numpy

def indminskew(genome):

  skewarr = skew.skew(genome)
  
  indices = numpy.where(skewarr == numpy.amin(skewarr))
  
#  print skewarr
  
  return(indices[0])

def main():

  print indminskew('TAAAGACTGCCGAGAGGCCAACACGAGTGCTAGAACGAGGGGCGTAAACGCGGGTCCGAT')

#  f = open('dataset_7_6.txt', 'r')
  
#  genome = f.readline()
  
#  genome = genome.strip()
  
#  f.close()
  
#  print indminskew(genome)

if __name__ == "__main__":
  main()
