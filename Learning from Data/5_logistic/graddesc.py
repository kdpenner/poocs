#!/usr/bin/python -tt

import numpy

def error(weights):

  two = numpy.float_(2.)

  u = weights[0]
  
  v = weights[1]
  
  errorval = numpy.square(u*numpy.exp(v)-two*v*numpy.exp(-u))

  return(errorval)

def egrad(weights):

  u = weights[0]
  
  v = weights[1]
  
  two = numpy.float_(2.)
  
  common = two*(u*numpy.exp(v)-two*v*numpy.exp(-u))

  partialu = common*(numpy.exp(v)+two*v*numpy.exp(-u))
  
  partialv = common*(u*numpy.exp(v)-two*numpy.exp(-u))
  
  norm = numpy.sqrt(numpy.square(partialu)+numpy.square(partialv))

  errorgrad = numpy.array([partialu, partialv], dtype = numpy.float_)

  return(errorgrad)

def main():

  init = numpy.array([1., 1.], dtype = numpy.float_)
  
  init_e = error(init)

  i = 0
  
  print 'Gradient descent:'
  
  while init_e > 1.e-14:
  
    change = -.1*egrad(init)
    
    init = init + change
    
    init_e = error(init)
    
    i = i+1
    
    print i, change, init, init_e
    
  initc = numpy.array([1., 1.], dtype = numpy.float_)
  
  print 'Coordinate descent:'
  
  for j in range(0,15):
  
    change1 = -.1*egrad(initc)
    
    initc[0] = initc[0] + change1[0]
    
    change2 = -.1*egrad(initc)
    
    initc[1] = initc[1] + change2[1]
    
    print j, change1, change2, initc

  print error(initc)

if __name__ == '__main__':
  main()
