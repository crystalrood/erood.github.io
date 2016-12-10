Title: Bar Charts
Slug: bar-charts
Summary: Bar Charts
Date: 2016-05-01 12:00
Category: R Stats
Tags: Data Visualization
Authors: Chris Albon


original source: ggplot2 book

The bar geom counts the number of instances of each class so that you don’t need to tabulate your values beforehand


```R
# load the ggplot2 library
library(ggplot2)

# set the seed so we can reproduce the results
set.seed(1410)
```


```R
# plot the color
qplot(color, data = diamonds, geom = "bar")
```









![png]({filename}/images/bar-charts_files/bar-charts_3_1.png)
