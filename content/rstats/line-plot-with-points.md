Title: Plot With Both Lines And Poiints
Slug: line-plot-with-points
Summary: Plot With Both Lines And Poiints
Date: 2016-05-01 12:00
Category: R Stats
Tags: Data Visualization
Authors: Chris Albon




```R
# load the gcookbook package for the data
library(gcookbook)

# load the ggplot2 package
library(ggplot2)

# reset the graphing device
dev.off()
```




    null device
              1




```R
# create a plot with both lines and dots
ggplot(BOD, aes(x=Time, y=demand)) +
  geom_line() +
  geom_point()
```









![png]({filename}/images/line-plot-with-points_files/line-plot-with-points_2_1.png)
