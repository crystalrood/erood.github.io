Title: Removing Observations In Data Frames With Missing Data
Slug: removing-missing-obs
Summary: Removing Observations In Data Frames With Missing Data
Date: 2016-05-01 12:00
Category: R Stats
Tags: Data Wrangling
Authors: Chris Albon




```R
# create a data frame of fake data
names <- c("Gob", "George Michael", "Michael", "Maebe", "Jake", "NA", "Taylor", "NA", "Jack")
score.1 <- c(4355, NA, 435345, 435435, 347754, 5754364, 34534543, 43534534, NA)
score.2 <- c(4355, 324, 435345, 435435, 347754, NA, NA, NA, 9230)
df <- data.frame(names, score.1, score.2)
```


```R
# index only the rows with no missing data
df[complete.cases(df),]
```




        names score.1 score.2
    1     Gob    4355    4355
    3 Michael  435345  435345
    4   Maebe  435435  435435
    5    Jake  347754  347754
