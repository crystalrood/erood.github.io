Title: Summarize A Variable
Slug: summarize
Summary: Summarize A Variable
Date: 2016-05-01 12:00
Category: R Stats
Tags: Basics
Authors: Chris Albon




```R
# Create two variables of 50 observations
percent.sms <- runif(50)
location <- state.name
```


```R
# Create a dataframe of those two variables
usa <- data.frame(location, percent.sms)
```


```R
# Summarize the dataframe
summary(usa)
```




           location   percent.sms       
     Alabama   : 1   Min.   :0.0002011  
     Alaska    : 1   1st Qu.:0.2562950  
     Arizona   : 1   Median :0.5068584  
     Arkansas  : 1   Mean   :0.4832696  
     California: 1   3rd Qu.:0.7120861  
     Colorado  : 1   Max.   :0.9816996  
     (Other)   :44                      




```R
# View the top few rows of the dataframe
head(usa)
```




        location percent.sms
    1    Alabama   0.8962870
    2     Alaska   0.5507513
    3    Arizona   0.5061370
    4   Arkansas   0.9779650
    5 California   0.6913123
    6   Colorado   0.4087530




```R
# View the structure of the dataframe
str(usa)
```

    'data.frame':	50 obs. of  2 variables:
     $ location   : Factor w/ 50 levels "Alabama","Alaska",..: 1 2 3 4 5 6 7 8 9 10 ...
     $ percent.sms: num  0.896 0.551 0.506 0.978 0.691 ...



```R
# View the attributes of the dataframe
attributes(usa)
```




    $names
    [1] "location"    "percent.sms"

    $row.names
     [1]  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25
    [26] 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50

    $class
    [1] "data.frame"





```R
# View the dataframe
View(usa)
```
