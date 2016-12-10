Title: Calculate A Moving Average
Slug: calculate-moving-average
Summary: Calculate A Moving Average
Date: 2016-05-01 12:00
Category: R Stats
Tags: Basics
Authors: Chris Albon


original source: http://stackoverflow.com/questions/743812/calculating-moving-average-in-r


```R
# create some simulated data
x <- 1:10
```


```R
library(forecast)
```

    Warning message:
    : package ‘forecast’ was built under R version 3.1.3Loading required package: zoo

    Attaching package: ‘zoo’

    The following objects are masked from ‘package:base’:

        as.Date, as.Date.numeric

    Loading required package: timeDate
    This is forecast 5.9




```R
ma(x, order = 5, centre=TRUE)
```




     [1] NA NA  3  4  5  6  7  8 NA NA
