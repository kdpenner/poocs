better = rep(0, 1000)

num_svm = rep(0, 1000)

library('LowRankQP')

for (m in 1:1000) {

i = 0

while (i == 0) {

  initdata = data.frame(x = runif(2, min = -1, max = 1),
  y = runif(2, min = -1, max = 1))

  target = lm(y ~ x, data = initdata)

  N_pts = 100

  newdata = data.frame(x0 = rep(1, N_pts),
  x = runif(N_pts, min = -1, max = 1),
  y = runif(N_pts, min = -1, max = 1))

  blah = predict(target, newdata = newdata)
  
#  separation = which(abs(newdata['y'] - blah) < 0.2)
  
#  while (is.finite(separation[1]) == TRUE) {
#  newdata = data.frame(x0 = rep(1, N_pts),
#  x = runif(N_pts, min = -1, max = 1),
#  y = runif(N_pts, min = -1, max = 1))
  
#  separation = which(abs(newdata['y'] - blah) < 0.2)
  
#  }

  blah = predict(target, newdata = newdata)

  yreturn = sign(newdata['y'] - blah)

  if (sum(yreturn == 1) == N_pts | sum(yreturn == -1) == N_pts) {i = 0}
  else {i = 1}
  
  }

weights = data.frame(w0 = 0, w1 = 0, w2 = 0)

ytest = sign(as.matrix(newdata) %*% t(as.matrix(weights)))

j = 0

while (sum(ytest != yreturn) != 0) {

  if (length(which(ytest != yreturn)) > 1)
  {index = sample(which(ytest != yreturn), 1)}
  else {index = which(ytest != yreturn)}

  weights = weights + yreturn[index,'y']*newdata[index,]
  
  ytest = sign(as.matrix(newdata) %*% t(as.matrix(weights)))
  
  j = j + 1
  
  }
  
eoutdata = data.frame(x0 = rep(1, 10000),
x = runif(10000, min = -1, max = 1),
y = runif(10000, min = -1, max = 1))

blah1 = predict(target, newdata = eoutdata)

eoutsign = sign(eoutdata['y'] - blah1)

eouttest = sign(as.matrix(eoutdata) %*% t(as.matrix(weights)))

disagree_pla = sum(eouttest != eoutsign)/10000.

# Dmat = yreturn*yreturn[1,'y']*(as.matrix(newdata[c('x','y')]) %*%
# as.matrix(t(newdata[1, c('x','y')])))

# for (k in 2:N_pts) {

#  Dmat = cbind(Dmat,
#  yreturn*yreturn[k,'y']*(as.matrix(newdata[c('x','y')]) %*%
#  as.matrix(t(newdata[k, c('x','y')]))))
 
#  }
 
Dmat1 = as.matrix(c(yreturn,yreturn)*newdata[c('x','y')]) %*%
t(as.matrix(c(yreturn,yreturn)*newdata[c('x','y')]))

# Dmat = as.matrix(Dmat)

dvec = as.matrix(rep(-1., N_pts))

Amat = as.matrix(t(yreturn))

bvec = 0.

uvec = as.matrix(rep(10000., N_pts))

sol = LowRankQP(Vmat = Dmat1, dvec = dvec, Amat = Amat, bvec = bvec, 
uvec = uvec, method = 'LU')

alpha = zapsmall(sol$alpha)

supportvectors = which(alpha != 0)

num_svm[m] = length(supportvectors)

t = data.frame(a1 = alpha[supportvectors,], a2 = alpha[supportvectors,])
yt = data.frame(y1 = yreturn[supportvectors,'y'], y2 = yreturn[supportvectors,'y'])
datat = data.frame(x1 = newdata[supportvectors,'x'], x2 = newdata[supportvectors,'y'])

svmwt = sapply(t*yt*datat, sum)

svmw = data.frame(w0 = 1./yreturn[supportvectors[1],'y']-
(as.matrix(newdata[supportvectors[1],c('x','y')]) %*% as.matrix(svmwt)),
w1 = svmwt['a1'], w2 = svmwt['a2'])

svmtest = sign(as.matrix(eoutdata) %*% t(as.matrix(svmw)))

disagree_svm = sum(svmtest != eoutsign)/10000.

if (disagree_svm < disagree_pla) {better[m] = 1}

}
