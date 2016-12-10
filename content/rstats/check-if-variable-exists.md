Title: Check To See If A Variable Exists
Slug: check-if-variable-exists
Summary: Check To See If A Variable Exists
Date: 2016-05-01 12:00
Category: R Stats
Tags: Basics
Authors: Chris Albon


original source: http://www.r-bloggers.com/check-if-a-variable-exists-in-r/


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
# does a variable called "x" exists in the object "data"?
"x" %in% names(data)
```




    [1] TRUE




```R
# does a column called "x" exists in the object "data"?
"x" %in% colnames(data)
```




    [1] TRUE
