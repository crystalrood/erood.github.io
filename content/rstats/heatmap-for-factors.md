Title: Heatmap For Factors
Slug: heatmap-for-factors
Summary: Heatmap For Factors
Date: 2016-05-01 12:00
Category: R Stats
Tags: Data Visualization
Authors: Chris Albon




```R
# download the data
nba <- read.csv("http://datasets.flowingdata.com/ppg2008.csv", sep=",")
```


```R
# order the data by the PTS variable
nba <- nba[order(nba$PTS),]
```


```R
# name each now by the Name variable
row.names(nba) <- nba$Name
```


```R
# drop the first column
nba <- nba[,2:20]
```


```R
# convert the data to a matrix for the heatmap
nba_matrix <- data.matrix(nba)
```


```R
# create a heatmap of nba_matrix with the columns colored by the heat.colors
nba_heatmap <- heatmap(nba_matrix, Rowv=NA, Colv=NA, col = heat.colors(256), scale="column", margins=c(5,10))
```


![png]({filename}/images/heatmap-for-factors_files/heatmap-for-factors_6_0.png)
