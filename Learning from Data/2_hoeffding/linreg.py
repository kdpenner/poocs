#!/usr/bin/python -tt

import numpy
#import matplotlib.pyplot as plot

def target():

  # establish target function
  
  points = numpy.random.uniform(low = -1, high = 1, size = (2,2))

  points = points[numpy.lexsort((points[:,1],points[:,0]))]

  slope = (points[0,1]-points[1,1])/(points[0,0]-points[1,0])
  
  intercept = points[0,1]-slope*points[0,0]
  
  return(points, slope, intercept)
  
def eval_target(m, b, points_eval):

  sign = numpy.sign(points_eval[:,1] - (m*points_eval[:,0]+b))
  
  return(sign)

def linreg(N_points):

  pts, m_target, b_target = target()
  
  x = numpy.random.uniform(low = -1, high = 1, size = (N_points, 2))

  y = eval_target(m_target, b_target, x)

  x_mod = numpy.insert(x, 0, 1., axis = 1)
  
  x_dagger = numpy.dot(numpy.linalg.inv(numpy.dot(x_mod.T, x_mod)), x_mod.T)
  
  w = numpy.dot(x_dagger, y)
  
  m_est = -1.*w[1]/w[2]
  
  b_est = -1.*w[0]/w[2]

  y_hypothesis = eval_target(m_est, b_est, x)

  Error_in = sum(y_hypothesis != y)/float(N_points)

  Error_in2 = sum(numpy.sign(numpy.dot(x_mod, w)) != y)/float(N_points)

  #plot.plot(x[:,0], x[:,1], 'bo')
  #plot.xlim(-1,1)
  #plot.ylim(-1,1)
  #plot.plot([-1, 1], [m_target*-1+b_target, m_target*1+b_target])


  #plot.plot([-1, 1], [m_est*-1+b_est, m_est*1+b_est], 'r-')
  
  #plot.show()

  new_x = numpy.random.uniform(low = -1, high = 1, size = (10*N_points, 2))
  
  new_x_mod = numpy.insert(new_x, 0, 1., axis = 1)

  new_f = eval_target(m_target, b_target, new_x)

  new_f_hypothesis = eval_target(m_est, b_est, new_x)

  Error_out = sum(new_f != new_f_hypothesis)/(10.*N_points)
  
  Error_out2 = sum(numpy.sign(numpy.dot(new_x_mod, w)) != new_f)/float(10.*N_points)

  return(Error_in, Error_out, Error_in2, Error_out2, w)

def main():

  N_x = 100

  N_iter = 1000
  
  ein = []
  eout = []
  ein2 = []
  eout2 = []
  
  for k in range(0, N_iter):
    eint, eoutt, eint2, eoutt2, wt = linreg(N_x)
    ein.append(eint)
    eout.append(eoutt)
    ein2.append(eint2)
    eout2.append(eoutt2)
  
  print 'For', N_iter, 'iterations and', N_x, 'points, average E_in is', numpy.median(ein), 'and average E_out is', numpy.median(eout), '.'

  print 'Alt. measures:', numpy.median(ein2), numpy.median(eout2)

if __name__ == '__main__':
  main()
