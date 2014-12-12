#!/usr/bin/python -tt

import numpy
import matplotlib.pyplot as plot

def coin_flip(N_flip, N_coin, N_iter):

  nu_1 = []
  nu_rand = []
  nu_min = []

  for j in range(0, N_iter):

    results = numpy.zeros([N_flip, N_coin], dtype = numpy.int_)
    num_heads = numpy.empty(N_coin)
    num_heads[:] = numpy.nan
  
    for i in range(0, N_coin):
      results[:,i] = numpy.random.randint(0, 2, size = N_flip)
      num_heads[i] = N_flip - numpy.count_nonzero(results[:,i])
  
    c_1 = results[:,0]
    #print c_1
    #print num_heads[0]
    rand_index = numpy.random.randint(0, N_coin)
    #print rand_index
    c_rand = results[:,rand_index]
    #print c_rand
    #print num_heads[rand_index]
    min_index = numpy.argmin(num_heads)
    #print min_index
    c_min = results[:,min_index]
    #print c_min
    #print num_heads[min_index]
    
    frac_1 = num_heads[0]/N_flip
    frac_rand = num_heads[rand_index]/N_flip
    frac_min = num_heads[min_index]/N_flip
    
    #print frac_1
    #print frac_rand
    #print frac_min
    
    nu_1.append(frac_1)
    nu_rand.append(frac_rand)
    nu_min.append(frac_min)
    
  return(nu_1, nu_rand, nu_min)

def plot_hoeffding(dist, N_flip):

  N_bin = 50

  number, bin_edges = numpy.histogram(dist, N_bin)
  
  bin_mids = numpy.zeros(N_bin)
  
  for p in range(0, N_bin):
    bin_mids[p] = numpy.mean([bin_edges[p], bin_edges[p+1]])
  
  epsilon = abs(bin_mids - 0.5)

  epsilon_sub = epsilon[1:N_bin/2]
  
  epsilon_sub = numpy.append(epsilon_sub, 0.)
  
  num_gt_epsilon = numpy.zeros(N_bin/2)

  for k in range(0, N_bin/2):
    num_gt_epsilon[k] = sum(number[numpy.where(epsilon > epsilon_sub[k])])

  criteria = 2.*numpy.exp(-2.*numpy.square(epsilon_sub)*N_flip)

  plot.plot(epsilon_sub, num_gt_epsilon/100000., 'bo')
  plot.plot(epsilon_sub, criteria, 'r-')
  
  plot.show()


def main():

  N_flip = 10
  N_coin = 1000
  N_iter = 100000
  
  first, random, min = coin_flip(N_flip, N_coin, N_iter)

  print 'Average min is', numpy.mean(min)

  plot_hoeffding(first, N_flip)
  plot_hoeffding(random, N_flip)
  plot_hoeffding(min, N_flip)

if __name__ == '__main__':
  main()
