Title: Basic Math Functions In R
Slug: arithmetic
Summary: Basic Math Functions In R
Date: 2016-05-01 12:00
Category: R Stats
Tags: Basics
Authors: Chris Albon



**Arithmetic operators**


```R
# 1 plus 1
1 + 1
```




    [1] 2




```R
# 4 minus 3
4 - 3
```




    [1] 1




```R
# 14 divided by 10
14 / 10
```




    [1] 1.4




```R
# 10 multiplied by 5
10*5
```




    [1] 50




```R
# 3 squared
3^2
```




    [1] 9




```R
# 5 mod 2
5%%2
```




    [1] 1




```R
# 4 divided by 2 (integer division)
4%/%2
```




    [1] 2




```R
# log to the base e of 2
log(2)
```




    [1] 0.6931472




```R
# antilog of 2
exp(2)
```




    [1] 7.389056




```R
# log to base 2 of 3
log(3,2)
```




    [1] 1.584963




```R
# log to base 10 of 2
log10(2)
```




    [1] 0.30103




```R
# square root of 2
sqrt(2)
```




    [1] 1.414214




```R
# !5
factorial(4)
```




    [1] 24




```R
# largest interger smaller than 2
floor(2)
```




    [1] 2




```R
# smallest integer greater than 6
ceiling(6)
```




    [1] 6




```R
# round 3.14159 to three digits
round(3.14159, digits=3)
```




    [1] 3.142




```R
# create 10 random digits between zero and 1 (from a uniform distribution)
runif(10)
```




     [1] 0.07613962 0.66543266 0.48379168 0.40593920 0.67715428 0.49170373
     [7] 0.62351598 0.19275859 0.48018351 0.34890640




```R
# cosine of 3
cos(3)
```




    [1] -0.9899925




```R
# sine of 3
sin(3)
```




    [1] 0.14112




```R
# tangent of 3
tan(3)
```




    [1] -0.1425465




```R
# absolute value of -3
abs(-3)
```




    [1] 3
