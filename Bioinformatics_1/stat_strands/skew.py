#!/usr/bin/env python -tt

def skew(genome):

  skewarr = [0]
  
  for i, base in enumerate(genome, start = 1):
  
#    print i, base
  
    if base == 'A' or base == 'T':
      skewarr.append(skewarr[i-1])
    elif base == 'C':
      skewarr.append(skewarr[i-1]-1)
    elif base == 'G':
      skewarr.append(skewarr[i-1]+1)

  return(skewarr)

def main():

  print skew('CATGGGCATCGGCCATACGCC')
  
  print skew('GAGCCACCGCGATA')

if __name__ == "__main__":
  main()
