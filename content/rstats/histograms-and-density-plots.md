Title: Histograms and Density Plots
Slug: histograms-and-density-plots
Summary: Histograms and Density Plots
Date: 2016-05-01 12:00
Category: R Stats
Tags: Data Visualization
Authors: Chris Albon


Original source: ggplot2 book

Histograms and density plots show the distribution of a single variable across it's values


```R
# load the ggplot2 library
library(ggplot2)

# set the seed so we can reproduce the results
set.seed(1410)
```


```R
# plot a histogram
qplot(carat, data = diamonds, geom = "histogram")
```

    stat_bin: binwidth defaulted to range/30. Use 'binwidth = x' to adjust this.










![png]({filename}/images/histograms-and-density-plots_files/histograms-and-density-plots_2_2.png)



```R
# plot a histogram with more smoothness (by increasing bin size)
qplot(carat, data = diamonds, geom = "histogram", binwidth = 1)
```









![png]({filename}/images/histograms-and-density-plots_files/histograms-and-density-plots_3_1.png)



```R
# plot a density plot
qplot(carat, data = diamonds, geom = "density")
```









![png]({filename}/images/histograms-and-density-plots_files/histograms-and-density-plots_4_1.png)



```R
# plot a density plot with a smoother line
qplot(carat, data = diamonds, adjust = 4, geom = "density")
```









![png]({filename}/images/histograms-and-density-plots_files/histograms-and-density-plots_5_1.png)



```R
# plot a density plot with the color of the lines determined by the diamond's color (the "color" variable)
qplot(carat, data = diamonds, geom = "density", colour = color)
```









![png]({filename}/images/histograms-and-density-plots_files/histograms-and-density-plots_6_1.png)



```R
# plot a histogram plot with the color of the lines determined by the diamond's color (the "color" variable)
qplot(carat, data = diamonds, geom = "histogram", fill = color)
```

    stat_bin: binwidth defaulted to range/30. Use 'binwidth = x' to adjust this.










![png]({filename}/images/histograms-and-density-plots_files/histograms-and-density-plots_7_2.png)
