Title: Line Plot With Multiple Lines
Slug: line-plot-with-multiple-lines
Summary: Line Plot With Multiple Lines
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

# load plyr package
library(plyr)

# reset the graphing device
dev.off()
```




    null device
              1




```R
# summarize the ToothGrowth data
tg <- ddply(ToothGrowth, c("supp", "dose"), summarise, length=mean(len))
```


```R
# create a ggplot with lines colored by the tg$supp variable
ggplot(tg, aes(x=dose, y=length, colour=supp)) +
  geom_line()
```









![png]({filename}/images/line-plot-with-multiple-lines_files/line-plot-with-multiple-lines_3_1.png)



```R
# create a ggplot with line-types determined by the tg$supp variable
ggplot(tg, aes(x=dose, y=length, linetype=supp)) +
  geom_line()
```









![png]({filename}/images/line-plot-with-multiple-lines_files/line-plot-with-multiple-lines_4_1.png)
