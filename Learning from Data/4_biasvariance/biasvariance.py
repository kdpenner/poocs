#!/usr/bin/python -tt

import numpy
import matplotlib.pyplot as plot

def linreg():

  N_points = 2

  x = numpy.random.uniform(low = -1, high = 1, size = (N_points, 1))

  y = numpy.sin(numpy.pi*x)
  
  x_dagger = numpy.dot(numpy.linalg.inv(numpy.dot(x.T, x)), x.T)
  
#  print numpy.sum(x*y)/numpy.sum(x*x)
  
  w = numpy.dot(x_dagger, y)
  
#  print w

#  plot.plot(x, y, 'bo')
#  plot.xlim(-1,1)
#  plot.ylim(-1,1)
#  plot.plot([-1, 1], [-1*w[0], 1*w[0]], 'r-')

#  plotx = numpy.linspace(-1, 1, 100)

#  ploty = numpy.sin(numpy.pi*plotx)

#  plot.plot(plotx, ploty, 'g-')
  
#  plot.show()

  return(w)

def bias(m_bar):

# m_bar is average slope

  b = 0.5*(2./3.*numpy.square(m_bar)-4.*m_bar/numpy.pi+1.)
  
#  print b
  
#  testx = numpy.linspace(-1, 1, 1000)
  
#  gbar = m_bar*testx
  
#  f = numpy.sin(numpy.pi*testx)
  
#  plot.plot(testx, gbar, 'r-')
#  plot.plot(testx, f, 'g-')
#  plot.xlim(-1,1)
#  plot.ylim(-1,1)
  
#  plot.show()

#  plot.plot(testx, numpy.square(gbar-f), 'r-')
#  plot.xlim(-1,1)
#  plot.ylim(-1,1)
  
#  plot.show()

#  print gbar[0:10]
#  print f[0:10]
#  print numpy.square(gbar[0:10]-f[0:10])
#  print numpy.mean(numpy.square(gbar-f))
  
#  print 0.5*numpy.trapz(numpy.square(gbar-f), testx)
  
  return(b)
  
def variance(m_bar, m):

  difference = m-m_bar
  
#  plot.hist(difference)
  
#  plot.show()
  
#  plot.hist(numpy.square(difference))
  
#  plot.show()
  
  expect_data = numpy.mean(numpy.square(difference))
  
  var = 1./3.*expect_data
  
#  testx = numpy.linspace(-1,1,1000)
  
#  print numpy.mean(expect_data*numpy.square(testx))
  
  return(var)

def main():

  N_iter = 100000
  
  slopes = numpy.zeros(N_iter)
  
  for k in range(0, N_iter):
    slopes[k] = linreg()

#  plot.hist(slope)
  
#  plot.show()
  
  slope_avg = numpy.mean(slopes)
  
  print 'Average slope is:', slope_avg
  print 'Bias is:', bias(slope_avg)
  print 'Variance is:', variance(slope_avg, slopes)
  

if __name__ == '__main__':
  main()
