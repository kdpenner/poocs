#!/usr/bin/python -tt

import sys
import numpy

def linreg(x, y):

  N_points = x.shape[0]
  
  x_dagger = numpy.dot(numpy.linalg.inv(numpy.dot(x.T, x)), x.T)
  
  w = numpy.dot(x_dagger, y)

  y_hypothesis = numpy.sign(numpy.dot(x, w))

  Error_in = sum(y_hypothesis != y)/float(N_points)

  return(w, Error_in)
  
def transform(x):

  x1 = x[:,0]
  x2 = x[:,1]
  
  nonlin_x = numpy.array([x1, x2, numpy.square(x1), numpy.square(x2), \
  x1*x2, numpy.abs(x1-x2), numpy.abs(x1+x2)])
  
  nonlin_x = numpy.insert(nonlin_x, 0, 1., axis = 0).T
  
  return(nonlin_x)

def main():

  file1 = sys.argv[1]
  
  data = numpy.loadtxt(file1)
  
  train = data[25:]
  
  valid = data[0:25]

  train_newx = transform(train[:,0:2])

  val_newx = transform(valid[:,0:2])

  file2 = sys.argv[2]

  out = numpy.loadtxt(file2)
  
  out_newx = transform(out[:,0:2])
  
  for i in range(0, train_newx.shape[1]):

    weights, E_in = linreg(train_newx[:,0:i+1], train[:,2])

    val_y = numpy.sign(numpy.dot(val_newx[:,0:i+1], weights))

    val_error = sum(val_y != valid[:,2])/float(len(valid))

    print 'Validation error for k =', i, ':', val_error

    out_y = numpy.sign(numpy.dot(out_newx[:,0:i+1], weights))
    
    out_error = sum(out_y != out[:,2])/float(len(out))
  
    print 'Out of sample error for k =', i, ':', out_error
  
#  y_hypo = numpy.sign(numpy.dot(newxtest, weights))
  
#  N_points = len(test[:,0])
  
#  E_out = sum(y_hypo != test[:,2])/float(N_points)
  
#  print 'Out of sample error of test set:', E_out
  
if __name__ == '__main__':
  main()
