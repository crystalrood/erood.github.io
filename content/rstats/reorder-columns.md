Title: Reorder Columns
Slug: reorder-columns
Summary: Reorder Columns
Date: 2016-05-01 12:00
Category: R Stats
Tags: Data Wrangling
Authors: Chris Albon


Original source: http://stackoverflow.com/questions/5620885/how-does-one-reorder-columns-in-r


```R
# create some simulated data
df <- data.frame(1,2,3,4)
```


```R
df
```




      X1 X2 X3 X4
    1  1  2  3  4




```R
# move the third element to the second element's spot
df <- df[,c(1,3,2,4)]
```


```R
df
```




      X1 X3 X2 X4
    1  1  3  2  4
