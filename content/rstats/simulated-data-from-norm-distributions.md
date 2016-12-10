Title: Simulated Data From Normal Distribution Function
Slug: simulated-data-from-norm-distributions
Summary: Simulated Data From Normal Distribution Function
Date: 2016-05-01 12:00
Category: R Stats
Tags: Other
Authors: Chris Albon


Original source: http://rforpublichealth.blogspot.com/2013/02/normal-distribution-functions.html


```R
# set seed to 3000 for reproducability
set.seed(3000)
```


```R
# create a sequence from 04 to 4 in increments of 0.01
xseq<-seq(-4,4,.01)
```


```R
# create a probability density function of xseq, with mean 0 and an standard deviation of 1
densities<-dnorm(xseq, 0,1)
```


```R
# create a cumative distribution function of xseq with mean 0 and a SD of 1
cumulative<-pnorm(xseq, 0, 1)
```


```R
# create 1000 random numbers from a normal distribution with mean 0 and an sd of 1
randomdeviates<-rnorm(1000,0,1)
```


```R
# create a grid to hold all the plots
par(mfrow=c(1,3), mar=c(3,4,4,2))
```


```R
# make the first plot
plot(xseq, densities, col="darkgreen",xlab="", ylab="Density", type="l",lwd=2, cex=2, main="PDF of Standard Normal", cex.axis=.8)
```


![png]({filename}/images/simulated-data-from-norm-distributions_files/simulated-data-from-norm-distributions_7_0.png)



```R
# make the second plot
plot(xseq, cumulative, col="darkorange", xlab="", ylab="Cumulative Probability",type="l",lwd=2, cex=2, main="CDF of Standard Normal", cex.axis=.8)
```


![png]({filename}/images/simulated-data-from-norm-distributions_files/simulated-data-from-norm-distributions_8_0.png)



```R
# make the third plot
hist(randomdeviates, main="Random draws from Std Normal", cex.axis=.8, xlim=c(-4,4))
```


![png]({filename}/images/simulated-data-from-norm-distributions_files/simulated-data-from-norm-distributions_9_0.png)
