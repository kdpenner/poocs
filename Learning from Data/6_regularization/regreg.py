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
  
def reglinreg(x, y, k):

  N_points = x.shape[0]
  
  I_size = x.shape[1]
  
  x_dagger = numpy.dot(numpy.linalg.inv(numpy.dot(x.T, x) + \
  numpy.power(10., k)*numpy.identity(I_size)), x.T)
  
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
  
  train = numpy.loadtxt(file1)

  newx = transform(train[:,0:2])
  
  weights, E_in = linreg(newx, train[:,2])
  
  print 'Weights:', weights
  
  print 'In sample error of training set:', E_in
  
  file2 = sys.argv[2]
  
  test = numpy.loadtxt(file2)
  
  newxtest = transform(test[:,0:2])
  
  y_hypo = numpy.sign(numpy.dot(newxtest, weights))
  
  N_points = len(test[:,0])
  
  E_out = sum(y_hypo != test[:,2])/float(N_points)
  
  print 'Out of sample error of test set:', E_out
  
  k = sys.argv[3]
  
  k = float(k)
  
  regweights, regE_in = reglinreg(newx, train[:,2], k)
  
  print 'Reg. weights for k =', k, ':', regweights
  
  print 'In sample error of reg. training set:', regE_in
  
  regy_hypo = numpy.sign(numpy.dot(newxtest, regweights))
  
  regE_out = sum(regy_hypo != test[:,2])/float(N_points)
  
  print 'Out of sample error of reg. test set:', regE_out

if __name__ == '__main__':
  main()
