Title: Expand A Table Of Counts Into A Dataframe
Slug: expand-counts-into-dataframe
Summary: Expand A Table Of Counts Into A Dataframe
Date: 2016-05-01 12:00
Category: R Stats
Tags: Data Wrangling
Authors: Chris Albon


Original source: The R Book


```R
# create a dataframe of simulated values
count <- c(2, 3, 4, 1)
sex <- c("male", "female", "male", "female")
nationality <- c("USA", "USA", "UK", "UK")
data.df <- data.frame(count, sex, nationality)
rm(count, sex, nationality)
```


```R
# apply a function that repeats a row the number of times it appears in data.df$count
data.expand <- lapply(data.df,function(x)rep(x, data.df$count))
```


```R
# convert it to a data frame
data.expand.df <- as.data.frame(data.expand)
```


```R
# remove the no-longer-needed count column
data.expand.df <- data.expand.df[,-1]; data.expand.df
```




          sex nationality
    1    male         USA
    2    male         USA
    3  female         USA
    4  female         USA
    5  female         USA
    6    male          UK
    7    male          UK
    8    male          UK
    9    male          UK
    10 female          UK
