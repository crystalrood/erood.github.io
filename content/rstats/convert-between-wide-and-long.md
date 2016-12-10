Title: Converting Between Wide And Long Form Data
Slug: convert-between-wide-and-long
Summary: Converting Between Wide And Long Form Data
Date: 2016-05-01 12:00
Category: R Stats
Tags: Data Wrangling
Authors: Chris Albon


Original Source: Learning R


```R
# Load the reshape library
library(reshape2)
```


```R
# Generate five subjects, each with five measurements
name <- c("Jack", "Jill", "Steve", "Jake", "Bill")
obs1 <- runif(5)
obs2 <- runif(5)
obs3 <- runif(5)
obs4 <- runif(5)
obs5 <- runif(5)
```


```R
# create a wide form data frame. That is, one row per person, one column per measurement
survey.wide <- data.frame(name, obs1, obs2, obs3, obs4, obs5)
```


```R
# convert from wide to long. id.vars denotes the variable to make the transition by and measure.vars denotes the variables to flip
survey.long <- melt(survey.wide, id.vars = "name", measure.vars = c("obs1", "obs2", "obs3", "obs4", "obs5"))
```


```R
survey.long
```




        name variable      value
    1   Jack     obs1 0.74041288
    2   Jill     obs1 0.52529347
    3  Steve     obs1 0.97317970
    4   Jake     obs1 0.85910345
    5   Bill     obs1 0.55121888
    6   Jack     obs2 0.03121784
    7   Jill     obs2 0.30319273
    8  Steve     obs2 0.05282432
    9   Jake     obs2 0.31912928
    10  Bill     obs2 0.15419403
    11  Jack     obs3 0.11751059
    12  Jill     obs3 0.15045148
    13 Steve     obs3 0.45201750
    14  Jake     obs3 0.99880524
    15  Bill     obs3 0.73128530
    16  Jack     obs4 0.09517355
    17  Jill     obs4 0.97003014
    18 Steve     obs4 0.57478533
    19  Jake     obs4 0.68951869
    20  Bill     obs4 0.17464191
    21  Jack     obs5 0.85086481
    22  Jill     obs5 0.45689664
    23 Steve     obs5 0.80029436
    24  Jake     obs5 0.14644067
    25  Bill     obs5 0.36649096




```R
# convert long to wide
survey.wide.2 <- dcast(survey.long, name ~ variable)
```


```R
survey.wide.2
```




       name      obs1       obs2      obs3       obs4      obs5
    1  Bill 0.5512189 0.15419403 0.7312853 0.17464191 0.3664910
    2  Jack 0.7404129 0.03121784 0.1175106 0.09517355 0.8508648
    3  Jake 0.8591035 0.31912928 0.9988052 0.68951869 0.1464407
    4  Jill 0.5252935 0.30319273 0.1504515 0.97003014 0.4568966
    5 Steve 0.9731797 0.05282432 0.4520175 0.57478533 0.8002944
