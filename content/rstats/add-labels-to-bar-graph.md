Title: Adding labels to a ggplot2 bar graph
Slug: add-labels-to-bar-graph
Summary: Adding labels to a ggplot2 bar graph
Date: 2016-05-01 12:00
Category: R Stats
Tags: Data Visualization
Authors: Chris Albon



original source: r graphics cookbook


```R
# load the ggplot2 package
library(ggplot2)

# load the gcookbook package
library(gcookbook)
```

## Below the top


```R
# create a ggplot data
ggplot(cabbage_exp, aes(x=interaction(Date, Cultivar), y=Weight)) +
  # draw the bar plot
  geom_bar(stat="identity") +
  # create the weight text above the bar in white
  geom_text(aes(label=Weight), vjust=1.5, colour="white")
```









![png]({filename}/images/add-labels-to-bar-graph_files/add-labels-to-bar-graph_3_1.png)


## Above the top


```R
# create a ggplot data
ggplot(cabbage_exp, aes(x=interaction(Date, Cultivar), y=Weight)) +
  # draw the bar plot
  geom_bar(stat="identity") +
  # create the weight text below the bar in white
  geom_text(aes(label=Weight), vjust=-0.2)
```









![png]({filename}/images/add-labels-to-bar-graph_files/add-labels-to-bar-graph_5_1.png)


# Labels on a grouped bar chart


```R
# create the ggplot data for a grouped bar chart
ggplot(cabbage_exp, aes(x=Date, y=Weight, fill=Cultivar)) +
  # plot the bars
  geom_bar(stat="identity", position="dodge") +
  # create the label, "dodged" to fit the bars
  geom_text(aes(label=Weight), vjust=1.5, colour="white",
            position=position_dodge(.9), size=3)

```

    ymax not defined: adjusting position using y instead










![png]({filename}/images/add-labels-to-bar-graph_files/add-labels-to-bar-graph_7_2.png)
