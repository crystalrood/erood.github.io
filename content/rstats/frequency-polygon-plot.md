Title: Frequency Polygon Plot
Slug: frequency-polygon-plot
Summary: Frequency Polygon Plot
Date: 2016-05-01 12:00
Category: R Stats
Tags: Data Visualization
Authors: Chris Albon


Original source: r graphics cookbook


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
# divide the faithful$waiting data into 10 bins
binsize <- diff(range(faithful$waiting))/10
```


```R
# create the ggplot2 data for the faithful$waiting variable
ggplot(faithful, aes(x=waiting)) +
  # add a sensity line
  geom_freqpoly(binwidth=binsize) +
  # zoom out the plot a little bit
  expand_limits(y=0)
```









![png]({filename}/images/frequency-polygon-plot_files/frequency-polygon-plot_3_1.png)
