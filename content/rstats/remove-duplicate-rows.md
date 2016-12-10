Title: Remove Duplicate Rows
Slug: remove-duplicate-rows
Summary: Remove Duplicate Rows
Date: 2016-05-01 12:00
Category: R Stats
Tags: Data Wrangling
Authors: Chris Albon


Original source: the r book


```R
# create a dataframe with simulated values
x <- c(1,2,3,1,2,2)
y <- c(1,6,3,1,2,2)
z <- c(1,2,3,1,2,2)
a <- c(1,5,6,1,2,2)
data <- data.frame(x, y, z, a)
rm(x, y, z, a)
```


```R
# find all the rows that are the same
duplicates <- data[duplicated(data),];duplicates
```




      x y z a
    4 1 1 1 1
    6 2 2 2 2




```R
# find all the rows that are unique
not.duplicates <- unique(data);not.duplicates
```




      x y z a
    1 1 1 1 1
    2 2 6 2 5
    3 3 3 3 6
    5 2 2 2 2
