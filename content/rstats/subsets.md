Title: Subsetting Data
Slug: subsets
Summary: Subsetting Data
Date: 2016-05-01 12:00
Category: R Stats
Tags: Basics
Authors: Chris Albon


Original source: http://rforpublichealth.blogspot.com/2012/10/quick-and-easy-subsetting.html


```R
# create some simulated data
ID <- 1:10
Age <- c(26, 65, 15, 7, 88, 43, 28, 66 ,45, 12)
Sex <- c(1, 0, 1, 1, 0 ,1, 1, 1, 0, 1)
Weight <- c(132, 122, 184, 145, 118, NA, 128, 154, 166, 164)
Height <- c(60, 63, 57, 59, 64, NA, 67, 65, NA, 60)
Married <- c(0, 0, 0, 0, 0, 0, 1, 1, 0, 1)
```


```R
# create a dataframe of the simulated data
mydata <- data.frame(ID, Age, Sex, Weight, Height, Married)
mydata
```




       ID Age Sex Weight Height Married
    1   1  26   1    132     60       0
    2   2  65   0    122     63       0
    3   3  15   1    184     57       0
    4   4   7   1    145     59       0
    5   5  88   0    118     64       0
    6   6  43   1     NA     NA       0
    7   7  28   1    128     67       1
    8   8  66   1    154     65       1
    9   9  45   0    166     NA       0
    10 10  12   1    164     60       1




```R
# create a new variable called sub.data that is the subset of mydata, containing all rows where Age is less than 50 and sex is 0 and the columns ID, Age, and Weight
sub.data<-subset(mydata, Age>50 & Sex==0, select=c(ID, Age, Weight))
sub.data
```




      ID Age Weight
    2  2  65    122
    5  5  88    118
