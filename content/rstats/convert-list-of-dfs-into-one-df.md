Title: Converting List Of Dataframes Into A Single Dataframe
Slug: convert-list-of-dfs-into-one-df
Summary: Converting List Of Dataframes Into A Single Dataframe
Date: 2016-05-01 12:00
Category: R Stats
Tags: Data Wrangling
Authors: Chris Albon


original source: http://stackoverflow.com/questions/2851327/converting-a-list-of-data-frames-into-one-data-frame-in-r

Imagine we have two dataframes of numeric data contained within a single list, and  we want to combine that data by stacking them on top of each other as a single dataframe


```R
# create some simulated data
high <- data.frame(a = 1001:1005, b = 1006:1010)
low <- data.frame(a = 1:5, b = 6:10)
```


```R
# combine them into a list
df.list <- list(low, high)
```


```R
# rbind across every item of df.list and view it
df <- do.call("rbind", df.list);df
```




          a    b
    1     1    6
    2     2    7
    3     3    8
    4     4    9
    5     5   10
    6  1001 1006
    7  1002 1007
    8  1003 1008
    9  1004 1009
    10 1005 1010
