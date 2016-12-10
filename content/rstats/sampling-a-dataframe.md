Title: Getting A Sample Of Random Rows From A Dataframe
Slug: sampling-a-dataframe
Summary: Getting A Sample Of Random Rows From A Dataframe
Date: 2016-05-01 12:00
Category: R Stats
Tags: Data Wrangling
Authors: Chris Albon


Original source: http://stackoverflow.com/questions/8273313/random-rows-in-dataframe-in-r


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
df <- data.frame(ID, Age, Sex, Weight, Height, Married)
```


```R
df
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
# create some simulated data
ID <- 1:10
Age <- c(26, 65, 15, 7, 88, 43, 28, 66 ,45, 12)
Sex <- c(1, 0, 1, 1, 0 ,1, 1, 1, 0, 1)
Weight <- c(132, 122, 184, 145, 118, NA, 128, 154, 166, 164)
Height <- c(60, 63, 57, 59, 64, NA, 67, 65, NA, 60)
Married <- c(0, 0, 0, 0, 0, 0, 1, 1, 0, 1)
```


```R
# create a new object that is comprised of three rows of the dataframe df, taken as random. literally what it is doing is chosing three numbers at random out of the total number of rows in a dataframe, and use that as the row index to definite which rows are included.
df.sample <- df[sample(nrow(df), 3), ]
```


```R
df.sample
```




      ID Age Sex Weight Height Married
    7  7  28   1    128     67       1
    2  2  65   0    122     63       0
    5  5  88   0    118     64       0
