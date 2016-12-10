Title: Rounding Numbers
Slug: rounding
Summary: Rounding Numbers
Date: 2016-05-01 12:00
Category: R Stats
Tags: Basics
Authors: Chris Albon




```R
# round up to the nearest integer
ceiling(3.14159)
```




    [1] 4




```R
# round down to the nearest integer
floor(3.14159)
```




    [1] 3




```R
# cut off everything after the decimal point
trunc(3.14159)
```




    [1] 3




```R
# round the number to the third decimal place
round(3.14159, digits = 3)
```




    [1] 3.142




```R
# round to five significant digits
signif(3.14159, digits = 5)
```




    [1] 3.1416
