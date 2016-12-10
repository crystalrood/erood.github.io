Title: Split, Apply, Recombine
Slug: split-apply-recombine
Summary: Split, Apply, Recombine
Date: 2016-05-01 12:00
Category: R Stats
Tags: Data Wrangling
Authors: Chris Albon




```R
# split up the data by gear number
data <- split(mtcars, mtcars$gear)
```


```R
# apply a function (in this case a linear model)
fits <- lapply(data, function(x) return(lm(x$mpg~x$disp)$coef))
```


```R
# recombine the function applied in the line aboove again
do.call(rbind, fits)
```




      (Intercept)      x$disp
    3    24.51557 -0.02577046
    4    39.56753 -0.12221268
    5    31.66095 -0.05077512
