Title: Selecting Data According To Patterns
Slug: select-data-according-to-patterns
Summary: Selecting Data According To Patterns
Date: 2016-05-01 12:00
Category: R Stats
Tags: Data Wrangling
Authors: Chris Albon




```R
# create simulated district names
district <- factor(c("NORTH", "NORTHWEST", "CENTRAL", "SOUTH", "SOUTHWEST", "WESTERN"))
```


```R
#Select all the cases where Baltimore's district name is "North"
district[grep("NORTH", as.character(district))]
```




    [1] NORTH     NORTHWEST
    Levels: CENTRAL NORTH NORTHWEST SOUTH SOUTHWEST WESTERN
