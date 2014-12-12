#!/usr/bin/python -tt

import sys
import numpy

def mask(data, digits):

  data = numpy.insert(data, 1, 1, axis = 1)

  y = numpy.zeros(len(data))

  i = 1.

  for digit in digits:
    if digit.isdigit():
      y[data[:,0] == float(digit)] = i
      i = -1.*i
    elif not digit.isdigit() and digit == 'all':
      y[data[:,0] != float(digits[0])] = i
      i = -1*i
    elif not digit.isdigit() and digit != 'all':
      print 'Exiting. Did you mean to type "all"?'
      sys.exit(1)

  good = y != 0
  
  data = data[good,:]
  y = y[good]

  return(data, y)
  
def reglinreg(x, y, lam):

  I_size = x.shape[1]
  
  x_dagger = numpy.dot(numpy.linalg.inv(numpy.dot(x.T, x) + \
  lam*numpy.identity(I_size)), x.T)
  
  w = numpy.dot(x_dagger, y)
  
  return(w)
  
def error(x, y, w):

  N_points = x.shape[0]

  y_hypothesis = numpy.sign(numpy.dot(x, w))
  
  error = sum(y_hypothesis != y)/float(N_points)
  
  return(error)
  
def transform(x):

  x1 = x[:,2]
  x2 = x[:,3]
  
  nonlin_x = numpy.array([x1, x2, x1*x2, numpy.square(x1), numpy.square(x2)])

  nonlin_x = numpy.insert(nonlin_x, 0, 1., axis = 0).T

  nonlin_x = numpy.insert(nonlin_x, 0, x[:,0], axis = 1)
  
  return(nonlin_x)

def main():

  args = sys.argv[1:]

  if not args or len(args) != 6:
    print 'usage: file_train file_test {--lin | --nonlin} lambda digit1 digit2'
    sys.exit(1)

  file1 = args[0]
  file2 = args[1]
  
  transflag = args[2]
  
  lam = float(args[3])
  digits = sorted(args[4:])

  train = numpy.loadtxt(file1, skiprows = 1)
  test = numpy.loadtxt(file2, skiprows = 1)
  
  input, output = mask(train, digits)
  testin, testout = mask(test, digits)

  if transflag == '--nonlin':
    input = transform(input)
    testin = transform(testin)
    w = reglinreg(input[:,1:], output, lam)
    ein = error(input[:,1:], output, w)
    eout = error(testin[:,1:], testout, w)
  elif transflag == '--lin':
    w = reglinreg(input[:,1:4], output, lam)
    ein = error(input[:,1:4], output, w)
    eout = error(testin[:,1:4], testout, w)

  numpy.set_printoptions(precision = 3)
  
  print 'Weight vector:', w
  print 'E_in for', digits[0], 'vs.', digits[1], 'classification with lambda =', lam, 'is:', '%.4f' % ein
  print 'E_out for', digits[0], 'vs.', digits[1], 'classification with lambda =', lam, 'is:', '%.4f' % eout
  
if __name__ == '__main__':
  main()
