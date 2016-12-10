Title: Scatterplot With Trend Line
Slug: scatterplot-with-trendline
Summary: Scatterplot With Trend Line
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
# create the scatterplot
sps <- ggplot(heightweight, aes(x = ageYear, y = heightIn, colour = sex)) +
  geom_point() +
  scale_colour_brewer(palette = "Set1")
```


```R
# create a scatterplot with loess smoothing
sps + geom_smooth()
```

    geom_smooth: method="auto" and size of largest group is <1000, so using loess. Use 'method = x' to change the smoothing method.










![png]({filename}/images/scatterplot-with-trendline_files/scatterplot-with-trendline_3_2.png)



```R
# create a scatterplot with lm (straight line) trend line
sps + geom_smooth(method=lm, se=FALSE, fullrange=TRUE)
```









![png]({filename}/images/scatterplot-with-trendline_files/scatterplot-with-trendline_4_1.png)
