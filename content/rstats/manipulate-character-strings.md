Title: Manipulating Character Strings (i.e. text)
Slug: manipulate-character-strings
Summary: Manipulating Character Strings (i.e. text)
Date: 2016-05-01 12:00
Category: R Stats
Tags: Basics
Authors: Chris Albon



R can handle a number of types of data, including numbers and text. In R, the text is refered to as character strings and is always wrapped in double quotation marks. In other words, if something is inside quotation marks, it is treated as text.

R has a number of functions avaliable for manipulating text.


```R
# create simulated district crime name
district <- factor(c("NORTH", "NORTHWEST", "CENTRAL", "SOUTH", "SOUTHWEST", "WESTERN"))
```

## Count the number of characters in each individual character string in an object


```R
# display each district's name
levels(district)
```




    [1] "CENTRAL"   "NORTH"     "NORTHWEST" "SOUTH"     "SOUTHWEST" "WESTERN"  



## You can also display text without quotes, although it is rare you would want to do so.


```R
# display each police district's name
levels(district)
```




    [1] "CENTRAL"   "NORTH"     "NORTHWEST" "SOUTH"     "SOUTHWEST" "WESTERN"  




```R
# display each police district's name without quotes
noquote(levels(district))
```




    [1] CENTRAL   NORTH     NORTHWEST SOUTH     SOUTHWEST WESTERN  



## R can add characters to a vector of character strings using the paste function


```R
# Add "DISTRICT" to the name of each police district
paste(levels(district), "DISTRICT")
```




    [1] "CENTRAL DISTRICT"   "NORTH DISTRICT"     "NORTHWEST DISTRICT"
    [4] "SOUTH DISTRICT"     "SOUTHWEST DISTRICT" "WESTERN DISTRICT"  



## Extracting Segments Of Character Strings using Substring Function


```R
# Extract characters from district names, starting at the 1st character and ending at the 5th character
substr(district, 1, 5)
```




    [1] "NORTH" "NORTH" "CENTR" "SOUTH" "SOUTH" "WESTE"
