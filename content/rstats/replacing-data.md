Title: Replacing Data
Slug: replacing-data
Summary: Replacing Data
Date: 2016-05-01 12:00
Category: R Stats
Tags: Basics
Authors: Chris Albon




```R
# create simulated crime data of 20 observations
number.of.crimes <- runif(20)
```


```R
# replace the 10th and 11th value in number of crimes with 14 and 1, respectively
replace(number.of.crimes, c(10,11), c(14,1))
```




     [1]  0.76663091  0.90760481  0.17940086  0.73056629  0.10152773  0.79474331
     [7]  0.85948238  0.75014760  0.08862732 14.00000000  1.00000000  0.77783735
    [13]  0.34835337  0.97988156  0.06695829  0.47863876  0.48860696  0.19188663
    [19]  0.66221872  0.74794979
