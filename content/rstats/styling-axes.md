Title: Styling Axes
Slug: styling-axes
Summary: Styling Axes
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
```

## Swapping Axes


```R
# create the ggplot2 data
ggplot(PlantGrowth, aes(x=group, y=weight)) +
  # plot the boxplots
  geom_boxplot() +
  # swap the axes
  coord_flip()
```









![png]({filename}/images/styling-axes_files/styling-axes_3_1.png)



```R
# Reverse The Axis
ggplot(PlantGrowth, aes(x=group, y=weight)) +
  # plot the boxplots
  geom_boxplot() +
  # reverse the y-axis
  scale_y_reverse()
```









![png]({filename}/images/styling-axes_files/styling-axes_4_1.png)


## Set The Range Of An Axis


```R
# create the ggplot2 data
ggplot(PlantGrowth, aes(x=group, y=weight)) +
  # plot the boxplots
  geom_boxplot() +
  # set the y axis to range from 0 to 10
  scale_y_continuous(limits=c(0, 10))
```









![png]({filename}/images/styling-axes_files/styling-axes_6_1.png)


## Zoom In


```R
# create the ggplot2 data
ggplot(PlantGrowth, aes(x=group, y=weight)) +
  # plot the boxplots
  geom_boxplot() +
  # zoom in to the plot so the plot displays only between y=5 and y=6.5
  coord_cartesian(ylim = c(5, 6.5))
```









![png]({filename}/images/styling-axes_files/styling-axes_8_1.png)


## Rearrange The Display Ordering Of Categorical Data


```R
# create the ggplot2 data
ggplot(PlantGrowth, aes(x=group, y=weight)) +
  # plot the boxplots
  geom_boxplot() +
  # Display the three boxplots in a custom order
  scale_x_discrete(limits=c("trt1","ctrl","trt2"))
```









![png]({filename}/images/styling-axes_files/styling-axes_10_1.png)


## Set The Axis Tick Marks


```R
# create the ggplot2 data
ggplot(PlantGrowth, aes(x=group, y=weight)) +
  # plot the boxplots
  geom_boxplot() +
  # Set the tick marks at certain points
  scale_y_continuous(breaks=c(4, 4.25, 4.5, 5, 6, 8))
```









![png]({filename}/images/styling-axes_files/styling-axes_12_1.png)



```R
# create the ggplot2 data
ggplot(PlantGrowth, aes(x=group, y=weight)) +
  # plot the boxplots
  geom_boxplot() +
  # Remove the tick marks
  scale_y_continuous(breaks=NULL)
```









![png]({filename}/images/styling-axes_files/styling-axes_13_1.png)



```R
# create the ggplot2 data
ggplot(PlantGrowth, aes(x=group, y=weight)) +
  # plot the boxplots
  geom_boxplot() +
  # Set the tick marks at certain points
  scale_y_continuous(breaks=c(4, 4.25, 4.5, 5, 6, 8),
                    # set custom tick labels
                    labels=c("Super\nTiny", "Tiny", "Really\nshort", "Short", "Medium", "Tallish")) +
  scale_x_discrete(breaks=c("ctrl", "trt1", "trt2"),
                   # set custom tick labels
                   labels=c("Control", "Treatment 1", "Treatment 2")) +
                    # set the axis label angle
                    theme(axis.text.x = element_text(angle=30, hjust=1, vjust=1, family="Times", face="italic", colour="darkred"))
```









![png]({filename}/images/styling-axes_files/styling-axes_14_1.png)


## Set The Axis Labels


```R
# create the ggplot2 data
ggplot(PlantGrowth, aes(x=group, y=weight)) +
  # plot the boxplots
  geom_boxplot() +
  # write a custom xlab
  xlab("Age in years") +
  # wrote a custom ylab
  ylab("Height in inches")
```









![png]({filename}/images/styling-axes_files/styling-axes_16_1.png)


## Remove The Axis Labels


```R
# create the ggplot2 data
ggplot(PlantGrowth, aes(x=group, y=weight)) +
  # plot the boxplots
  geom_boxplot() +
  # remove the x label
  theme(axis.title.x=element_blank())
```









![png]({filename}/images/styling-axes_files/styling-axes_18_1.png)


## Style the Axis Label


```R
# create the ggplot2 data
ggplot(PlantGrowth, aes(x=group, y=weight)) +
  # plot the boxplots
  geom_boxplot() +
  # style the x axis
  theme(axis.title.x=element_text(face="italic", colour="darkred", size=14))
```









![png]({filename}/images/styling-axes_files/styling-axes_20_1.png)


## Drawing Axis Lines


```R
# create the ggplot2 data
ggplot(PlantGrowth, aes(x=group, y=weight)) +
  # plot the boxplots
  geom_boxplot() +
  # style whole plot as black and white
  theme_bw() +
  # draw axis line with a strong line and the x-y corner being a square
  theme(panel.border = element_blank(), axis.line = element_line(colour="black", size=2, lineend="square"))
```









![png]({filename}/images/styling-axes_files/styling-axes_22_1.png)
