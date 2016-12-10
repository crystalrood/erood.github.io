Title: Coloring Boxplot Outliers
Slug: color-boxplot-outliers
Summary: Coloring Boxplot Outliers
Date: 2016-05-01 12:00
Category: R Stats
Tags: Data Visualization
Authors: Chris Albon


original source: http://stackoverflow.com/questions/8499378/ggplot2-boxplot-how-do-i-match-the-outliers-color-to-fill-aesthetics


```R
# load the ggplot2 package
library(ggplot2)
```


```R
# create the ggplot2 data with color determined by Animation
m <- ggplot(movies, aes(y = votes, x = factor(round(rating)), colour = factor(Animation))) +
  # draw a boxplot without standard boxplot colors
  geom_boxplot(outlier.colour = NULL) +
  # draw a large y-scale
  scale_y_log10()
```


```R
m
```









![png]({filename}/images/color-boxplot-outliers_files/color-boxplot-outliers_3_1.png)
