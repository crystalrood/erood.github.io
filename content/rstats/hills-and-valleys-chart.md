Title: Hills And Valley Bar Chart
Slug: hills-and-valleys-chart
Summary: Hills And Valley Bar Chart
Date: 2016-05-01 12:00
Category: R Stats
Tags: Data Visualization
Authors: Chris Albon




```R
# load the ggplot2 package
library(ggplot2)

# load the gcookbook package
library(gcookbook)
```


```R
# create a subset of data from the Berkeley data and year after 1900
csub <- subset(climate, Source=="Berkeley" & Year >= 1900)
```


```R
# create a logical variable that says if the value is above or below 0
csub$pos <- csub$Anomaly10y >= 0
```


```R
# create a ggplot of Year and Temperature, visualuzed with a bar those filled by csub$pos
ggplot(csub, aes(x=Year, y=Anomaly10y, fill=pos)) +
  geom_bar(stat="identity", position="identity")
```









![png]({filename}/images/hills-and-valleys-chart_files/hills-and-valleys-chart_4_1.png)



```R
# same chart above but with more features defeind
ggplot(csub, aes(x=Year, y=Anomaly10y, fill=pos)) +
  geom_bar(stat="identity", position="identity", colour="black", size=0.25) + scale_fill_manual(values=c("#CCEEFF", "#FFDDDD"), guide=FALSE)
```









![png]({filename}/images/hills-and-valleys-chart_files/hills-and-valleys-chart_5_1.png)
