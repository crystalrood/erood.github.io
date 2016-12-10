Title: Converting Strings To Logical
Slug: strings-to-logical
Summary: Converting Strings To Logical
Date: 2016-05-01 12:00
Category: R Stats
Tags: Data Wrangling
Authors: Chris Albon




```R
# Create a string with Y and N string elements
answers <- c("Y", "Y", "N", "Y", "N")
```


```R
# write a function that converts "Y" to TRUE and "N" to FALSE
yn_to_logical <- function(x) {
  y <- rep.int(NA, length(x))
  y[x == "Y"] <- TRUE
  y[x == "N"] <- FALSE
  y
}
```


```R
# run the function on the data
yn_to_logical(answers)
```




    [1]  TRUE  TRUE FALSE  TRUE FALSE
