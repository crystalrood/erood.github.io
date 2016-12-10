Title: Simple Random Sampling Of Rows
Slug: srs-of-rows
Summary: Simple Random Sampling Of Rows
Date: 2016-05-01 12:00
Category: R Stats
Tags: Basics
Authors: Chris Albon




```R
# create a dataframe with simulated values
x <- runif(1000)
y <- runif(1000)
z <- runif(1000)
a <- runif(1000)
df <- data.frame(x, y, z, a)
```


```R
# create a vector of weighs
w <- runif(1000)
```


```R
# sample 10 rows of the dataframe at pseudorandom, without replacement
sample <- df[sample(1:nrow(df), 10, replace = F),]
```


```R
sample
```




                 x         y          z           a
    500 0.44885287 0.7228785 0.11504159 0.054208551
    980 0.08392782 0.4568137 0.04393736 0.639204705
    445 0.48527409 0.9822628 0.37823768 0.410292231
    734 0.54769226 0.8992187 0.58030521 0.178938602
    177 0.43245083 0.9172805 0.02955689 0.743852472
    266 0.94394635 0.7638428 0.43960561 0.942814638
    256 0.77091541 0.2714964 0.49622060 0.009319224
    944 0.92682962 0.4278643 0.87805822 0.283003822
    492 0.84598479 0.7312344 0.02114653 0.366224907
    409 0.71072941 0.8280846 0.03118358 0.196112987




```R
# sample 10 rows of the dataframe at pseudorandom, without replacement, with the selection of reach row weighted by w (note w doesn't need to add up to 1)
sample.weighted <- df[sample(1:nrow(df), 10, replace = F, prob = w),]
```


```R
sample.weighted
```




                 x         y         z         a
    588 0.42359291 0.7747600 0.3443440 0.7502456
    417 0.23503932 0.2448383 0.8961582 0.2380380
    997 0.05755856 0.1587866 0.8144725 0.3183274
    789 0.46962589 0.5453313 0.3952169 0.5651571
    646 0.74493118 0.5151418 0.8717189 0.8330892
    231 0.60350137 0.2860977 0.8010951 0.7727321
    957 0.11192911 0.8962056 0.1051003 0.7203017
    947 0.38530976 0.7359524 0.1379156 0.7036205
    101 0.32523590 0.8928368 0.2648167 0.8808521
    208 0.84037450 0.8692373 0.5897262 0.2414655
