Title: Boxplots
Slug: boxplots
Summary: Boxplots
Date: 2016-05-01 12:00
Category: R Stats
Tags: Data Visualization
Authors: Chris Albon


Original Source: http://www.statmethods.net/graphs/boxplot.html


```R
# Create some fake data about different types of casualties in a war
deaths <- c(234,234,643,74,323,67,34,78,434)
population <- factor(c("civilian", "soldier", "rebel"))
war <- cbind(deaths, population)
```


```R
# Create a boxplot of the number of deaths, seperated by populaton type, with teach boxplot labelled with the factor name, and colored different shades of red
boxplot(deaths~population,data=war, main="Deaths By Type", xlab="Type of Victims", ylab="Number Of Deaths", names=population, col=c("red3","indianred4","orangered1"))
```


![png]({filename}/images/boxplots_files/boxplots_2_0.png)
