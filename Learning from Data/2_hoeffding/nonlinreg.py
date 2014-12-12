#!/usr/bin/python -tt

import numpy
#import matplotlib.pyplot as plot

def eval_target(points_eval):

  sign = numpy.sign(numpy.square(points_eval[:,0]) +
  numpy.square(points_eval[:,1]) - 0.6)
  
  return(sign)
  
def noise(y_nonoise):

  y_noise = numpy.asarray(y_nonoise)

  change_index = numpy.random.random_integers(0, len(y_noise)-1,
  size = int(0.1*len(y_noise)))
  
  y_noise[change_index] = -1.*y_noise[change_index]
  
  return(y_noise)
  
def generate_lindata(N_points):

  x = numpy.random.uniform(low = -1, high = 1, size = (N_points, 2))

  y_before = tuple(eval_target(x))
  
  #print y_before
  
  y = noise(y_before)
  
  #print y

  x_mod = numpy.insert(x, 0, 1., axis = 1)
  
  x_dagger = numpy.dot(numpy.linalg.inv(numpy.dot(x_mod.T, x_mod)), x_mod.T)
  
  w = numpy.dot(x_dagger, y)

  y_hypothesis = numpy.sign(numpy.dot(x_mod, w))

  return(x, y, y_hypothesis)  

def linreg(N_points):
  
  x, y, y_hypothesis = generate_lindata(N_points)
  
  #print y_hypothesis

  Error_in = sum(y_hypothesis != y)/float(N_points)

  #new_x = numpy.random.uniform(low = -1, high = 1, size = (10*N_points, 2))
  
  #new_x_mod = numpy.insert(new_x, 0, 1., axis = 1)

  #new_f = eval_target(m_target, b_target, new_x)

  #new_f_hypothesis = eval_target(m_est, b_est, new_x)

  #Error_out = sum(new_f != new_f_hypothesis)/(10.*N_points)
  
  #Error_out2 = sum(numpy.sign(numpy.dot(new_x_mod, w)) != new_f)/float(10.*N_points)

  return(Error_in)
  
def generate_nonlindata(N_points):

  x = numpy.random.uniform(low = -1, high = 1, size = (N_points, 2))

  nonlin_x = numpy.zeros((N_points, 6))
  
  nonlin_x[:,0] = numpy.ones(N_points)
  nonlin_x[:,1] = x[:,0]
  nonlin_x[:,2] = x[:,1]
  nonlin_x[:,3] = x[:,0]*x[:,1]
  nonlin_x[:,4] = numpy.square(x[:,0])
  nonlin_x[:,5] = numpy.square(x[:,1])

  #print x

  #print nonlin_x

  y_before = tuple(eval_target(x))
  
  #print y_before
  
  y = noise(y_before)
  
  #print y
  
  x_dagger = numpy.dot(numpy.linalg.inv(numpy.dot(nonlin_x.T, nonlin_x)),
  nonlin_x.T)
  
  w = numpy.dot(x_dagger, y)

  y_hypothesis = numpy.sign(numpy.dot(nonlin_x, w))

  return(nonlin_x, y, y_hypothesis, w)
  
def nonlinreg(N_points):

  x, y, y_hypothesis, w = generate_nonlindata(N_points)
  
  x1, y1, y1_hypothesis, w1 = generate_nonlindata(N_points)
  
  Error_in = sum(y_hypothesis != y)/float(N_points)
  
  Error_out = sum(numpy.sign(numpy.dot(x1, w)) != y1)/float(N_points)
  
  #print Error_out
  
  return(w, Error_in, Error_out)
  
def model_compare(w, N_points):

  input, output, output_noise, w_output = generate_nonlindata(N_points)
  
  model1 = numpy.array([-1., -.05, .08, .13, 1.5, 1.5])
  model2 = numpy.array([-1., -.05, .08, .13, 1.5, 15])
  model3 = numpy.array([-1., -.05, .08, .13, 15, 1.5])
  model4 = numpy.array([-1., -1.5, .08, .13, .05, .05])
  model5 = numpy.array([-1., -.05, .08, 1.5, .15, .15])

  frac1 = sum(numpy.sign(numpy.dot(input, model1)) !=
  numpy.sign(numpy.dot(input, w)))/float(N_points)

  frac2 = sum(numpy.sign(numpy.dot(input, model2)) !=
  numpy.sign(numpy.dot(input, w)))/float(N_points)

  frac3 = sum(numpy.sign(numpy.dot(input, model3)) !=
  numpy.sign(numpy.dot(input, w)))/float(N_points)

  frac4 = sum(numpy.sign(numpy.dot(input, model4)) !=
  numpy.sign(numpy.dot(input, w)))/float(N_points)

  frac5 = sum(numpy.sign(numpy.dot(input, model5)) !=
  numpy.sign(numpy.dot(input, w)))/float(N_points)

  return(frac1, frac2, frac3, frac4, frac5)

def main():

  N_x = 1000

  N_iter = 1000
  
  ein_lin = []
  
  ein_nonlin = []
  eout_nonlin = []
  
  w_nonlin = numpy.zeros((N_iter, 6))
  
  for k in range(0, N_iter):
    ein_lin.append(linreg(N_x))
    w_nonlint, ein_nonlint, eout_nonlint = nonlinreg(N_x)
    w_nonlin[k] = w_nonlint
    ein_nonlin.append(ein_nonlint)
    eout_nonlin.append(eout_nonlint)
  
  print 'For', N_iter, 'iterations and', N_x, 'points, average E_in for lin. reg. is', numpy.median(ein_lin)

  print 'For', N_iter, 'iterations and', N_x, 'points, average w for nonlin. reg is:'

  best_w = numpy.median(w_nonlin, axis = 0)

  print best_w
  
  f1, f2, f3, f4, f5 = model_compare(best_w, N_x)
  
  print 'Agreement with model 1:', f1
  print 'Agreement with model 2:', f2
  print 'Agreement with model 3:', f3
  print 'Agreement with model 4:', f4
  print 'Agreement with model 5:', f5
  
  print 'For', N_iter, 'iterations and', N_x, 'points, average E_in for nonlin. reg. is', numpy.median(ein_nonlin)
  print 'For', N_iter, 'iterations and', N_x, 'points, average E_out for nonlin. reg. is', numpy.median(eout_nonlin)


if __name__ == '__main__':
  main()
