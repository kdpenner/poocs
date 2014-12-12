#!/usr/bin/python -tt

import numpy
#import matplotlib.pyplot as plot

def target():

  # establish target function
  
  points = numpy.random.uniform(low = -1, high = 1, size = (2,2))

  #print points

  points = points[numpy.lexsort((points[:,1],points[:,0]))]

  #print points

  slope = (points[0,1]-points[1,1])/(points[0,0]-points[1,0])
  
  intercept = points[0,1]-slope*points[0,0]
  
  return(points, slope, intercept)
  
def eval_target(m, b, points_eval):

  sign = numpy.sign(points_eval[:,1] - (m*points_eval[:,0]+b))
  
  return(sign)
  
def hypothesis(num_points, w_mod, x_mod):

  h = numpy.zeros(num_points)
  
  for i in range(0, num_points):
    h[i] = numpy.sign(numpy.dot(w_mod[i,:].T, x_mod[i,:]))
    
  #print h

  return(h)

def pla(N_points):

  pts, m_target, b_target = target()
  
  #print numpy.array([0.5, 0.5])-numpy.array([0.5, m*0.5+b])
  
  #print numpy.sign(0.5 - (m*0.5+b))
  
  #plot.plot(pts[:,0], pts[:,1])
  #plot.xlim(-1,1)
  #plot.ylim(-1,1)
  #plot.plot(0.5, 0.5, 'bo')
  
  
  #plot.show()
  
  x = numpy.random.uniform(low = -1, high = 1, size = (N_points, 2))

  #print x

  y = eval_target(m_target, b_target, x)
  
  #print y
  
  plot.plot(x[:,0], x[:,1], 'bo')
  plot.xlim(-1,1)
  plot.ylim(-1,1)
  plot.plot([-1, 1], [m_target*-1+b_target, m_target*1+b_target])
  
  #plot.show()

  x_pla = numpy.insert(x, 0, 1., axis = 1)
  
  #print x_pla
  
  w = numpy.zeros(x_pla.shape)
  
  #print w_init
  
  test = hypothesis(N_points, w, x_pla)

  j = 0

  while sum(y == test) != N_points:

    update = numpy.where(y != test)
    
    #print update

    index = update[0][0]

    #print w
    #print y
    #print x_pla
    #print x_pla[index,:]
    
    #print index
    
    w = w+y[index]*x_pla[index,:]
    
    #print w

    test = hypothesis(N_points, w, x_pla)
    
    #print test

    j += 1

  #print 'It took ', j, ' iterations to converge.'

  #print w
  
  #print y
  
  #print x_pla
  
  #print 'Final weight matrix:', w

  m_est = -1.*w[0][1]/w[0][2]
  
  b_est = -1.*w[0][0]/w[0][2]

  plot.plot([-1, 1], [m_est*-1+b_est, m_est*1+b_est], 'r-')
  
  plot.show()

  new_x = numpy.random.uniform(low = -1, high = 1, size = (N_points, 2))

  new_x_pla = numpy.insert(new_x, 0, 1., axis = 1)

  new_f = eval_target(m_target, b_target, new_x)

  new_g = hypothesis(N_points, w, new_x_pla)
  
  #print new_x_pla
  #print new_f
  #print new_g

  p_disagree = float(sum(new_f != new_g))/float(N_points)

  #print p_disagree

  return(j, p_disagree)

def main():

  N_x = 10

  N_iter = 5
  
  N_converge = numpy.zeros(N_iter)
  
  p = []
  
  for k in range(0,N_iter):
    N_converge_iter, p_iter = pla(N_x)
    N_converge[k] = N_converge_iter
    p.append(p_iter)

  print 'For', N_iter, 'iterations and', N_x, 'points, average convergence took', numpy.mean(N_converge), 'steps.'

  print 'For', N_iter, 'iterations and', N_x, 'points, average disagreement with', numpy.mean(p), 'of new sample.'

if __name__ == '__main__':
  main()
