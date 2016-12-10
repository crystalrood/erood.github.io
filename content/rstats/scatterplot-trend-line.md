Title: Smooth A Scatterplot Trend Line
Slug: scatterplot-trend-line
Summary: Smooth A Scatterplot Trend Line
Date: 2016-05-01 12:00
Category: R Stats
Tags: Data Visualization
Authors: Chris Albon


Original source: ggplot2 book


```R
# load the ggplot2 library
library(ggplot2)

# set the seed so we can reproduce the results
set.seed(1410)
```


```R
# create a variable that is the first 100 rows of the diamonds dataset
dsmall <- diamonds[sample(nrow(diamonds), 100), ]
```


```R
# create a scatterplot with a smoothing line with a wiggly trend line
p1 <- qplot(carat, price, data = dsmall, geom = c("point", "smooth"), span = 0.2); p1
```

    geom_smooth: method="auto" and size of largest group is <1000, so using loess. Use 'method = x' to change the smoothing method.










![png]({filename}/images/scatterplot-trend-line_files/scatterplot-trend-line_3_2.png)



```R
# create a scatterplot with a smoothing line with a smooth trend line
p2 <- qplot(carat, price, data = dsmall, geom = c("point", "smooth"), span = 1); p2
```

    geom_smooth: method="auto" and size of largest group is <1000, so using loess. Use 'method = x' to change the smoothing method.










![png]({filename}/images/scatterplot-trend-line_files/scatterplot-trend-line_4_2.png)
