Title: Merge Data Frames
Slug: merge-data-frame
Summary: Merge Data Frames
Date: 2016-05-01 12:00
Category: R Stats
Tags: Data Wrangling
Authors: Chris Albon




```R
# Create two variables of 50 observations, note that we only use 10 month names, because to be combined into a dataset all variables must have the same number of lengths OR be a multiple of the longest length.
percent.sms.85 <- runif(50)
state <- state.name
month.85 <- month.name[1:10]
```


```R
# Create a dataframe of those two variables
usa1985 <- data.frame(state, percent.sms.85, month.85)
```


```R
percent.sms.95 <- runif(50)
state <- state.name
month.95 <- month.name[1:10]
```


```R
# Create a dataframe of those two variables
usa1995 <- data.frame(state, percent.sms.95, month.95)
```


```R
# Merge the 1995 and 1985 data frames by the variable "state"
usa <- merge(usa1985, usa1995, by = "state")
```

If some observations don't have a match, we can force the merge with the all = TRUE argument


```R
# Drop the last 10 observations in usa1985
usa1985a <- usa1985[1:40,]
```


```R
# Merge 1985 and 1995 data frames
usa.a <- merge(usa1985a, usa1995, by = "state", all = TRUE)
```


```R
usa.a
```




                state percent.sms.85  month.85 percent.sms.95  month.95
    1         Alabama    0.911839169   January     0.78692563   January
    2          Alaska    0.962579448  February     0.70895643  February
    3         Arizona    0.026227813     March     0.72485492     March
    4        Arkansas    0.670236194     April     0.01125962     April
    5      California    0.020827639       May     0.33374079       May
    6        Colorado    0.863195854      June     0.68766522      June
    7     Connecticut    0.219795803      July     0.10379131      July
    8        Delaware    0.184099688    August     0.49875863    August
    9         Florida    0.454246269 September     0.73110314 September
    10        Georgia    0.765207091   October     0.61619085   October
    11         Hawaii    0.877940437   January     0.34551863   January
    12          Idaho    0.443048854  February     0.74052659  February
    13       Illinois    0.772117489     March     0.19904699     March
    14        Indiana    0.004526970     April     0.85266998     April
    15           Iowa    0.537924783       May     0.98608913       May
    16         Kansas    0.517531423      June     0.35238215      June
    17       Kentucky    0.048399794      July     0.96977605      July
    18      Louisiana    0.127585422    August     0.87639278    August
    19          Maine    0.693070376 September     0.93714056 September
    20       Maryland    0.446622736   October     0.47403974   October
    21  Massachusetts    0.996398812   January     0.11717452   January
    22       Michigan    0.598997187  February     0.85384948  February
    23      Minnesota    0.453290568     March     0.46549906     March
    24    Mississippi    0.501605880     April     0.54499399     April
    25       Missouri    0.344708045       May     0.99621523       May
    26        Montana    0.199458824      June     0.26662323      June
    27       Nebraska    0.661483499      July     0.30106483      July
    28         Nevada    0.403032863    August     0.99457227    August
    29  New Hampshire    0.006592093 September     0.29969927 September
    30     New Jersey    0.080242319   October     0.68534574   October
    31     New Mexico    0.157568631   January     0.35347240   January
    32       New York    0.425534808  February     0.30905687  February
    33 North Carolina    0.780164812     March     0.29777418     March
    34   North Dakota    0.338809068     April     0.31317768     April
    35           Ohio    0.969465860       May     0.70756109       May
    36       Oklahoma    0.869238595      June     0.63593124      June
    37         Oregon    0.069332679      July     0.99365654      July
    38   Pennsylvania    0.067476764    August     0.38521444    August
    39   Rhode Island    0.264621076 September     0.27603005 September
    40 South Carolina    0.843611176   October     0.22785430   October
    41   South Dakota             NA      <NA>     0.06466419   January
    42      Tennessee             NA      <NA>     0.56589275  February
    43          Texas             NA      <NA>     0.75391787     March
    44           Utah             NA      <NA>     0.82641243     April
    45        Vermont             NA      <NA>     0.99062278       May
    46       Virginia             NA      <NA>     0.38918234      June
    47     Washington             NA      <NA>     0.82666687      July
    48  West Virginia             NA      <NA>     0.69003692    August
    49      Wisconsin             NA      <NA>     0.03635303 September
    50        Wyoming             NA      <NA>     0.90969228   October
