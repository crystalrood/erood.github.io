Title: File Paths
Slug: file-paths
Summary: File Paths
Date: 2016-05-01 12:00
Category: R Stats
Tags: Basics
Authors: Chris Albon



Paths can be relative to the current working directory


```R
# View the working directory
getwd()
```




    [1] "/Users/chrisralbon/cra/cra_projects/peripheral_brain/notebooks/rstats"




```R
# Set the working directory to the user's home directory
setwd("~")
```

- In relative paths, . denotes the currect directory
- In relative paths, .. denotes the parent directory
- In relative paths,  ~ denotes your home directory


```R
# Path.expand converts relative paths to absolutely paths
path.expand("~")
```




    [1] "/Users/chrisralbon"




```R
# basename() returns the file name without the path
basename("~")
```




    [1] "chrisralbon"




```R
# dirname returns the path without the file name
dirname("~")
```




    [1] "/Users"
