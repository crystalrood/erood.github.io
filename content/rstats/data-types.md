Title: Data Types
Slug: data-types
Summary: Data Types
Date: 2016-05-01 12:00
Category: R Stats
Tags: Basics
Authors: Chris Albon



## Vectors

### Vectors could best be described as rows of information.


```R
### Create a row containing five values
x <- c(1,2,3,4,5)
```

## Factors

### Factors are best thought about as categories, and each individual category is represented by a name and a numerical identifying value.


```R
### Create a factor that represents a variable with three categories
y <- factor(c("yes", "no", "maybe"))
```

## Matrix

### A matrix is a great of numbers, but no text strings


```R
### Create a matrix of some data
k <- matrix(data = 1:15, nrow = 5, ncol = 5, byrow = T)
```

## Arrays

### An array is like a matrix, but in 3D (like a time series)


```R
### Create an array
z <- array(1:27,dim=c(3,3,3))
```

## Lists

### A list is a list of R objects, any objects


```R
### Create variables of three different data types
f <- c(1:4)
j <- FALSE
u <- matrix(c(1:4),nrow=2,ncol=2)

### Combine them into a list
m <- list(f,j,u)
```

## Dataframes

### Data frames are like excel spreadsheets, all types of data in a big grid


```R
s <- 1:5
d <- c(T,T,F,F,T)
df <- data.frame(s,d)
```
