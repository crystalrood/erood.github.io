Title: Proportional Stacked Bar Graph
Slug: proportional-stacked-bar-graph
Summary: Proportional Stacked Bar Graph
Date: 2016-05-01 12:00
Category: R Stats
Tags: Data Visualization
Authors: Chris Albon


Original source: r graphics cookbook


```R
# load the ggplot2 package
library(ggplot2)

# load the gcookbook package
library(gcookbook)

# load the plyr package
library(plyr)
```


```R
# do dataframe to dataframe apply. split up cabbage_exp by "Date" (there are three dates), and create a new variable which is percent_weight
ce <- ddply(cabbage_exp, "Date", transform, percent_weight = Weight / sum(Weight) * 100)
```


```R
# create a ggplot data object of date, percent_weight, and filled by cultivar
ggplot(ce, aes(x=Date, y=percent_weight, fill=Cultivar)) +
  # plot the bars that are black
  geom_bar(stat="identity", colour="black") +
  # reserve the legend so it matches the colors
  guides(fill=guide_legend(reverse=TRUE)) +
  # fill with the pastel1 color palette
  scale_fill_brewer(palette="Pastel1")
```









![png]({filename}/images/proportional-stacked-bar-graph_files/proportional-stacked-bar-graph_3_1.png)
