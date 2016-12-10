Title: Faceting in ggplot2
Slug: faceting
Summary: Faceting in ggplot2
Date: 2016-05-01 12:00
Category: R Stats
Tags: Data Visualization
Authors: Chris Albon


Original source: ggplot2 book

Faceting is when we show many little charts, one for each category of a factor


```R
# load the ggplot2 library
library(ggplot2)

# set the seed so we can reproduce the results
set.seed(1410)
```


```R
# create a plot of x = carat and y = count, with a single chart for each category of diamond color
qplot(carat, data = diamonds, facets = color ~ ., geom = "histogram", binwidth = 0.1, xlim = c(0, 3))
```









![png]({filename}/images/faceting_files/faceting_2_1.png)
