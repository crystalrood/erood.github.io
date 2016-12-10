Title: Random Numbers
Slug: random-numbers
Summary: Random Numbers
Date: 2016-05-01 12:00
Category: R Stats
Tags: Basics
Authors: Chris Albon




```R
# Generate 10 random numbers between 0 and 1
runif(10)
```




     [1] 0.13315436 0.14357165 0.52478178 0.21880271 0.18908152 0.02590017
     [7] 0.05517990 0.58034118 0.32128920 0.90293812




```R
# Generate 10 random numbers between 5 and 1-
runif(10, 5, 10)
```




     [1] 5.179785 5.485701 5.885241 6.159060 5.281826 7.630544 9.717838 9.091188
     [9] 5.138212 7.781516




```R
# Generate 10 random integers between 1 and 10, with replacement
sample(1:10, 10, replace=T)
```




     [1]  1  6 10 10  1 10 10  2  7  2




```R
# Select 3 random integers from a pool of 100 integers that range between 1 and 100
sample(1:100, 6, replace=F)
```




    [1] 76 18 32 37 94 78




```R
# Select three state names witout replacement
sample(state.name, 3)
```




    [1] "Connecticut" "Nevada"      "Wyoming"    
