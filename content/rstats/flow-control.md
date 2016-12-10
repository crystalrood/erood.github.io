Title: Flow Control
Slug: flow-control
Summary: Flow Control
Date: 2016-05-01 12:00
Category: R Stats
Tags: Basics
Authors: Chris Albon



This is the same as conditional statements.

## If

If always needs a logical statement in its brackets.


```R
# If TRUE, say so.
if(TRUE) message("This is true.")
```

    This is true.



```R
# If FALSE, say so.
if(FALSE) message("Wrong.")
```


```R
# If the random number generated is over .5, execute what is inside the top brackets, else execute what is inside the bottom brackets
if(runif(1) > 0.5)
{
  message("The number is over .5")
} else
{
  message("The number is under .5")
}
```

    The number is under .5


## ELSE IF


```R
# Generate a random number between 0 and 1
x <- runif(1)
```


```R
# Execute different message commands depending on the value of the number.
if(x > 0.25)
{
  message("x is greater than 0.25")
} else if(x > 0.5)
{
  message("x is greater than 0.50")
} else if(x > 0.75)
{
  message("x is greater than 0.75")
} else if(x > 0.95)
{
  message("x is greater than 0.95")
}
```

    x is greater than 0.25


## IFELSE On Every Element In A Vector

IFELSE is for the flow control of entire vectors


```R
# Generate 10 random elements between 0 and 1
y <- runif(10)
```


```R
# If an element is above .5, mark as "high", else, mark as "low"
ifelse(y > 0.5, "High", "Low")
```




     [1] "Low"  "Low"  "High" "Low"  "Low"  "High" "Low"  "Low"  "Low"  "High"
