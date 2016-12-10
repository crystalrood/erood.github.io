Title: Element Names
Slug: element-names
Summary: Element Names
Date: 2016-05-01 12:00
Category: R Stats
Tags: Basics
Authors: Chris Albon



Each element in a vector can have a name assigned to it


```R
# Create a vector with names for values
percent.sms <- c(high = 94, low = 23, 50)
```


```R
# List names of a vector
names(percent.sms)
```




    [1] "high" "low"  ""    
