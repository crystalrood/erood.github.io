Title: Split, Apply, Combine
Slug: split-apply-combine
Summary: Split, Apply, Combine
Date: 2016-05-01 12:00
Category: R Stats
Tags: Data Wrangling
Authors: Chris Albon


Original source: Learning R


```R
# generate fake data with multiple lines for a single observation
war.name <- c("WWII", "WWII", "WWI", "WWI", "Franco-Prussian", "Franco-Prussian", "Franco-Prussian", "Boer War", "Boer War", "Boer War")
deaths <- c(938, 9480, 2049, 1039, 3928, 9202, 10933, 40293, 10394, 20394)
casualties <- data.frame(war.name, deaths); casualties
```




              war.name deaths
    1             WWII    938
    2             WWII   9480
    3              WWI   2049
    4              WWI   1039
    5  Franco-Prussian   3928
    6  Franco-Prussian   9202
    7  Franco-Prussian  10933
    8         Boer War  40293
    9         Boer War  10394
    10        Boer War  20394



Using the split function we can calculate the average deaths for each war, even though they are split on different lines.


```R
## split the deaths by war.name
casualties.by.war <- with(casualties, split(deaths, war.name))
```


```R
## calculate the list mean war deaths for each war
list.of.means.by.war <- lapply(casualties.by.war, mean)
```


```R
# convert the list into a vector
mean.by.war <- unlist(list.of.means.by.war)
```
