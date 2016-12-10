Title: Select Rows By Logical Test
Slug: select-rows-by-logical-test
Summary: Select Rows By Logical Test
Date: 2016-05-01 12:00
Category: R Stats
Tags: Data Wrangling
Authors: Chris Albon


Original source: the r book


```R
# create a dataframe with simulated values
x <- runif(10)
y <- runif(10)
z <- runif(10)
a <- runif(10)
data <- data.frame(x, y, z, a)
rm(x, y, z, a)
```


```R
# select all rows where y is greater than x
data[data$y > data$x,]
```




              x         y          z         a
    2 0.3617916 0.5513793 0.73714905 0.8678027
    3 0.4121965 0.8947345 0.00735662 0.3614312
    6 0.7360850 0.8569630 0.97564971 0.6338547
    8 0.2491201 0.3543410 0.41584055 0.5313946
    9 0.1619093 0.6615272 0.51492096 0.9567799




```R
# select all rows where y IS NOT greater than x
data[!(data$y > data$x),]
```




               x         y         z          a
    1  0.8097187 0.4683501 0.9130371 0.18605450
    4  0.8210452 0.2808778 0.1992804 0.03930297
    5  0.2189346 0.1651140 0.2851813 0.64965427
    7  0.6266258 0.2833319 0.7272680 0.92645638
    10 0.8173277 0.3407574 0.7902216 0.11055400
