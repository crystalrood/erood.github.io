Title: Line and Path Plots
Slug: line-and-path-plots
Summary: Line and Path Plots
Date: 2016-05-01 12:00
Category: R Stats
Tags: Data Visualization
Authors: Chris Albon


Original source: ggplot2 book

Line plots is a path plot sorted by the x value


```R
# load the ggplot2 library
library(ggplot2)

# set the seed so we can reproduce the results
set.seed(1410)
```


```R
# plot a line plot with the date on the x axis and unemployment rate
qplot(date, unemploy / pop, data = economics, geom = "line")
```









![png]({filename}/images/line-and-path-plots_files/line-and-path-plots_3_1.png)



```R
# plot a line plot with the date being the x axis and the avg number of weeks unemployed on the y axis
qplot(date, uempmed, data = economics, geom = "line")
```









![png]({filename}/images/line-and-path-plots_files/line-and-path-plots_4_1.png)
