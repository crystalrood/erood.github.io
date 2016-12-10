Title: Sorting A Data Frame By A Single Column
Slug: sort-dataframe-by-columns
Summary: Sorting A Data Frame By A Single Column
Date: 2016-05-01 12:00
Category: R Stats
Tags: Data Wrangling
Authors: Chris Albon


Original source: http://onertipaday.blogspot.com/2007/08/sortingordering-dataframe-according.html


```R
# Create three vectors of data
x = rnorm(20)
y = sample(rep(1:2, each = 10))
z = sample(rep(1:4, 5))
```


```R
# Create a dataframe containing those vectors
data.df <- data.frame(x, y, z)
```


```R
# Sort the entire dataframe by column y, then by column z
sort.by <- c("y", "z")
data.df.sorted = data.df[do.call(order, data.df[sort.by]), ]
```


```R
# View the sorted data frame
print(data.df.sorted)
```

                x y z
    2   0.6573883 1 1
    7   0.7038443 1 1
    5  -0.8647954 1 2
    17  0.6415467 1 2
    20 -2.0368409 1 2
    16 -0.1966456 1 3
    18 -0.1435698 1 3
    19  1.7946029 1 3
    9   0.4068842 1 4
    11 -1.4022449 1 4
    3  -0.3688571 2 1
    4  -1.6158611 2 1
    14 -0.4293812 2 1
    1  -0.2070859 2 2
    13 -0.8712713 2 2
    6   0.4727199 2 3
    10 -0.7866490 2 3
    8   0.3843080 2 4
    12  0.7966665 2 4
    15  1.4994587 2 4
