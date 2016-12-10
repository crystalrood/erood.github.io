Title: Advanced Applying With Plyr
Slug: apply-with-plyr
Summary: Advanced Applying With Plyr
Date: 2016-05-01 12:00
Category: R Stats
Tags: Basics
Authors: Chris Albon



**The plyr package uses \*\*ply() functions, where the first star in the input and the second star is the output. For example, llplyr takes a list in and spits a list out.**


```R
# load the plyr package
library(plyr)
```


```R
#generate some fake list data
war.name <- c("WWII", "WWII", "WWI", "WWI", "Franco-Prussian", "Franco-Prussian", "Franco-Prussian", "Boer War", "Boer War", "Boer War")
deaths <- c(938, 9480, 2049, 1039, 3928, 9202, 10933, 40293, 10394, 20394)
allies <- c(9, 5, 4, 6, 3, 2, 4, 1, 2, 3)
casualties <- list(war.name, deaths, allies)
casualties.df <- data.frame(war.name, deaths, allies)
```


```R
# split up the list by casualties, find all the unique elements, output them as a list
llply(casualties, unique)
```




    [[1]]
    [1] "WWII"            "WWI"             "Franco-Prussian" "Boer War"       

    [[2]]
     [1]   938  9480  2049  1039  3928  9202 10933 40293 10394 20394

    [[3]]
    [1] 9 5 4 6 3 2 1




**r\*ply replaces replicate, with the \* denoting the output**


```R
# run runif(1) five times, outputting a data frame
rdply(5, runif(1))
```




      .n         V1
    1  1 0.09292281
    2  2 0.06861817
    3  3 0.04870200
    4  4 0.57864348
    5  5 0.21716079



**ddply replaces tapply, it inputs a data frame and outputs a data frame**


```R
# take the data frame casualties.df, split it up by war.name (for some reasons it uses the .() function, the find the mean)
ddply(
  casualties.df,
  .(war.name),
  colwise(mean)
)
```




             war.name   deaths allies
    1        Boer War 23693.67      2
    2 Franco-Prussian  8021.00      3
    3             WWI  1544.00      5
    4            WWII  5209.00      7
