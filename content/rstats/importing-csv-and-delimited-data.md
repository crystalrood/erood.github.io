Title: Importing CSV and Delimited Data
Slug: importing-csv-and-delimited-data
Summary: Importing CSV and Delimited Data
Date: 2016-05-01 12:00
Category: R Stats
Tags: Basics
Authors: Chris Albon


Original source: Learning R

**Note: This tutorial won't work until you change the URL to the CSV and remove the comment tags.**


```R
# Flat Files Offline
# testdata <- read.table("d:/data/mydata.dat", header=TRUE) # valid
```


```R
## Read.csv is like read.table but the default seperator and adds a header
```


```R
# Flat File Online
# testdata2 <- read.table("http://science.nature.nps.gov/im/monitor/stats/R/data/ MyData.csv", header=TRUE, sep=",")
```


```R
# Specify . As Denoting A Missing Value
# testdata <- read.table("mydata.csv", header=TRUE, sep=",", na.strings=".")
```
