#!/usr/bin/python -tt

import linreg
import numpy

def pla(N_points):

  pts, m_target, b_target = linreg.target()
  
  x = numpy.random.uniform(low = -1, high = 1, size = (N_points, 2))

  y = linreg.eval_target(m_target, b_target, x)

  x_mod = numpy.insert(x, 0, 1., axis = 1)
  
  x_dagger = numpy.dot(numpy.linalg.inv(numpy.dot(x_mod.T, x_mod)), x_mod.T)
  
  w = numpy.dot(x_dagger, y)

  test = numpy.sign(numpy.dot(x_mod, w))
  
  j = 0

  while sum(y == test) != N_points:

    update = numpy.where(y != test)

    index = update[0][0]
    
    w = w+y[index]*x_mod[index,:]
    
    #print w

    test = numpy.sign(numpy.dot(x_mod, w))
    
    #print test

    j += 1

  #new_x = numpy.random.uniform(low = -1, high = 1, size = (N_points, 2))

  #new_x_pla = numpy.insert(new_x, 0, 1., axis = 1)

  #new_f = eval_target(m_target, b_target, new_x)

  #new_g = hypothesis(N_points, w, new_x_pla)
  
  #p_disagree = float(sum(new_f != new_g))/float(N_points)

  return(j)

def main():

  N_x = 10

  N_iter = 1000
  
  N_converge = numpy.zeros(N_iter)
  
  for k in range(0, N_iter):
    N_converge[k] = pla(N_x)

  print 'For', N_iter, 'iterations and', N_x, 'points, average convergence took', numpy.median(N_converge), 'steps.'

if __name__ == '__main__':
  main()
