Title: Making A Back To Back Histogram
Slug: back-to-back-histogram
Summary: Making A Back To Back Histogram
Date: 2016-05-01 12:00
Category: R Stats
Tags: Data Visualization
Authors: Chris Albon


Original source: http://onertipaday.blogspot.com/2007/06/back-to-back-historgram.html


```R
# Load the Hmisc package (install it if necessary)
library(Hmisc)
```


```R
# Create 1000  observations, with mean 300
data <- rnorm(1000,300,10)
```


```R
# Create 1000 sex observations of male and female
sex <- sample(c('female','male'),1000,TRUE)
```


```R
# Create a back to back histogram of the data divided up by sex
out <- histbackback(split(data, sex), probability=TRUE, xlim=c(-.06,.06), main = 'Back to Back Histogram')

# Add color to the left histogram
barplot(-out$left, col="red" , horiz=TRUE, space=0, add=TRUE, axes=FALSE)

# Add color to the right histogram
barplot(out$right, col="blue", horiz=TRUE, space=0, add=TRUE, axes=FALSE)
```


![png]({filename}/images/back-to-back-histogram_files/back-to-back-histogram_4_0.png)



![png]({filename}/images/back-to-back-histogram_files/back-to-back-histogram_4_1.png)



![png]({filename}/images/back-to-back-histogram_files/back-to-back-histogram_4_2.png)
