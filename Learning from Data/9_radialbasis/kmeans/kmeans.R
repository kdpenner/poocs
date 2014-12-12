distance = function(x, cen) {

  xs = do.call('rbind', replicate(length(cen[,1]), x, simplify = F))

  euclid = (xs - cen)^2

  return(rowSums(euclid))
  
  }

lloyd_cluster = function (input, centers) {

  membership = rep(0, length(input[,1]))
  dist_all = matrix(0, nrow = length(input[,1]), ncol = length(centers[,1]))

  for (i in 1:length(input[,1])) {

    dist_all[i,] = distance(input[i,1:2], centers[,1:2])
    
    membership[i] = which.min(dist_all[i,])
    
    }
  
  dist_mem = list(membership = membership, dists = dist_all)
    
  return(dist_mem)
  
  }

lloyd_centers = function(input, centers, K) {

  for (j in 1:K) {

    good = which(input$cluster == j)
    
    centers[j,1:2] = sapply(input[good,1:2], mean)
    
    }
    
  return(centers)
    
  }

k_centers = function(input, K) {

  centers = data.frame(cen1 = NaN, cen2 = NaN)

  while (sum(sapply(centers, is.nan)) != 0) {

    centers = data.frame(cen1 = runif(K, min=-1, max=1),
    cen2 = runif(K, min=-1, max=1))

    stop = 0

    while (stop == 0) {

      clusters = lloyd_cluster(input, centers)
  
      if (sum(clusters$membership != input$cluster) != 0) {
  
        input$cluster = clusters$membership
        centers = lloyd_centers(input, centers, K)

        if (sum(sapply(centers, is.nan)) != 0) {
    
          stop = stop + 1
      
          }
    
        }
    
      else if (sum(clusters$membership != input$cluster) == 0) {

        stop = stop + 1

        }
    
      }
      
    }

  cen_dist = list(centers = centers, membership = clusters$membership,
  dists = clusters$dists)
    
  return(cen_dist)

  }

ein9 = rep(0, 100)
ein12 = rep(0, 100)
eout9 = rep(0, 100)
eout12 = rep(0, 100)
einsvm = rep(0, 100)
eoutsvm = rep(0, 100)
num_margin = rep(0, 100)

library('e1071')

for (run in 1:100) {

  input = data.frame(x1 = runif(100, min=-1, max=1),
  x2 = runif(100, min=-1, max=1), cluster = rep(0, 100))

  input$fx = sign(input$x2 - input$x1 + .25*sin(pi*input$x1))

  K9 = 9
  K12 = 12
  
  cents_dists9 = k_centers(input, K9)
  cents_dists12 = k_centers(input, K12)

  norm9 = cents_dists9$dists
  norm12 = cents_dists12$dists

  gamma = 1.5

  phi9 = cbind(rep(1, length(input$x1)), exp(-gamma * norm9))
  phi12 = cbind(rep(1, length(input$x1)), exp(-gamma * norm12))

  weights9 = solve(t(phi9) %*% phi9) %*% t(phi9) %*% input$fx
  weights12 = solve(t(phi12) %*% phi12) %*% t(phi12) %*% input$fx
  
  hypo9 = sign(t(weights9) %*% t(phi9))
  hypo12 = sign(t(weights12) %*% t(phi12))
  
  ein9[run] = sum(hypo9 != input$fx)/length(input$fx)
  ein12[run] = sum(hypo12 != input$fx)/length(input$fx)
  
  fresh = data.frame(x1 = runif(10000, min=-1, max=1),
  x2 = runif(10000, min=-1, max=1))
  
  fresh$fx = sign(fresh$x2 - fresh$x1 + .25*sin(pi*fresh$x1))
  
  outnorm9 = lloyd_cluster(fresh, cents_dists9$centers)$dists
  outnorm12 = lloyd_cluster(fresh, cents_dists12$centers)$dists
  
  outphi9 = cbind(rep(1, length(fresh$x1)), exp(-gamma * outnorm9))
  outphi12 = cbind(rep(1, length(fresh$x1)), exp(-gamma * outnorm12))
  
  outhypo9 = sign(t(weights9) %*% t(outphi9))
  outhypo12 = sign(t(weights12) %*% t(outphi12))
  
  eout9[run] = sum(outhypo9 != fresh$fx)/length(fresh$fx)
  eout12[run] = sum(outhypo12 != fresh$fx)/length(fresh$fx)
  
  svmfit = svm(fx ~ x1 + x2, data = input,
  scale = F, type = 'C-classification', kernel = 'radial',
  gamma = gamma, cost = .Machine$double.xmax)

  svmhypo = predict(svmfit, input)
  svmouthypo = predict(svmfit, fresh)
  
  einsvm[run] = sum(svmhypo != input$fx)/length(input$fx)
  eoutsvm[run] = sum(svmouthypo != fresh$fx)/length(fresh$fx)
  
  num_margin[run] = sum(svmfit$coefs == .Machine$double.xmax)
  
  print(run)
  
  }

