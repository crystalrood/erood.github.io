Title: Character Dates
Slug: character-dates
Summary: Character Dates
Date: 2016-05-01 12:00
Category: R Stats
Tags: Basics
Authors: Chris Albon




```R
# create a dates2 variable with simulated data
dates2 <- as.data.frame(
  cbind(c(1:5),
  c("8/31/70", "NA", "10/12/60", "1/1/66", "12/31/80"),
  c("8/31/56", "12-31-1977", "12Aug55", "July 31 1965" ,"30jan1952")))
```


```R
# add column names
colnames(dates2) <- c("ID", "date_factor", "date_horrible")

# view the dataframe
dates2
```




      ID date_factor date_horrible
    1  1     8/31/70       8/31/56
    2  2          NA    12-31-1977
    3  3    10/12/60       12Aug55
    4  4      1/1/66  July 31 1965
    5  5    12/31/80     30jan1952




```R
# load the chron packaage
library(chron)
```


```R
# convert date_factor into characters and the translate it into date format using format =
dates2$date.fmt <- chron(as.character(dates2$date_factor), format = "m/d/y")

# same as above but change the output format
dates2$date.fmt <- chron(as.character(dates2$date_factor), format = "m/d/y", out.format = "month day year")

# create a new variable that is their age in years (thus divide by 360), the floor() function converts the number into integers
dates2$age <- as.numeric(floor(difftime(chron("03/01/2013"), dates2$date.fmt, unit = "days")/360))

# Add a day to each element of a vector of ages
dates2$date.fmt + 1

# Ask which dates in a vector came before a set date
dates2$date.fmt < chron("04/02/62")
```

    Warning message:
    In unpaste(dates., sep = fmt$sep, fnames = fmt$periods, nfields = 3): wrong number of fields in entry(ies) 2Warning message:
    In unpaste(dates., sep = fmt$sep, fnames = fmt$periods, nfields = 3): wrong number of fields in entry(ies) 2




    [1] September 01 1970 <NA>              October 13 1960   January 02 1966  
    [5] January 01 1981  






    [1] FALSE    NA  TRUE FALSE FALSE




```R
# load the date package
library(date)
```


```R
dates2$date_autofmt <- as.date(as.character(dates2$date_horrible))
dates2[, c(1, 3, 6)]
```




      ID date_horrible date_autofmt
    1  1       8/31/56        -1218
    2  2    12-31-1977         6574
    3  3       12Aug55        -1603
    4  4  July 31 1965         2038
    5  5     30jan1952        -2893




```R
# take the horribly formatted dates, convert them into characters, auto convert the messy dates into clean dates (using as.date) then convert it into R's date class (as.Date). Notice the capitalization of as.date and as.Date.
dates2$date_amazing <- as.Date(as.date(as.character(dates2$date_horrible)))

dates2[, c(1, 3, 7)]
```




      ID date_horrible date_amazing
    1  1       8/31/56   1956-08-31
    2  2    12-31-1977   1977-12-31
    3  3       12Aug55   1955-08-12
    4  4  July 31 1965   1965-07-31
    5  5     30jan1952   1952-01-30
