Title: Inner, Outer, Right, And Left Joins
Slug: inner-outter-right-left-join
Summary: Inner, Outer, Right, And Left Joins
Date: 2016-05-01 12:00
Category: R Stats
Tags: Basics
Authors: Chris Albon



Additional explaination: http://www.codinghorror.com/blog/2007/10/a-visual-explanation-of-sql-joins.html

Original source: http://stackoverflow.com/questions/1299871/how-to-join-data-frames-in-r-inner-outer-left-right


```R
# create two dataframes are fake data
survey.1 <- data.frame(response.id = c(1:6), region = c(rep("Kisumu",3),rep("Mumbasa",3)))
survey.2 <- data.frame(response.id = c(2,4,6), region = c(rep("Nairobi",2),rep("Tankana",1)))
```

## Inner Join Only Merges Observations Shared By Both Data Frames


```R
# merge survey.1 and survey.2 by response.id
merge(survey.1, survey.2, by="response.id")
```




      response.id region.x region.y
    1           2   Kisumu  Nairobi
    2           4  Mumbasa  Nairobi
    3           6  Mumbasa  Tankana



## Outer Join Includes Merges All Observations, Leaving A NULL Observation When There Is No Match


```R
# merge survey.1 and survey.2 by response.id, but include observations that don't match
merge(x = survey.1, y = survey.2, by = "response.id", all = TRUE)
```




      response.id region.x region.y
    1           1   Kisumu     <NA>
    2           2   Kisumu  Nairobi
    3           3   Kisumu     <NA>
    4           4  Mumbasa  Nairobi
    5           5  Mumbasa     <NA>
    6           6  Mumbasa  Tankana



## Left Join Includes All Observations From The First Dataframe But Only Matching Observations From The Second Dataframe


```R
# merge survey.1 and survey.2 by response.id, but include survey.1 observations
merge(x = survey.1, y = survey.2, by = "response.id", all.x=TRUE)
```




      response.id region.x region.y
    1           1   Kisumu     <NA>
    2           2   Kisumu  Nairobi
    3           3   Kisumu     <NA>
    4           4  Mumbasa  Nairobi
    5           5  Mumbasa     <NA>
    6           6  Mumbasa  Tankana



## Left Join Includes All Observations From The Second Dataframe But Only Matching Observations From The First Dataframe


```R
# merge survey.1 and survey.2 by response.id, but include survey.2 observations
merge(x = survey.1, y = survey.2, by = "response.id", all.y=TRUE)
```




      response.id region.x region.y
    1           2   Kisumu  Nairobi
    2           4  Mumbasa  Nairobi
    3           6  Mumbasa  Tankana
