Title: Extracting Information From Objects Using Names()
Slug: names
Summary: Extracting Information From Objects Using Names()
Date: 2016-05-01 12:00
Category: R Stats
Tags: Basics
Authors: Chris Albon


Original source: http://rforpublichealth.blogspot.com/2013/03/extracting-information-from-objects.html


```R
# create some simulated data
ID <- 1:10
Age <- c(26, 65, 15, 7, 88, 43, 28, 66 ,45, 12)
Sex <- c(1, 0, 1, 1, 0 ,1, 1, 1, 0, 1)
Weight <- c(132, 122, 184, 145, 118, NA, 128, 154, 166, 164)
Height <- c(60, 63, 57, 59, 64, NA, 67, 65, NA, 60)
Married <- c(0, 0, 0, 0, 0, 0, 1, 1, 0, 1)
```


```R
# create a dataframe of the simulated data
mydata <- data.frame(ID, Age, Sex, Weight, Height, Married)
```

## names() shows us everything stored under an object


```R
# view everything under mydata
names(mydata)
```




    [1] "ID"      "Age"     "Sex"     "Weight"  "Height"  "Married"



## we can use names() to change a column header


```R
# change the name of column 4 to Weight_lbs
names(mydata)[4]<-"Weight_lbs"
```


```R
# run a regression
reg.object <- lm(Weight_lbs ~ Height + Age, data = mydata)
```


```R
# display all the objects under the regression
names(reg.object)
```




     [1] "coefficients"  "residuals"     "effects"       "rank"         
     [5] "fitted.values" "assign"        "qr"            "df.residual"  
     [9] "na.action"     "xlevels"       "call"          "terms"        
    [13] "model"        




```R
# print the residuals of the regression
reg.object$residuals
```




             1          2          3          4          5          7          8
    -19.799464 -12.030679  20.687479 -14.062906  -7.873562  -2.223245  26.229706
            10
      9.072671




```R
# print a histogram of the residuals
hist(reg.object$residuals, main="Distribution of Residuals" ,xlab="Residuals")
```


![png]({filename}/images/names_files/names_10_0.png)
