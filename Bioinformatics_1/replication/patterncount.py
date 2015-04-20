#!/usr/bin/env python -tt

def subtext(text, start, num_characters):

#  print text[start:start+num_characters]

  return(text[start:start+num_characters])

def patterncount(text, pattern):

  count = 0
  
  for i in xrange(0, len(text) - len(pattern) + 1):
    
    if subtext(text, i, len(pattern)) == pattern:
    
      count += 1
      
  return(count)
  
def main():

#  print patterncount('ACAACTATGCATACTATCGGGAACTATCCT', 'ACTAT')
  
#  print patterncount('CGATATATCCATAG', 'ATA')
  
#  print patterncount('GCGCG', 'GCG')

  print patterncount('ACCTAAAGCACCTAAAGCCACCAAAAGGTCGATCACAACCGGCCTGTCGAACCTAAACGTACCTAAATGACCTAAACGACCTAAAACCTAAAGGTGTCTGGGACCTAAAACCTAAATCACCTAAAACCTAAACTGACCTAAACCCCGGGACGACGTCGTAAAGTAGACCTAAACGACCTAAAACCTAAAAAACCTAAAACCTAAATACCTAAAGACGACCTAAACACCTAAATGCACCTAAAACCTAAAATCAGCGGACCTAAAACCTAAATACCTAAAACCTAAAAAACCTAAACACCTAAAGACCTAAACCTACCTAAATCGTACCTAAATTCCGTAAACCTAAATGAGTCGCCGGGCACCTAAAGACCTAAAACTGGACCTAAACCTCGGCACCTAAATACCTAAATCACCTAAAGACCTAAAACCTAAAACCTAAAGCGGCACCTAAATACCCTTGACCTAAAGGACCTAAACAGACCTAAAGGACCTAAAACCTAAAACCTAAAAACCTAAATATGGTCAACCTAAAATACCTAAACTTACCTAAATAAACCTAAAACCTAAAACCTAAAACCTAAAACCTAAATGTTTACCTAAACTTCACCTAAAACCTAAATGTAACCTAAATTACCTAAAGTCTGAAACCTAAATACCTAAATCGATACCTAAAGTTGACCTAAATACCTAAAACACCTAAACTCACCTAAAGGCAGTCACCTAAATACCTAAATACCTAAAGGAACCTAAAGCTACCTAAATACCTAAAACCTAAAGGCAGCGAAGAAACCTAAACACCTAAATTGCAAACCTAAAACCTAAAATATAACCTAAACGGCACCTAAATCACCTAAATGACCTAAACCTACACTAACCTAAAACCTAAAACCTAAAACCTAAACCCTACCTAAATGCACCTAAAGCACATTT', 'ACCTAAAAC')

if __name__ == "__main__":
  main()