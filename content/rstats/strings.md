Title: Strings
Slug: strings
Summary: Strings
Date: 2016-05-01 12:00
Category: R Stats
Tags: Basics
Authors: Chris Albon



Strings are text data stored in character vectors.

Paste function can "paste" text into string elements


```R
# Create a character vector with three strings
meals <- c("cheeseburger", "soup", "sandwich")
```


```R
# Paste "bacon" onto the end of each string element
bacon.meals <- paste(meals, "bacon"); bacon.meals
```




    [1] "cheeseburger bacon" "soup bacon"         "sandwich bacon"    




```R
bacon.meals.dash <- paste(meals, "bacon", sep="-"); bacon.meals.dash; bacon.meals.dash
```




    [1] "cheeseburger-bacon" "soup-bacon"         "sandwich-bacon"    






    [1] "cheeseburger-bacon" "soup-bacon"         "sandwich-bacon"    




```R
# We can also collapse the whole vector into a single string
mouthful <- paste(meals, collapse=""); mouthful
```




    [1] "cheeseburgersoupsandwich"
