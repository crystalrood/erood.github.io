Title: Aggregate Data By Week Or Month
Slug: aggregate-by-week-or-month
Summary: Aggregate Data By Week Or Month
Date: 2016-05-01 12:00
Category: R Stats
Tags: Data Wrangling
Authors: Chris Albon



original source: http://stackoverflow.com/questions/19716244/aggregate-data-by-week-month-etc-in-r?lq=1


```R
# load the xts package
library(xts)
```

    Loading required package: zoo

    Attaching package: ‘zoo’

    The following objects are masked from ‘package:base’:

        as.Date, as.Date.numeric



## Create some simulated data


```R
# create an element for every year between two dates
date <- seq(as.Date("2006-01-01"), as.Date("2007-01-01"), by = "1 day")

# create some simulated values
score <- runif(366)

# create a zoo time series object of score and ata
zoo <- zoo(score, date)
```

## Create some averages


```R
# create a weekly average
weekly.avg <- apply.weekly(zoo, mean)
```


```R
weekly.avg
```




    2006-01-01 2006-01-08 2006-01-15 2006-01-22 2006-01-29 2006-02-05 2006-02-12
     0.6463105  0.3696941  0.4492466  0.5587588  0.3330893  0.7490642  0.3463500
    2006-02-19 2006-02-26 2006-03-05 2006-03-12 2006-03-19 2006-03-26 2006-04-02
     0.4594144  0.3015816  0.5016827  0.3824588  0.4501046  0.5086366  0.6927037
    2006-04-09 2006-04-16 2006-04-23 2006-04-30 2006-05-07 2006-05-14 2006-05-21
     0.5238080  0.6618441  0.4366701  0.6187016  0.6110044  0.5724795  0.5267836
    2006-05-28 2006-06-04 2006-06-11 2006-06-18 2006-06-25 2006-07-02 2006-07-09
     0.4003268  0.3999404  0.6366840  0.4546525  0.5675619  0.4411083  0.5747285
    2006-07-16 2006-07-23 2006-07-30 2006-08-06 2006-08-13 2006-08-20 2006-08-27
     0.4136250  0.4936679  0.4814989  0.4419165  0.3644543  0.6385395  0.5230308
    2006-09-03 2006-09-10 2006-09-17 2006-09-24 2006-10-01 2006-10-08 2006-10-15
     0.5259253  0.5474812  0.4658602  0.4771834  0.6106620  0.4471343  0.4576065
    2006-10-22 2006-10-29 2006-11-05 2006-11-12 2006-11-19 2006-11-26 2006-12-03
     0.6124155  0.5418694  0.3136825  0.4227544  0.2406943  0.3723846  0.6079556
    2006-12-10 2006-12-17 2006-12-24 2006-12-31 2007-01-01
     0.5289365  0.4426345  0.6362102  0.4849858  0.1102631




```R
# create a monthly average
monthly.avg <- apply.monthly(zoo, mean)
```


```R
monthly.avg
```




    2006-01-31 2006-02-28 2006-03-31 2006-04-30 2006-05-31 2006-06-30 2006-07-31
     0.4636550  0.4345047  0.4883293  0.5791776  0.5045688  0.5301847  0.4698487
    2006-08-31 2006-09-30 2006-10-31 2006-11-30 2006-12-31 2007-01-01
     0.5033712  0.5218908  0.5171836  0.3661705  0.5341010  0.1102631
