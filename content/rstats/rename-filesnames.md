Title: Renaming Filenames
Slug: rename-filesnames
Summary: Renaming Filenames
Date: 2016-05-01 12:00
Category: R Stats
Tags: Basics
Authors: Chris Albon




```R
# create a variable with the directory of the files we want to rename
loc.dir <- paste(getwd(), "/test", sep=""); loc.dir
```




    [1] "/Users/chrisralbon/cra/cra_projects/peripheral_brain/notebooks/rstats/test"




```R
# create a list of files in the directory
refs <- list.files(path=loc.dir, all.files=TRUE, recursive=TRUE, full.names=TRUE); refs
```




    character(0)




```R
# create a vector with the numbers we will add to the file names
numbers <- 1:length(refs); numbers
```




    [1] 1 0




```R
# rename the files in "refs" to albon-*.txt, wherein * is the digits in the variable "numbers"
# file.rename(refs, paste0(loc.dir, "/", "albon-", numbers, ".txt"))
```
