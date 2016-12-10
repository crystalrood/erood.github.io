Title: Indexing
Slug: indexing
Summary: Indexing
Date: 2016-05-01 12:00
Category: R Stats
Tags: Basics
Authors: Chris Albon



** How indexing is formatted:**

`variable[ row(s), column(s) ]`


```R
# Create a variables of five elements
x <- c(1, 4, 9, 16, 25)
y <- c(1, 4, 4, 36, 24)
m <- data.frame(x, y)
```


```R
# Select the first, third, and fifth elements
x[c(1,3,5)]
```




    [1]  1  9 25




```R
# Select of all EXCEPT the second and fourth elements
x[c(-2, -4)]
```




    [1]  1  9 25




```R
# Select of all EXCEPT the second and fourth elements
x[c(TRUE, FALSE, TRUE, FALSE, TRUE)]
```




    [1]  1  9 25




```R
# Select the entire first row of a matrix, array, or dataframe
m[1, ]
```




      x y
    1 1 1




```R
# Select an the entire first column of a matrix, array, or dataframe
m[, 1]
```




    [1]  1  4  9 16 25
