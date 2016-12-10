Title: Replacing Factor Names Using Match
Slug: replacing-factor-names
Summary: Replacing Factor Names Using Match
Date: 2016-05-01 12:00
Category: R Stats
Tags: Data Wrangling
Authors: Chris Albon




```R
# create simulated factor names
district <- factor(c("NORTH", "NORTHWEST", "CENTRAL", "SOUTH", "SOUTHWEST", "WESTERN"))
```


```R
# for the levels of the Baltimore crime district variable, find instances where the names of the levels are WESTERN and replace with WEST
levels(district)[match("WESTERN",levels(district))] <- "WEST"
```

You can also do another way. Since every level in a factor can be identified by both a name (as done in the previous example) and a number.


```R
# view the levels of the district factor
levels(district)
```




    [1] "CENTRAL"   "NORTH"     "NORTHWEST" "SOUTH"     "SOUTHWEST" "WEST"     




```R
# replace the name of the third factor, NORTHEASTERN, with NORTHEAST
levels(district)[3] <- 'NORTHEAST'
```


```R
district
```




    [1] NORTH     NORTHEAST CENTRAL   SOUTH     SOUTHWEST WEST     
    Levels: CENTRAL NORTH NORTHEAST SOUTH SOUTHWEST WEST
