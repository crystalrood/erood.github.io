Title: Conditional execution
Slug: conditional
Summary: Conditional execution
Date: 2016-05-01 12:00
Category: R Stats
Tags: Basics
Authors: Chris Albon




```R
# Make some data
my.age <- 20
our.ages <- cbind(20,30,40)
```


```R
# Sometimes we might only want R to do one thing under certain conditions and another thing under other conditions. Conditional execution let's us do that.
if (my.age < 30) { # if my.age is greater than 30
  under.30 <- TRUE # then set under.30 as TRUE
} else { # if my.age is not greater than 30
  under.30 <- FALSE # then set under.30 as FALSE
} # close this conditional execution
under.30 # display under.30
```




    [1] TRUE




```R
# If we want to run a conditional execution on all values in a vector, we can use the ifelse function
old.or.young <- ifelse(our.ages < mean(our.ages), "OLDER", "YOUNGER") # create an object old.or.young and add to label a value as older if the age of someone in our.age is older than the average (mean) age of the vector and "younger" if they are younger than the average age.
```


```R
old.or.young # display old.or.young
```




         [,1]    [,2]      [,3]     
    [1,] "OLDER" "YOUNGER" "YOUNGER"
