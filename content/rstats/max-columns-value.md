Title: Find Which Column Has The Greatest Value In Each Row
Slug: max-columns-value
Summary: Find Which Column Has The Greatest Value In Each Row
Date: 2016-05-01 12:00
Category: R Stats
Tags: Data Wrangling
Authors: Chris Albon


Original source: the r book


```R
# create a dataframe with simulated values
x <- runif(50)
y <- runif(50)
z <- runif(50)
a <- runif(50)
df <- data.frame(x, y, z, a)
```


```R
# go through each row, and find the column index with the maximum value
max.col(df)
```




     [1] 1 2 4 4 2 1 3 2 2 3 3 2 2 3 3 3 2 2 3 2 3 3 2 2 2 1 4 1 3 4 2 3 4 3 2 4 4 1
    [39] 1 4 1 4 4 3 2 4 4 2 3 1




```R
# go through each row, and find the column index with the minimum value
max.col(-df)
```




     [1] 2 4 3 2 4 3 2 1 3 2 4 4 1 4 2 4 3 4 1 3 4 4 1 4 4 4 2 3 1 1 4 4 1 1 3 3 2 4
    [39] 4 3 3 3 2 2 4 2 2 3 1 4