eing1 = rep(0, 100)
eing2 = rep(0, 100)
eoutg1 = rep(0, 100)
eoutg2 = rep(0, 100)

for (run in 1:100) {

  input = data.frame(x1 = runif(100, min=-1, max=1),
  x2 = runif(100, min=-1, max=1), cluster = rep(0, 100))

  input$fx = sign(input$x2 - input$x1 + .25*sin(pi*input$x1))

  K9 = 9
  
  cents_dists9 = k_centers(input, K9)

  norm9 = cents_dists9$dists

  gamma1 = 1.5
  gamma2 = 2

  phi1 = cbind(rep(1, length(input$x1)), exp(-gamma1 * norm9))
  phi2 = cbind(rep(1, length(input$x1)), exp(-gamma2 * norm9))

  weights1 = solve(t(phi1) %*% phi1) %*% t(phi1) %*% input$fx
  weights2 = solve(t(phi2) %*% phi2) %*% t(phi2) %*% input$fx
  
  hypo1 = sign(t(weights1) %*% t(phi1))
  hypo2 = sign(t(weights2) %*% t(phi2))
  
  eing1[run] = sum(hypo1 != input$fx)/length(input$fx)
  eing2[run] = sum(hypo2 != input$fx)/length(input$fx)
  
  fresh = data.frame(x1 = runif(10000, min=-1, max=1),
  x2 = runif(10000, min=-1, max=1))
  
  fresh$fx = sign(fresh$x2 - fresh$x1 + .25*sin(pi*fresh$x1))
  
  outnorm9 = lloyd_cluster(fresh, cents_dists9$centers)$dists
  
  outphi1 = cbind(rep(1, length(fresh$x1)), exp(-gamma1 * outnorm9))
  outphi2 = cbind(rep(1, length(fresh$x1)), exp(-gamma2 * outnorm9))
  
  outhypo1 = sign(t(weights1) %*% t(outphi1))
  outhypo2 = sign(t(weights2) %*% t(outphi2))
  
  eoutg1[run] = sum(outhypo1 != fresh$fx)/length(fresh$fx)
  eoutg2[run] = sum(outhypo2 != fresh$fx)/length(fresh$fx)
  
  print(run)
  
  }
  
g1 = seq(-1, 1, .1)
g2 = seq(-1, 1, .1)
grid = expand.grid(x = g1, y = g2)
grid$z = rep(0, 21*21)

for (p in 1:(21*21)) {grid$z[p] = t(weights9) %*% c(1, exp(-gamma *
distance(grid[p,1:2], cents_dists9$centers[,1:2])))}

plot(x = input$x1, y = input$x2, col = input$fx + 2)
points(cents_dists9$centers, cex = 2, col = 'red')
contour(x = g1, y = g2, z = matrix(grid$z, 21, 21), level = 0, add = T)
