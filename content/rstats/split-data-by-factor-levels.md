Title: Data can be split up by levels of a factor
Slug: split-data-by-factor-levels
Summary: Data can be split up by levels of a factor
Date: 2016-05-01 12:00
Category: R Stats
Tags: Data Wrangling
Authors: Chris Albon


(i.e. categories in a nominal variable)


```R
district <- factor(c("NORTH", "NORTHWEST", "CENTRAL", "SOUTH", "SOUTHWEST", "WESTERN"))
number.crimes <- runif(6)
year <- c(2009, 2009, 2009, 2010, 2010, 2009)
crime <- data.frame(year, district, number.crimes)
```


```R
# split up the crime data by district
split(crime, district)
```




    $CENTRAL
      year district number.crimes
    3 2009  CENTRAL     0.9478017

    $NORTH
      year district number.crimes
    1 2009    NORTH     0.6461916

    $NORTHWEST
      year  district number.crimes
    2 2009 NORTHWEST     0.1150372

    $SOUTH
      year district number.crimes
    4 2010    SOUTH     0.8126506

    $SOUTHWEST
      year  district number.crimes
    5 2010 SOUTHWEST     0.6700562

    $WESTERN
      year district number.crimes
    6 2009  WESTERN     0.5597461




Imagine if you also can crime data for 2009, you can use the combination of split() and sapply() to create a nice 2x2 table


```R
# create 2009 crime data, for this example we are keeping the data the same for both years
numberCrimes09 <- number.crimes

# add a column in bmore.crime for numberCrime09
crime <- cbind(numberCrimes09, crime)

# display the top few rows of bmore.crime to check everything looks good
head(crime)

#find the combined sum of the both annual crime total columns, by district
sapply(split(crime[,c('numberCrimes09','number.crimes')], district), sum)
```




      numberCrimes09 year  district number.crimes
    1      0.6461916 2009     NORTH     0.6461916
    2      0.1150372 2009 NORTHWEST     0.1150372
    3      0.9478017 2009   CENTRAL     0.9478017
    4      0.8126506 2010     SOUTH     0.8126506
    5      0.6700562 2010 SOUTHWEST     0.6700562
    6      0.5597461 2009   WESTERN     0.5597461






      CENTRAL     NORTH NORTHWEST     SOUTH SOUTHWEST   WESTERN
    1.8956034 1.2923833 0.2300744 1.6253013 1.3401124 1.1194923
