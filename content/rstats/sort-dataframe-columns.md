Title: Sorting Columns Of A Data Frame
Slug: sort-dataframe-columns
Summary: Sorting Columns Of A Data Frame
Date: 2016-05-01 12:00
Category: R Stats
Tags: Data Wrangling
Authors: Chris Albon


Original source: http://stackoverflow.com/questions/1296646/how-to-sort-a-dataframe-by-columns-in-r


```R
# create some simulated data
df <- data.frame(score = c(runif(5)), team = c(letters[1:5]), state = c(state.name[1:5]))
```


```R
# sort by decending score, THEN sort by ascending team letter
df[with(df, order(-score, team)), ]
```




           score team      state
    1 0.99573538    a    Alabama
    2 0.82771332    b     Alaska
    5 0.61670246    e California
    3 0.32848427    c    Arizona
    4 0.04267817    d   Arkansas
