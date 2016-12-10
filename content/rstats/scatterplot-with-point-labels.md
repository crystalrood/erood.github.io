Title: Scatterplot With Point's Labelled
Slug: scatterplot-with-point-labels
Summary: Scatterplot With Point's Labelled
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
# add a layer of point labels to the scatterplot, offset of .2 of the x axis
sps + geom_text(aes(x = ageYear + .2, label = sex))
```









![png]({filename}/images/scatterplot-with-point-labels_files/scatterplot-with-point-labels_3_1.png)
