Title: Loops With Replicate
Slug: replication-loops
Summary: Loops With Replicate
Date: 2016-05-01 12:00
Category: R Stats
Tags: Basics
Authors: Chris Albon


Original source: Learning R

Replicate applies an action individually to every element of a vector


```R
# Run runif(1) five times
replicate(5, runif(1))
```




    [1] 0.2769136 0.8304662 0.5407557 0.8074367 0.2867881



The below more complicated example, we create a function that first chooses a method of transportation and then based on what method of transport was selection, calculates a travel time based on that method of transport (hence the switch function). rnorm and rlnorm are simply what the example uses to create fake travel time data


```R
time_for_commute <- function() {
  #Choose a mode of transport for the day
  mode_of_transport <- sample(
    c("car", "bus", "train", "bike"),
    size = 1,
    prob = c(0.1, 0.2, 0.3, 0.4)
  )
  #Find the time to travel, depending upon mode of transport
  time <- switch(
    mode_of_transport,
    car   = rlnorm(1, log(30), 0.5),
    bus   = rlnorm(1, log(40), 0.5),
    train = rnorm(1, 30, 10),
    bike  = rnorm(1, 60, 5)
  )
  names(time) <- mode_of_transport
  time
}
```


```R
# Run the function
time_for_commute()
```




        bike
    60.55362




```R
# Run the function five times
replicate(5, time_for_commute())
```




        bike      bus    train    train     bike
    65.26913 71.15877 23.13382 29.23679 58.59026
