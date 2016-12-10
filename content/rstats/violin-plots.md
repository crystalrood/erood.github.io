Title: Violin Plots
Slug: violin-plots
Summary: Violin Plots
Date: 2016-05-01 12:00
Category: R Stats
Tags: Data Visualization
Authors: Chris Albon


Original Source: http://www.statmethods.net/graphs/boxplot.html


```R
# Load package
library(vioplot)
```

    Loading required package: sm
    Package 'sm', version 2.2-5.4: type help(sm) for summary information



```R
# Create some fake data about different types of casualties in a war
fpwar <- c(234,234,643,74,323,67,34,78,434)
wwi <- c(42,534,65,47,85,67,90,45,78)
wwii <- c(345,2,25,345,35,373,463,46,85)
```


```R
# Create a violin of the number of deaths
vioplot(fpwar, wwi, wwii, names=c("Franco-Prussian", "WWI", "WWII"), col="red3")
```


![png]({filename}/images/violin-plots_files/violin-plots_3_0.png)
