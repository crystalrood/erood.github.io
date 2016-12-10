Title: Cleaning Up Gender
Slug: cleaning-gender
Summary: Cleaning Up Gender
Date: 2016-05-01 12:00
Category: R Stats
Tags: Data Wrangling
Authors: Chris Albon


Original source: Learning R


```R
# create some messy fake gender data
gender <- c("MALE", "Male", "male", "M", "FEMALE", "Female", "female", "f", NA)
```


```R
# find strings that start with m and optionally ending in ale
clean_gender <- str_replace(
  gender,
  ignore.case("^m(ale)?$"),
  "Male"
)
```


```R
# find strings the start with f and optionally end in emale
clean_gender <- str_replace(
  clean_gender,
  ignore.case("^f(emale)?$"),
  "Female"
)
```


```R
clean_gender
```




    [1] "Male"   "Male"   "Male"   "Male"   "Female" "Female" "Female" "Female"
    [9] NA      
