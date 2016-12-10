Title: For Loops
Slug: for-loop
Summary: For Loops
Date: 2016-05-01 12:00
Category: R Stats
Tags: Basics
Authors: Chris Albon


Original source: the r book


```R
# create a dataframe with simulated values
x <- runif(1000)
y <- runif(1000)
z <- runif(1000)
a <- runif(1000)
data <- data.frame(x, y, z, a)
rm(x, y, z, a)
```


```R
# create a variable to place the results of the for loop in
data.altered <- NULL
```


```R
# for each element in data, square x and put the value in data.altered
for (i in data) {
  data.altered <- data$x^2
}
```
