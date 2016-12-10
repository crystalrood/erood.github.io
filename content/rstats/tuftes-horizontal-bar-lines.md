Title: Tufte's Horizontal Bar Lines
Slug: tuftes-horizontal-bar-lines
Summary: Tufte's Horizontal Bar Lines
Date: 2016-05-01 12:00
Category: R Stats
Tags: Data Visualization
Authors: Chris Albon


Original source: http://stackoverflow.com/questions/13701485/r-graphs-creating-tuftes-horizontal-bar-lines


```R
# load the ggplot2 package
library(ggplot2)    
```


```R
# create the ggplot2 data
ggplot(msleep, aes(x=order)) +
  # draw the bars
  stat_bin() +
  # draw the black and white theme
  theme_bw() +
  # draw white horizontal lines on the yintercept between 5 and 20, spaced every 5
  geom_hline(yintercept=seq(5, 20, 5), col="white")
```









![png]({filename}/images/tuftes-horizontal-bar-lines_files/tuftes-horizontal-bar-lines_2_1.png)
