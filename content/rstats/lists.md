Title: Lists
Slug: lists
Summary: Lists
Date: 2016-05-01 12:00
Category: R Stats
Tags: Basics
Authors: Chris Albon



Lists are objects whose elements can be anything, from matrices to functions.


```R
# Create a numeric vector
x <- runif(50)
```


```R
# Create a character string vector
y <- state.name
```


```R
# Create a matrix
m <- matrix(c(3, 2, 4, 3), nrow= 2)
```


```R
# Create a list containing all of the above
l <- list(x, y, m)
```


```R
# You can name each element in a list
names(l) <- c("percent voted", "state", "vote matrix")
```
