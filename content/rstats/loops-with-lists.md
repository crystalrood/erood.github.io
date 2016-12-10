Title: Loops With Lists
Slug: loops-with-lists
Summary: Loops With Lists
Date: 2016-05-01 12:00
Category: R Stats
Tags: Basics
Authors: Chris Albon




```R
# create list object of fake data
names <- c("John", "Jack", "John", "Jack", "Jack")
numbers <- c(3434, 4352, 3452, 3452, 2345)
numbers2 <- c(3434, 4352, 3452, 3452, 2345)
win <- c(T, F, T, F, T, F)
data.list <- list(names, numbers, win)
data.list.numbers <- list(numbers, numbers2)
```


```R
# apply (via list apply) the unique() function to every element in the list
lapply(data.list, unique)
```




    [[1]]
    [1] "John" "Jack"

    [[2]]
    [1] 3434 4352 3452 2345

    [[3]]
    [1]  TRUE FALSE




## vapply is like lapply, but it returns a vector


```R
# apply (via list apply) the unique() function to every element in the list
vapply(data.list.numbers, unique, numeric(4))
```




         [,1] [,2]
    [1,] 3434 3434
    [2,] 4352 4352
    [3,] 3452 3452
    [4,] 2345 2345
