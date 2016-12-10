Title: Change The Barplot Bar Width
Slug: change-barplot-bar-width
Summary: Change The Barplot Bar Width
Date: 2016-05-01 12:00
Category: R Stats
Tags: Data Visualization
Authors: Chris Albon




```R
# load the gcookbook package for the data
library(gcookbook)

# load the ggplot2 package
library(ggplot2)
```


```R
# plot a default barplot
ggplot(pg_mean, aes(x=group, y=weight)) + geom_bar(stat="identity")
```









![png]({filename}/images/change-barplot-bar-width_files/change-barplot-bar-width_2_1.png)



```R
# plot a barplot with skinny bars
ggplot(pg_mean, aes(x=group, y=weight)) + geom_bar(stat="identity", width=0.5)
```









![png]({filename}/images/change-barplot-bar-width_files/change-barplot-bar-width_3_1.png)



```R
# plot a barplot with thick bars
ggplot(pg_mean, aes(x=group, y=weight)) + geom_bar(stat="identity", width=1)
```









![png]({filename}/images/change-barplot-bar-width_files/change-barplot-bar-width_4_1.png)
