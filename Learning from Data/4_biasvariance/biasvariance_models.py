#!/usr/bin/python -tt

import numpy
import matplotlib.pyplot as plot

def linreg(x, y):

  x_dagger = numpy.dot(numpy.linalg.inv(numpy.dot(x.T, x)), x.T)
  
  w = numpy.dot(x_dagger, y)

  return(w)

def bias(gbar, f):
  
  b = numpy.mean(numpy.square(gbar-f))
  
  return(b)
  
def variance(gbar, g):
  
  diff = numpy.zeros(g.shape)
  
  for i in range(0, g.shape[1]):
    diff[:,i] = numpy.square(g[:,i] - gbar)

  var = numpy.mean(diff)
  
  return(var)

def main():

  N_iter = 100000
  
  N_param = 1

  N_points = 2
  
  N_integrands = 1000
  
  ws = numpy.zeros((N_param, N_iter))
  
  g = numpy.zeros((N_integrands, N_iter))
  
  testx = numpy.linspace(-1, 1, N_integrands)
  
  for k in range(0, N_iter):

    x = numpy.random.uniform(low = -1, high = 1, size = (N_points, 1))

#    x_mod = numpy.insert(x, 0, 1., axis = 1)

    x_mod = x

    y = numpy.sin(numpy.pi*x_mod)

    ws[:,k] = linreg(numpy.square(x_mod), y)

    g[:,k] = ws[0,k]*numpy.square(testx)# + ws[1,k]*numpy.square(testx)
    
#    print x_mod
    
#    print y
    
#    print ws[:,k]
    
#    plot.plot(x, y, 'bo')
#    plot.xlim(-1,1)
#    plot.ylim(-1,1)
#    plotx = numpy.linspace(-1, 1, 100)
#    ploty1 = numpy.sin(numpy.pi*plotx)
#    ploty2 = numpy.square(plotx)*ws[:,k]
#    plot.plot(plotx, ploty1, 'g-')
#    plot.plot(plotx, ploty2, 'r-')
  
#    plot.show()

#  intercept_avg = numpy.mean(ws[0,:])
  slope_avg = numpy.mean(ws[0,:])

  gbar = slope_avg*numpy.square(testx)# + intercept_avg
  
  f = numpy.sin(numpy.pi*testx)
  
  print 'Average slope is:', slope_avg
#  print 'Average intercept is:', intercept_avg
  print 'Bias is:', bias(gbar, f)
  print 'Variance is:', variance(gbar, g)


if __name__ == '__main__':
  main()
