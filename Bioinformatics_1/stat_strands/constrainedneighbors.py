#!/usr/bin/env python -tt

from hammingdist import hammingdist

def constrainedneighbors1(pattern, hammingd):

  if hammingd == 0:
  
    return(pattern)
    
  if len(pattern) == 1:
  
    return(['A', 'C', 'G', 'T'])

  nucleotides = ['A', 'C', 'G', 'T']

  neighborhood = []
  
  prefixpattern = pattern[0]
  suffixpattern = pattern[1:]
  
  suffixneighbors = constrainedneighbors1(suffixpattern, hammingd)
  
#  print suffixneighbors
  
  for suffixneighbor in suffixneighbors:
  
    if hammingdist(suffixpattern, suffixneighbor) < hammingd:
    
      for nucleotide in nucleotides:

        neighborhood.append(nucleotide + suffixneighbor)
        
    else:
    
      neighborhood.append(prefixpattern + suffixneighbor)
      
  return(neighborhood)
  
#def constrainedneighbors2(pattern, hammingd):

#  nucleotides = ['A', 'C', 'G', 'T']

#  keeppattern = pattern
#  numiter = len(pattern)

#  for i in xrange(0, numiter):
  
#    neighborhood = []
    
#    prefix = pattern[:-2]
#    penultimate = pattern[-2]
#    suffix = pattern[-1]
    
#    for nucleotide in nucleotides:
    
#      if hammingdist(penultimate+nucleotide, penultimate+suffix) < hammingd:
      
#        neighborhood.append(prefix+penultimate+nucleotide)
        
#      else:
      
#        neighborhood.append(prefix+penultimate+suffix)
        
#    if len(pattern) > 2:
#      pattern = pattern[:-1]
#    else:
#      break
        
#  print neighborhood
    
#  return

def main():

  print constrainedneighbors1('AG', 1)
  
  print constrainedneighbors1('GC', 1)
  
  print constrainedneighbors1('ACG', 1)

#  print constrainedneighbors2('AG', 1)
  
#  print constrainedneighbors2('GC', 1)
  
#  print constrainedneighbors2('ACG', 1)


if __name__ == "__main__":
  main()
