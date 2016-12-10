Title: Dot Plot (Wilkinson Plot)
Slug: dot-plot
Summary: Dot Plot (Wilkinson Plot)
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

# reset the graphing device
dev.off()
```




    null device
              1




```R
# create a subset of countries
countries2009 <- subset(countries, Year==2009 & healthexp>2000)
```


```R
# create the ggplot2 data
p <- ggplot(countries2009, aes(x = infmortality))
```


```R
# create the dotplot layer
p + geom_dotplot(binwidth=.25) +
  # rescale the y axis and remove tic marks
  scale_y_continuous(breaks=NULL) +
  # remove the axis labels
  theme(axis.title.y=element_blank())
```









![png]({filename}/images/dot-plot_files/dot-plot_4_1.png)
