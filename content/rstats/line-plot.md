Title: ggplot2  line plot
Slug: line-plot
Summary: ggplot2  line plot
Date: 2016-05-01 12:00
Category: R Stats
Tags: Data Visualization
Authors: Chris Albon


Original source: r graphics cookbook


```R
# load the ggplot2 library
library(ggplot2)

# load the gcookbook library
library(gcookbook)
```


```R
# create the ggplot2 data
ggplot(BOD, aes(x=Time, y=demand)) +
  # draw the line
  geom_line() +
  # expand the y axis to include 0
  expand_limits(y=0) +
  # add points
  geom_point()
```









![png]({filename}/images/line-plot_files/line-plot_2_1.png)


## Line plot with multiple lines


```R
# load plyr package
library(plyr)
```


```R
# summarize ToothGrowth
tg <- ddply(ToothGrowth, c("supp", "dose"), summarise, length=mean(len))
```


```R
# by assigning supp to color, we tell ggplot2 to draw these as two different lines
ggplot(tg, aes(x=dose, y=length, colour=supp)) +
  geom_line()
```









![png]({filename}/images/line-plot_files/line-plot_6_1.png)



```R
# map supp to linetype to draw two different lines (this line with different line types)
ggplot(tg, aes(x=dose, y=length, linetype=supp)) +
  geom_line()
```









![png]({filename}/images/line-plot_files/line-plot_7_1.png)



```R
# same as above, but this time since x is a factor, we have to specify to ggplot how to group the data
ggplot(tg, aes(x=factor(dose), y=length, colour=supp, group=supp)) +
  geom_line()
```









![png]({filename}/images/line-plot_files/line-plot_8_1.png)
