Title: Line Graph
Slug: line-graph
Summary: Line Graph
Date: 2016-05-01 12:00
Category: R Stats
Tags: Data Visualization
Authors: Chris Albon




```R
# load the ggplot2 package
library(ggplot2)
```


```R
# plot pressure vs. temperature with a line
ggplot(pressure, aes(x=temperature, y=pressure)) + geom_line() + geom_point()
```









![png]({filename}/images/line-graph_files/line-graph_2_1.png)
