#!/usr/bin/env python -tt

from hammingdist import hammingdist

def constrainedneighbors(pattern, hammingd):

  """
  Generates all strings that differ by a given number or less of characters
  
  Inputs:
  pattern -- a string. Each character of the string must be either 'A', 'C',
  'G', or 'T'.
  hammingd -- the maximum number of characters you want to allow to differ.
  
  Output:
  a list of all strings that differ by 'hammingd' or fewer characters. For
  example, constrainedneighbors('AA', 1) will return [AA, AC, AG, AT, CA, GA,
  TA].
  
  I finally understand this recursive program. It strips away the leading
  character of 'pattern' until it reaches the last character. For each strip it
  stores the leading character and trailing character(s). The last character
  will be one of A, C, G, or T. The program compares the last character to each
  of A, C, G, and T and depending on 'hammingd' and the last character either:
  1) adds each of A, C, G, and T to the last character; or
  2) adds one of A, C, G, or T to the penultimate character.
  For example, if 'hammingd' is 1 and the last two characters are GT the output
  at this step is [GA, GC, GG, AT, CT, GT, TT]. (T differs from A so add GA;
  T differs from C so add GC; T differs from G so add GG; T is the same as T
  so add AT, CT, GT, and TT.) The program then compares this output with the
  last 2 characters of 'pattern' and so on.
  
  Each string in the output list differs from 'pattern' by 'hammingd' or fewer
  characters. constrainedneighborsexact will return each string that differs
  by 'hammingd' characters.
  
  The length of the output list should be sum(index from 0 to hammingd,
  choose(len(pattern), index) * 3^index)
  """
  

  if hammingd == 0:
  
    return(pattern)
    
  if len(pattern) == 1:
  
    return(['A', 'C', 'G', 'T'])

  nucleotides = ['A', 'C', 'G', 'T']

  neighborhood = []
  
  prefixpattern = pattern[0]
  suffixpattern = pattern[1:]

#  print 'Prefix pattern:', prefixpattern
#  print 'Suffix pattern:', suffixpattern
#  print 'Neighborhood:', neighborhood
  
  suffixneighbors = constrainedneighbors(suffixpattern, hammingd)
  
#  print 'Suffix neighborhood:', suffixneighbors
  
  for suffixneighbor in suffixneighbors:
  
    if hammingdist(suffixpattern, suffixneighbor) < hammingd:
    
      for nucleotide in nucleotides:

        neighborhood.append(nucleotide + suffixneighbor)
        
    else:

      neighborhood.append(prefixpattern + suffixneighbor)
      
  return(neighborhood)

def constrainedneighborsexact(pattern, hammingd):

  """
  Still thinking about this one
  """

  if hammingd == 0:
  
    return(pattern)
    
  if len(pattern) == 1:
  
    return(['A', 'C', 'G', 'T'])

  nucleotides = ['A', 'C', 'G', 'T']

  neighborhood = []
  
  prefixpattern = pattern[0]
  suffixpattern = pattern[1:]

  print 'Prefix pattern:', prefixpattern
  print 'Suffix pattern:', suffixpattern
  
  suffixneighbors = constrainedneighborsexact(suffixpattern, hammingd)
  
  print 'Suffix neighborhood:', suffixneighbors

  for suffixneighbor in suffixneighbors:
  
    if hammingdist(suffixpattern, suffixneighbor) < hammingd:
    
      for nucleotide in nucleotides:

        neighborhood.append(nucleotide + suffixneighbor)
        
    else:

      neighborhood.append(prefixpattern + suffixneighbor)
      
  print 'Final:', neighborhood
      
  return(neighborhood)

  
def main():

#  lala = constrainedneighbors('ACGT', 1)
#  print len(lala)
#  lala = constrainedneighbors('ACGT', 2)
#  print len(lala)
#  lala = constrainedneighbors('ACGT', 3)
#  print len(lala)
  lala = constrainedneighborsexact('ACGT', 1)
  print len(lala)
  lala = constrainedneighborsexact('ACGT', 2)
  print len(lala)
  lala = constrainedneighborsexact('ACGT', 3)
  print len(lala)

if __name__ == "__main__":
  main()
