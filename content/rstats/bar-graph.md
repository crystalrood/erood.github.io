Title: Bar Graph
Slug: bar-graph
Summary: Bar Graph
Date: 2016-05-01 12:00
Category: R Stats
Tags: Data Visualization
Authors: Chris Albon




```R
# load the ggplot2 library
library(ggplot2)
```


```R
# plot BOD$Time and BOD$demand
qplot(BOD$Time, BOD$demand, geom="bar", stat="identity")
```









![png]({filename}/images/bar-graph_files/bar-graph_2_1.png)



```R
# Convert the x variable to a factor, so that it is treated as discrete
qplot(factor(BOD$Time), BOD$demand, geom="bar", stat="identity")
```









![png]({filename}/images/bar-graph_files/bar-graph_3_1.png)
