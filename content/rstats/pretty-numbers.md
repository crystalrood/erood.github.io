Title: Making Pretty Numbers with prettyNum
Slug: pretty-numbers
Summary: Making Pretty Numbers with prettyNum
Date: 2016-05-01 12:00
Category: R Stats
Tags: Basics
Authors: Chris Albon



We are taking two input numbers 1e10 and 1e-14, and formatting them with commas after zero and peroids before.


```R
prettyNum(
  c(1e10, 1e-14),
  big.mark = ",",
  small.mark = ".",
  preserve.width = "individual",
  scientific = FALSE
)
```




    [1] "10,000,000,000"     "0.00000.00000.0001"
