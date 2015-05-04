#!/usr/bin/env python -tt

def hammingdist(string1, string2):

  dist = 0

  for i, char in enumerate(string1):
  
    if char != string2[i]:
    
      dist = dist + 1

  return(dist)

def main():

  print hammingdist('GGGCCGTTGGT', 'GGACCGTTGAC')

#  f = open('dataset_9_3.txt', 'r')
  
#  string1 = f.readline()
  
#  string1 = string1.strip()
  
#  string2 = f.readline()
  
#  string2 = string2.strip()
  
#  f.close()
  
#  print hammingdist(string1, string2)


if __name__ == "__main__":
  main()
