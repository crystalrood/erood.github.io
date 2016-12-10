Title: Adding Levels To A Factor
Slug: add-levels-to-factors
Summary: Adding Levels To A Factor
Date: 2016-05-01 12:00
Category: R Stats
Tags: Basics
Authors: Chris Albon


```R
# create simulated distract name data
district <- c("NORTH", "NORTHWEST", "CENTRAL", "SOUTH", "SOUTHWEST", "EAST")

# remake district categories with the combination of district categories and a new SOUTH CENTRAL category
levels(district) <- c(district, "SOUTH CENTRAL")
```


```R
levels(district)
```




    [1] "NORTH"         "NORTHWEST"     "CENTRAL"       "SOUTH"        
    [5] "SOUTHWEST"     "EAST"          "SOUTH CENTRAL"
