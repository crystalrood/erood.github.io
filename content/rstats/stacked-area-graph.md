Title: Stacked Area Graph In ggplot2
Slug: stacked-area-graph
Summary: Stacked Area Graph In ggplot2
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

# load the plyr library
library(plyr)
```


```R
# create the ggplot2 data, using Year and thousands (of people) and filled by age group.
ggplot(uspopage, aes(x=Year, y=Thousands, fill=AgeGroup)) +
  # add a area plot layer
  geom_area() +
  # change the colors and reserve the legend order (to match to stacking order)
  scale_fill_brewer(palette="Blues", breaks=rev(levels(uspopage$AgeGroup)))
```









![png]({filename}/images/stacked-area-graph_files/stacked-area-graph_2_1.png)


To reverse the stacking order we use plyr's desc() (decsending order) function


```R
# create the reversed stack ggplot2 data, using Year and thousands (of people) and filled by age group, grouped by reserve agegroup
ggplot(uspopage, aes(x=Year, y=Thousands, fill=AgeGroup, order=desc(AgeGroup))) +
  # add a area plot layer
  geom_area() +
  # change the colors and reserve the legend order (to match to stacking order)
  scale_fill_brewer(palette="Blues", breaks=levels(uspopage$AgeGroup))
```









![png]({filename}/images/stacked-area-graph_files/stacked-area-graph_4_1.png)
