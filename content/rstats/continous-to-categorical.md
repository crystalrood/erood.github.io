Title: Converting Continous Variables To Categorical Variables
Slug: continous-to-categorical
Summary: Converting Continous Variables To Categorical Variables
Date: 2016-05-01 12:00
Category: R Stats
Tags: Data Wrangling
Authors: Chris Albon


Original source: Learning R


```R
# Generate some age data of 10000 soldiers between 16 and 66
age <- 16 + 50 * rbeta(10000, 2, 3)
```


```R
# Use cut() to chunk up the observations into bins of 10 year block, the outcome is an ordered factor
grouped.ages <- ordered(cut(age, seq.int(16, 66, 10)))
```


```R
# view a table of the results
table(grouped.ages)
```




    grouped.ages
    (16,26] (26,36] (36,46] (46,56] (56,66]
       1817    3473    2898    1526     286




```R
# plot the results
plot(grouped.ages)
```


![png]({filename}/images/continous-to-categorical_files/continous-to-categorical_4_0.png)
