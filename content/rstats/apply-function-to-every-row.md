Title: Apply A Function On Every Row Of A Dataframe
Slug: apply-function-to-every-row
Summary: Apply A Function On Every Row Of A Dataframe
Date: 2016-05-01 12:00
Category: R Stats
Tags: Basics
Authors: Chris Albon


original source: http://stackoverflow.com/questions/2074606/doing-a-plyr-operation-on-every-row-of-a-data-frame-in-r


```R
# Load packages
library(plyr)
```


```R
# create a simulated dataframe
x <- rnorm(10)
y <- rnorm(10)
df <- data.frame(x,y)
```


```R
# array to dataframe apply, on df, for each row, apply transform() to create a variable called "max" whose values are the maximum value of x or y (whichever is higher).
adply(df, 1, transform, max = max(x, y))
```




                x          y        max
    1  -1.0286311  0.6621974  0.6621974
    2   0.5466022  0.2977963  0.5466022
    3  -0.6559125 -2.0830247 -0.6559125
    4  -1.6942847 -0.2205220 -0.2205220
    5   2.2678281 -0.4791234  2.2678281
    6  -1.6849528 -0.4873940 -0.4873940
    7   1.1627351  0.5137251  1.1627351
    8   1.4182618  0.9697840  1.4182618
    9   0.2025052 -0.3519337  0.2025052
    10 -0.7100003 -0.6827529 -0.6827529
