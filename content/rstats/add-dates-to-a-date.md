Title: Adding Time To A Date
Slug: add-dates-to-a-date
Summary: Adding Time To A Date
Date: 2016-05-01 12:00
Category: R Stats
Tags: Data Wrangling
Authors: Chris Albon




```R
# load the lubridate package
library(lubridate)
```


```R
# create a date variable
date.ex <- dmy("1/1/2001")
```


```R
date.ex
```




    [1] "2001-01-01 UTC"




```R
# add 45 days to a date
date.ex.2 <- date.ex + days(45)
```


```R
date.ex.2
```




    [1] "2001-02-15 UTC"




```R
# add six weeks to a date
date.ex.3 <- date.ex + weeks(6)
```


```R
date.ex.3
```




    [1] "2001-02-12 UTC"
