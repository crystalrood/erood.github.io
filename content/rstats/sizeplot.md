Title: Size Plot
Slug: sizeplot
Summary: Size Plot
Date: 2016-05-01 12:00
Category: R Stats
Tags: Data Visualization
Authors: Chris Albon


Original source: http://www.r-bloggers.com/using-r-coloured-sizeplot-with-ggplot2/


```R
# load the ggplot2 package
library(ggplot2)

# load the reshape2
library(reshape2)
```


```R
# create some simulated data
data <- data.frame(
  x=c(0, 0, 0, 0, 1, 1, 2, 2, 3, 3, 4, 4),
  y=c(0, 0, 0, 3, 1, 1, 1, 2, 2, 1, 4, 4),
  group=c(rep(1, 6), rep(2, 4), rep(3, 2)))
```


```R
# create a new object that "melts" the data so each row is a unique id-variable combination
counts <- melt(table(data[1:2]))
```


```R
# add column names
colnames(counts) <- c(colnames(data)[1:2], "count")
```


```R
# remove zeros
counts <- subset(counts, count != 0)
```


```R
# plot with the size of the dot being count
sizeplot <- qplot(x=x, y=y, size=count, data=counts) + scale_size(range=c(5, 10))
```


```R
# view the size plot
sizeplot
```









![png]({filename}/images/sizeplot_files/sizeplot_7_1.png)



```R
# create some factors
counts.and.groups <- merge(counts, unique(data))
```


```R
# create a sizeplot with color determined by a factor
sizeplot.colour <- qplot(
  x=x, y=y, size=count,
  colour=factor(group), data=counts.and.groups) +
  scale_size(range=c(5, 10))
```


```R
# view the plot
sizeplot.colour
```









![png]({filename}/images/sizeplot_files/sizeplot_10_1.png)



```R
dev.off()
```




    null device
              1
