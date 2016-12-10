Title: Pie Chart
Slug: pie-chart
Summary: Pie Chart
Date: 2016-05-01 12:00
Category: R Stats
Tags: Data Visualization
Authors: Chris Albon


Original source: http://www.statmethods.net/graphs/pie.html


```R
# Create some casualty numbers
slices <- c(4, 6, 1, 0, 0, 0, 5)
```


```R
# Create labels that correspond to the casualty numbers
lbls <- c("CrisisNET", "V3", "V2", "Crowdmap", "Ping", "SMSSync", "Other")
```


```R
# Create Percents For Each Slice
pct <- round(slices/sum(slices)*100)
```


```R
# Add Percents To Labels
lbls <- paste(lbls, pct)
```


```R
# Add The Percent Symbol To Labels
lbls <- paste(lbls,"%",sep="")
```


```R
# Create a pie chart with labels, with each slice colored by the terrain color pallete
pie(slices,labels = lbls, col=terrain.colors(length(lbls)), main="Main Ushahidi Blog Posts")
```


![png]({filename}/images/pie-chart_files/pie-chart_6_0.png)
