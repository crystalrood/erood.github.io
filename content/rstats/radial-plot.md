Title: Radial Plot
Slug: radial-plot
Summary: Radial Plot
Date: 2016-05-01 12:00
Category: R Stats
Tags: Data Visualization
Authors: Chris Albon


Inspiration: http://onertipaday.blogspot.com/2009/01/radar-chart.html


```R
# Load the plotrix library
library(plotrix)
```


```R
# Create a vector with the number of objects to be plotted
country <- c(1:8)
```


```R
# Create a vector of country names for the labels of the vector above
country.names <- names(country) <- c( "Yemen", "Spain", "Russia", "Portugal", "Italy", "Kenya", "USA", "Iceland")
```


```R
# Create a vector of the data to be plotted
country <- c(324, 234, 123, 63, 234, 423, 324, 452)
```


```R
# Set the font size on the radial plot
par(ps=12)
```


```R
# Create a radial plot
radial.plot(country, labels=country.names,rp.type="p",main="Radar Chart", radial.lim=c(0,500),line.col="blue")
```


![png]({filename}/images/radial-plot_files/radial-plot_6_0.png)
