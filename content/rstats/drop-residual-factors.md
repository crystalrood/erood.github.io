Title: Drop Residual Factors
Slug: drop-residual-factors
Summary: Drop Residual Factors
Date: 2016-05-01 12:00
Category: R Stats
Tags: Data Wrangling
Authors: Chris Albon



## create the problem


```R
# create a dataframe with a factor variable (state names)
df <- data.frame(states = state.name[1:5], score=seq(1:5))
```


```R
# drop two of the observations
subdf <- subset(df, score <= 3)
```


```R
# however, all the factors remain
levels(subdf$states)
```




    [1] "Alabama"    "Alaska"     "Arizona"    "Arkansas"   "California"



## the solution


```R
# run factor() to remake the factors correctly
subdf$states <- factor(subdf$states)
```


```R
# check to see it is correct
levels(subdf$states)
```




    [1] "Alabama" "Alaska"  "Arizona"
