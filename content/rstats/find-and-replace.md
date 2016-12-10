Title: Find And Replace
Slug: find-and-replace
Summary: Find And Replace
Date: 2016-05-01 12:00
Category: R Stats
Tags: Basics
Authors: Chris Albon


Original source: http://christophergandrud.blogspot.com/2013/12/three-quick-and-simple-data-cleaning.html


```R
# load the DataCombine package
library(DataCombine)
```


```R
# create a dataframe of simulated values
data.df <- data.frame(cities = c("London, UK", "Oxford, UK", "Berlin, DE", "Hamburg, DE", "Oslo, NO"), score = c(8, 0.1, 3, 2, 1))
```


```R
# create a dataframe of two vectors, one with the characters to be replaced and the other with what to replace it with
replace.values <- data.frame(short = c("UK", "DE"), long = c("England", "Germany"))
```


```R
# find and replace the character strings
data.longnames.df <- FindReplace(data = data.df, Var = "cities", replaceData = replace.values, from = "short", to = "long"); data.longnames.df
```

    Only exact matches will be replaced.





           cities score
    1  London, UK   8.0
    2  Oxford, UK   0.1
    3  Berlin, DE   3.0
    4 Hamburg, DE   2.0
    5    Oslo, NO   1.0
