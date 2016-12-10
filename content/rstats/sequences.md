Title: Create a sequences of numbers
Slug: sequences
Summary: Create a sequences of numbers
Date: 2016-05-01 12:00
Category: R Stats
Tags: Basics
Authors: Chris Albon



We can use the collem to create a sequence of integers.


```R
# Create a sequence from 1 to 5, spread one number apart
1:5
```




    [1] 1 2 3 4 5



However, for more control we can use seq.int to specify the spacing the sequence


```R
# Create a sequence from 1 to 10, spread 2.5 apart
seq.int(1, 10, 2.5)
```




    [1] 1.0 3.5 6.0 8.5
