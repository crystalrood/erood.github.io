Title: Loops
Slug: loops
Summary: Loops
Date: 2016-05-01 12:00
Category: R Stats
Tags: Basics
Authors: Chris Albon



R has three types of loops: repeat, while, and for.

## repeat Loops

Repeat loops executes the same code again and again until told to stop.


```R
# print 1 to 10, stop at 10
for(i in 1:10)
{
  print(paste("i =", i));
}
```

    [1] "i = 1"
    [1] "i = 2"
    [1] "i = 3"
    [1] "i = 4"
    [1] "i = 5"
    [1] "i = 6"
    [1] "i = 7"
    [1] "i = 8"
    [1] "i = 9"
    [1] "i = 10"


## while Loops

Unlike repeat loops, while loops check at the beginning of the code if that code should end, and then (maybe) execute. This is the oppsite to repeat loops that execute and then check if they should end.


```R
# create an object that samples one of the three character strings
action <- sample(
  c(
    "Make pancakes",
    "Make burritos",
    "Make tacos"
  ),
  1
)

# If the variable "action" (created above) is not "Make tacos" then run action (recreated in the loop) again. Do so until it is make tacos.
while(action != "Make tacos")
{
  action <- sample(
    c(
      "Make pancakes",
      "Make burritos",
      "Make tacos"
    ),
    1
  )
  message(action)
}
```

    Make burritos
    Make tacos


## for Loops

For loops are for when you want to repeat a code for a known and finite amount of time. for loops operate on each element of the vector.


```R
# for each element in a 1:5 vector, say a message
for(i in 1:5) message("i = ", i)

# For each month in the variable, month.name, say a message
for(month in month.name)
{
  message("The month of ", month)
}
```

    i = 1
    i = 2
    i = 3
    i = 4
    i = 5
    The month of January
    The month of February
    The month of March
    The month of April
    The month of May
    The month of June
    The month of July
    The month of August
    The month of September
    The month of October
    The month of November
    The month of December
