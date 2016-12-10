Title: Crosstabs
Slug: crosstabs
Summary: Crosstabs
Date: 2016-05-01 12:00
Category: R Stats
Tags: Data Visualization
Authors: Chris Albon




```R
# create some simulated disaster data
event <- c("flood","fire","flood","fire","riot","flood","riot","riot","flood");
location <- c("africa", "asia", "europe","africa", "asia", "europe","africa", "asia", "europe")
disaster <- data.frame(event, location)
rm(event, location)
```


```R
# create a variable that is the frequency counts of different types of disaster events
event.counts.df <- as.data.frame(table(disaster$event));event.counts.df
```




       Var1 Freq
    1  fire    2
    2 flood    4
    3  riot    3




```R
# create a crosstab of event types by location
disaster.crosstab <- table(disaster$event, disaster$location); disaster.crosstab
```





            africa asia europe
      fire       1    1      0
      flood      1    0      3
      riot       1    2      0
