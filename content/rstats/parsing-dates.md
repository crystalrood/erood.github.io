Title: Parsing Dates
Slug: parsing-dates
Summary: Parsing Dates
Date: 2016-05-01 12:00
Category: R Stats
Tags: Data Wrangling
Authors: Chris Albon



Often imported data will need to be parsed. If the dates are character strings, you can use strptime to parse the date-time.


```R
# Import some moon landing day/times
moon_landings_str <- c(
  "20:17:40 20/07/1969",
  "06:54:35 19/11/1969",
  "09:18:11 05/02/1971",
  "22:16:29 30/07/1971",
  "02:23:35 21/04/1972",
  "19:54:57 11/12/1972"
)
```


```R
moon_landings_str
```




    [1] "20:17:40 20/07/1969" "06:54:35 19/11/1969" "09:18:11 05/02/1971"
    [4] "22:16:29 30/07/1971" "02:23:35 21/04/1972" "19:54:57 11/12/1972"




```R
# convert the date-time character strings into dates
moon_landings_lt <- strptime(
  moon_landings_str,
  "%H:%M:%S %d/%m/%Y",
  tz = "UTC")
```


```R
moon_landings_lt
```




    [1] "1969-07-20 20:17:40 UTC" "1969-11-19 06:54:35 UTC"
    [3] "1971-02-05 09:18:11 UTC" "1971-07-30 22:16:29 UTC"
    [5] "1972-04-21 02:23:35 UTC" "1972-12-11 19:54:57 UTC"
