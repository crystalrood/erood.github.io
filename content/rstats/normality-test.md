Title: Normality Test
Slug: normality-test
Summary: Normality Test
Date: 2016-05-01 12:00
Category: R Stats
Tags: Other
Authors: Chris Albon



One simple test for normality is a quantile-quantile plot. It plots the sample's quantiles against a set of quantiles taken from a normal distribution.

If the points follow the line drawn, they are roughly normally distributed. If the points create a S-shape or other shape, they are not normally distributed


```R
# create simulated data that is not normal
y <- runif(1000)
```


```R
# create simulated data that is normal
y.norm <- rnorm(1000)
```


```R
# create a qq-plot for the non-normal data
qqnorm(y)
qqline(y,lty=2)
```


![png]({filename}/images/normality-test_files/normality-test_3_0.png)



![png]({filename}/images/normality-test_files/normality-test_3_1.png)



```R
# create a qq-plot for the normal data
qqnorm(y.norm)
qqline(y.norm,lty=2)
```


![png]({filename}/images/normality-test_files/normality-test_4_0.png)



![png]({filename}/images/normality-test_files/normality-test_4_1.png)


## Shapiro test

The null hypothesis is that the data is normally distributed. We want a large p-value, meaning that we cannot reject the null hypothesis (that the data is normally distributed)


```R
# shapiro test on non-normal data (results show that we can reject the null that the data is normally distributed)
shapiro.test(y)
```





    	Shapiro-Wilk normality test

    data:  y
    W = 0.9538, p-value < 2.2e-16





```R
# shapiro test on normal data (results show that we cannot reject the null hypothesis that the data is normally distributed)
shapiro.test(y.norm)
```





    	Shapiro-Wilk normality test

    data:  y.norm
    W = 0.9981, p-value = 0.3256
