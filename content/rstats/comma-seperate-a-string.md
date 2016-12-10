Title: Comma Seperate A String
Slug: comma-seperate-a-string
Summary: Comma Seperate A String
Date: 2016-05-01 12:00
Category: R Stats
Tags: Basics
Authors: Chris Albon


Original code: http://onertipaday.blogspot.com/2007/06/string-manipulation-insert-delim.html


```R
# Create a text string
cities <- c("sonomanapahealdsburgoakland")
```


```R
# A vector with the locations of where we want each comma
comma.locations <- c(6,4,10,7)
```


```R
# Place the commas into the string according to the locations specifics in comma.locations
paste(read.fwf(textConnection(cities), comma.locations, as.is = TRUE), collapse = ",")
```




    [1] "sonoma,napa,healdsburg,oakland"
