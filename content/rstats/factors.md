Title: Factors
Slug: factors
Summary: Factors
Date: 2016-05-01 12:00
Category: R Stats
Tags: Basics
Authors: Chris Albon



Factors are a variable type used for categorial data.

Whenever a data frame is created with text strings, R treats it as a factor.


```R
# Create three variables of 50 observations length.
turnout <- runif(50)
state <- state.name
outcome <- c("win", "loss")
```


```R
# Create a dataframe of those two variables
usa <- data.frame(state, turnout, outcome)
```


```R
# Is "outcome" a factor? Yes.
class(usa$outcome)
```




    [1] "factor"




```R
# View the levels (i.e. category names) of the factor
levels(usa$outcome)
```




    [1] "loss" "win"




```R
# views the number of these levels (i.e. category IDs) of the factor
nlevels(usa$outcome)
```




    [1] 2




```R
# change levels of a factor
levels(usa$outcome) <- c("victory", "defeat")
```
