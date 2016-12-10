Title: Histogram
Slug: histogram
Summary: Histogram
Date: 2016-05-01 12:00
Category: R Stats
Tags: Data Visualization
Authors: Chris Albon




```R
# load the ggplot2 package
library(ggplot2)
```


```R
# hisotogram of the mpg variable from the mtcars dataset
ggplot(mtcars, aes(x=mpg)) + geom_histogram(binwidth=4)
```









![png]({filename}/images/histogram_files/histogram_2_1.png)
