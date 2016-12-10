Title: Scatter Plot (Basic)
Slug: scatterplot
Summary: Scatter Plot (Basic)
Date: 2016-05-01 12:00
Category: R Stats
Tags: Data Visualization
Authors: Chris Albon




```R
# load the ggplot2 package
library(ggplot2)
```


```R
# plot using base graphics
plot(mtcars$wt, mtcars$mpg)
```


![png]({filename}/images/scatterplot_files/scatterplot_2_0.png)



```R
# plot using ggplot2
ggplot(mtcars, aes(x=wt, y=mpg)) + geom_point()
```









![png]({filename}/images/scatterplot_files/scatterplot_3_1.png)
