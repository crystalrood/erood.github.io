Title: Proporton Table
Slug: proportion-table
Summary: Proporton Table
Date: 2016-05-01 12:00
Category: R Stats
Tags: Data Visualization
Authors: Chris Albon


Original source: The R Book


```R
# create a matrix of simulated count data
counts <- matrix(sample(1:100, 20, replace=T), nrow=4); counts
```




         [,1] [,2] [,3] [,4] [,5]
    [1,]   77   79   14   94    7
    [2,]  100   54   86   28   60
    [3,]   38   99   77   84   81
    [4,]   75   93   19   21   39




```R
# calculate each cell's proportion of the entire row's total counts
prop.table(counts,1)
```




              [,1]      [,2]       [,3]       [,4]       [,5]
    [1,] 0.2841328 0.2915129 0.05166052 0.34686347 0.02583026
    [2,] 0.3048780 0.1646341 0.26219512 0.08536585 0.18292683
    [3,] 0.1002639 0.2612137 0.20316623 0.22163588 0.21372032
    [4,] 0.3036437 0.3765182 0.07692308 0.08502024 0.15789474




```R
# calculate each cell's proportion of the entire columns's total counts
prop.table(counts,2)
```




              [,1]      [,2]       [,3]       [,4]       [,5]
    [1,] 0.2655172 0.2430769 0.07142857 0.41409692 0.03743316
    [2,] 0.3448276 0.1661538 0.43877551 0.12334802 0.32085561
    [3,] 0.1310345 0.3046154 0.39285714 0.37004405 0.43315508
    [4,] 0.2586207 0.2861538 0.09693878 0.09251101 0.20855615
