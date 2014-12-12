library('e1071')

alpha = function (data, classify, cost) {

y = rep(0, length(data['digit']))
y[which(data['digit'] == classify)] = 1
y[which(data['digit'] != classify)] = -1

data1 = cbind(data, y)

fit = svm(x = data1[,c('symmetry', 'intensity')], y = data1[,'y'],
scale = F, type = 'C-classification', kernel = 'polynomial',
degree = 2, gamma = 1, coef0 = 1, cost = cost, cross = 10)

ind_b = which(abs(fit$coefs) < cost)
b = sign(fit$coefs[ind_b[1]])-sum(fit$coefs * (1 + fit$SV %*% fit$SV[ind_b[1],])^2)
g = sign(t(fit$coefs) %*% (1 + fit$SV %*%
t(as.matrix(data1[,c('symmetry','intensity')])))^2 + b)

g = -g

ein = length(which(g != data1[,'y']))/length(data1[,'y'])

return(ein)

}

data = read.table('features.train', header=T)
cost = .01

alpha(data, classify = 0, cost)
alpha(data, classify = 2, cost)
alpha(data, classify = 4, cost)
alpha(data, classify = 6, cost)
alpha(data, classify = 8, cost)

alpha(data, classify = 1, cost)
alpha(data, classify = 3, cost)
alpha(data, classify = 5, cost)
alpha(data, classify = 7, cost)
alpha(data, classify = 9, cost)

y = rep(0, length(data[,'digit']))
y[which(data[,'digit'] == 1)] = 1
y[which(data[,'digit'] == 5)] = -1
y[which(data[,'digit'] != 1 & data[,'digit'] != 5)] = NA

data2 = cbind(data, y)

data2 = na.omit(data2)

costs = c(.0001, .001, .01, .1, 1)

test = read.table('features.test', header=T)

yt = rep(0, length(test[,'digit']))
yt[which(test[,'digit'] == 1)] = 1
yt[which(test[,'digit'] == 5)] = -1
yt[which(test[,'digit'] != 1 & test[,'digit'] != 5)] = NA

test2 = cbind(test, yt)

test2 = na.omit(test2)

beta = function(train, test, cost, q) {

fit = svm(x = train[,c('symmetry', 'intensity')], y = train[,'y'],
scale = F, type = 'C-classification', kernel = 'polynomial',
degree = q, gamma = 1, coef0 = 1, cost = cost, cross = 10)

ind_b = which(abs(fit$coefs) < cost)
if (length(ind_b) == 0) {b = -fit$rho}
else {b = 1-sum(fit$coefs * (1 + fit$SV %*% fit$SV[ind_b[1],])^q)}
g = -sign(t(t(fit$coefs) %*% (1 + fit$SV %*%
t(as.matrix(train[,c('symmetry','intensity')])))^q) + b)

gout = -sign(t(t(fit$coefs) %*% (1 + fit$SV %*%
t(as.matrix(test[,c('symmetry','intensity')])))^q) + b)

ein = length(which(g != train[,'y']))/length(train[,'y'])
eout = length(which(gout != test[,'yt']))/length(test[,'yt'])

print(c(fit$tot.nSV, ein, eout))

}

for (i in 1:5) {beta(data2, test2, costs[i], 2)
beta(data2, test2, costs[i], 5)}

plot(data1$symmetry, data1$intensity, col=data1$y+2)

sym_hi = seq(.32, .7, .01)

int_hi = rep(0, length(sym_hi))

for (i in 1:length(sym_hi)) {
  blah = function(x) {
    t(fit$coefs) %*% (1+fit$SV %*%
    as.matrix(c(sym_hi[i], x)))^2 - fit$rho
    }
  int_hi[i] = uniroot(blah, lower=-2, upper = 0)$root
  }

sym_lo = seq(.32, .7, .01)

int_lo = rep(0, length(sym_lo))

for (i in 1:length(sym_lo)) {
  blah = function(x) {
    t(fit$coefs) %*% (1+fit$SV %*%
    as.matrix(c(sym_lo[i], x)))^2 - fit$rho
    }
  int_lo[i] = uniroot(blah, lower=-8, upper = -2)$root
  }

lines(sym_lo, int_lo, col='red')
lines(sym_hi, int_hi, col='red')

sym_new = seq(.1, .3, .01)
int_new = rep(0, length(sym_new))

for (i in 1:length(sym_new)) {
  blah = function(x) {
    t(fit$coefs) %*% (1+fit$SV %*%
    as.matrix(c(sym_new[i], x)))^2 - fit$rho
    }
  minval = optimize(blah, lower=-8, upper=0)$minimum
  maxval = optimize(blah, lower=-8, upper=0, maximum=T)$maximum
  int_new[i] = uniroot(blah, lower=minval, upper=maxval)$root
  }

ecv = array(dim = c(10,5,100))

for (i in 1:100) {

  data3 = data2[sample(nrow(data2)),]
  data3$group = as.numeric(cut(seq(1, nrow(data3)), 10))

  for (j in 1:10) {

    data4 = subset(data3, group != j)
    data5 = subset(data3, group == j)
    
    for (k in 1:5) {
    
      fit = svm(y ~ symmetry + intensity, data = data4,
      scale = F, type = 'C-classification', kernel = 'polynomial',
      degree = 2, gamma = 1, coef0 = 1, cost = costs[k])
      
      ecv[j,k,i] = sum(predict(fit, data5) != data5[,'y'])/nrow(data5)
      
      }
      
    }

}

ecv = colMeans(ecv, dims = 1)
select = rep(0,100)

for (i in 1:100) {select[i] = which.min(ecv[,i])}

costs = c(.01, 1, 100, 1e4, 1e6)

delta = function(train, test, cost) {

fit = svm(y ~ symmetry + intensity, data = train,
scale = F, type = 'C-classification', kernel = 'radial',
gamma = 1, cost = cost)

g = predict(fit, train)
gout = predict(fit, test)

ein = length(which(g != train[,'y']))/length(train[,'y'])
eout = length(which(gout != test[,'yt']))/length(test[,'yt'])

print(c(fit$tot.nSV, ein, eout))

}

for (i in 1:5) {delta(data2, test2, costs[i])}