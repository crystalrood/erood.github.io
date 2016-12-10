Title: Classes
Slug: classes
Summary: Classes
Date: 2016-05-01 12:00
Category: R Stats
Tags: Basics
Authors: Chris Albon



All variables have a class. Variables also have modes and storage types, but those are legacy and don't worry about them.


```R
# Find a variable's class
class(TRUE)
```




    [1] "logical"



### R has three classes of numbers


```R
# Numeric
class(sqrt(3))
```




    [1] "numeric"




```R
# Complex
class(3i)
```




    [1] "complex"




```R
# Integer (add L to make a number an integer)
class(3L)
```




    [1] "integer"




```R
# Integer
class(3:33)
```




    [1] "integer"



### R Also Has Other Classes


```R
# Characters (Strings, like text)
class(c("Arizona", "Maryland"))
```




    [1] "character"




```R
# Factors (like unordered categories)
class(factor(c("male", "female")))
```




    [1] "factor"




```R
# Factors have both values (i.e. a label) and a level (i.e. a numeric ID number)
gender <- factor(c("male", "female"))
```


```R
# View the values
levels(gender)
```




    [1] "female" "male"  




```R
# View the number of levels
nlevels(gender)
```




    [1] 2




```R
# View the levels of each element of a factor
as.integer(gender)
```




    [1] 2 1




```R
# View the values of a factor as character strings
as.character(gender)
```




    [1] "male"   "female"
