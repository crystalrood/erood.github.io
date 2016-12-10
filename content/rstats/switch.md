Title: Switch Function
Slug: switch
Summary: Switch Function
Date: 2016-05-01 12:00
Category: R Stats
Tags: Basics
Authors: Chris Albon


Original source: http://stackoverflow.com/questions/7825501/switch-statement-usage

The switch function is the same as having a bunch of if statements. It allows R to trigger between different actions based on an input.


```R
# create fake data
y <- runif(10)
```


```R
# Create a function that switches between different types of averages depending on the input. In this function "type" is input variable that the user enters to select which action is triggered.
avg <- function(x, type) {
  switch(type,
    mean = mean(x),
    median = median(x),
    trimmed = mean(x, trim = .2))
}
```


```R
# Trigger the function to calculate the mean
avg(y, "mean")
```




    [1] 0.6176063




```R
# Trigger the function to calculate the median
avg(y, "median")
```




    [1] 0.6356017




```R
# Trigger the function to calculate a trimmed mean
avg(y, "trimmed")
```




    [1] 0.6390694
