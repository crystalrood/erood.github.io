Title: Convert A List Into A Dataframe
Slug: list-to-dataframe
Summary: Convert A List Into A Dataframe
Date: 2016-05-01 12:00
Category: R Stats
Tags: Data Wrangling
Authors: Chris Albon




```R
# create a list of two elements, the first a vector of 20 obs, the second 20 state names
the.list <- list(scores = runif(20), states = state.name[1:20]); the.list
```




    $scores
     [1] 0.72770677 0.61598787 0.96234018 0.19366523 0.26006986 0.07253386
     [7] 0.73779295 0.58013676 0.18979002 0.72309143 0.48458231 0.51446047
    [13] 0.88990973 0.53759564 0.62698847 0.08148905 0.31585633 0.88666670
    [19] 0.87910724 0.59395343

    $states
     [1] "Alabama"     "Alaska"      "Arizona"     "Arkansas"    "California"
     [6] "Colorado"    "Connecticut" "Delaware"    "Florida"     "Georgia"    
    [11] "Hawaii"      "Idaho"       "Illinois"    "Indiana"     "Iowa"       
    [16] "Kansas"      "Kentucky"    "Louisiana"   "Maine"       "Maryland"   





```R
# create a dataframe with identifying each element of the list as a dataframe column
df <- data.frame(the.list$scores, the.list$states); df
```




       the.list.scores the.list.states
    1       0.72770677         Alabama
    2       0.61598787          Alaska
    3       0.96234018         Arizona
    4       0.19366523        Arkansas
    5       0.26006986      California
    6       0.07253386        Colorado
    7       0.73779295     Connecticut
    8       0.58013676        Delaware
    9       0.18979002         Florida
    10      0.72309143         Georgia
    11      0.48458231          Hawaii
    12      0.51446047           Idaho
    13      0.88990973        Illinois
    14      0.53759564         Indiana
    15      0.62698847            Iowa
    16      0.08148905          Kansas
    17      0.31585633        Kentucky
    18      0.88666670       Louisiana
    19      0.87910724           Maine
    20      0.59395343        Maryland
