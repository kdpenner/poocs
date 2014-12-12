#!/usr/bin/python -tt

import numpy
import matplotlib.pyplot as plot

def target():

  points = numpy.random.uniform(low = -1, high = 1, size = (2,2))

  points = points[numpy.lexsort((points[:,1],points[:,0]))]

  slope = (points[0,1]-points[1,1])/(points[0,0]-points[1,0])
  
  intercept = points[0,1]-slope*points[0,0]
  
  return(slope, intercept)

def eval_target(m, b, points_eval):

  sign = numpy.sign(points_eval[:,1] - (m*points_eval[:,0]+b))
  
  return(sign)
  
def egrad(x, y, weights):

  egrad = -1.*y*x/(1.+numpy.exp(y * numpy.dot(x, weights.T)))
  
  return(egrad)
  
def crossentropy(x, y, weights):

  error = numpy.mean(numpy.log(1.+numpy.exp(-1.*y*numpy.dot(x, weights.T))))
  
  return(error)

def main():

  N_iter = 5
  
  N_pts = 100

  e_out = numpy.zeros(N_iter)

  epoch_num = numpy.zeros(N_iter)

  for k in range(0, N_iter):

    m, b = target()
  
    x = numpy.random.uniform(low = -1, high = 1, size = (N_pts, 2))
  
    y = tuple(eval_target(m, b, x))
  
    fx = numpy.array(y)
  
    fx[fx == -1] = 0

    x = numpy.insert(x, 0, 1., axis = 1)
  
    weights = numpy.array([[0., 0., 0.]])

    full = numpy.insert(x, 0, y, axis = 1)

    change = numpy.array([1., 1., 1.])

    q = 0

    while numpy.sqrt(numpy.sum(numpy.square(change))) > .01:
  
      epoch = numpy.random.permutation(full)

      weights0 = weights[-1]

      for j in range(0,N_pts):

        change0 = .01*egrad(epoch[j,1:4], epoch[j,0], weights0)
        weights0 = weights0 - change0

      change = weights0 - weights[-1]
      
      weights = numpy.append(weights, [weights0], axis = 0)
      
      q = q+1

    plotx = numpy.dot(x, weights[-1])
    plot.plot(plotx, numpy.exp(plotx)/(1.+numpy.exp(plotx)), 'bo')
    plot.show()
    
    epoch_num[k] = q
    
    newx = numpy.random.uniform(low = -1, high = 1, size = (1000, 2))

    newy = eval_target(m, b, newx)

    newx = numpy.insert(newx, 0, 1., axis = 1)
  
    e_out[k] = crossentropy(newx, newy, weights[-1])
  
  print 'Median E_out is:', numpy.median(e_out)
  print 'Avg. E_out is:', numpy.mean(e_out)
  print 'Median num. of epochs is:', numpy.median(epoch_num)
  print 'Avg. num. of epochs is:', numpy.mean(epoch_num)

if __name__ == '__main__':
  main()
