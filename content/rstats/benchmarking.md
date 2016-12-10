Title: Benchmarking R Speed
Slug: benchmarking
Summary: Benchmarking R Speed
Date: 2016-05-01 12:00
Category: R Stats
Tags: Other
Authors: Chris Albon




```R
# how long does it take R to create a huge sequence of numbers?
system.time(1:10000000)
```




       user  system elapsed
      0.037   0.014   0.053




```R
# how long does it take R to create a equally long set of random draws
system.time(runif(10000000))
```




       user  system elapsed
      0.392   0.028   0.436
