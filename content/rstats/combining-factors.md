Title: Combining Factors
Slug: combining-factors
Summary: Combining Factors
Date: 2016-05-01 12:00
Category: R Stats
Tags: Basics
Authors: Chris Albon



Combining factors acts like interacting two variables. In other words, like interacting two binary variables to create all four possible combinations.


```R
# Create a binary variable for treatment or control
treatment <- gl(2, 1, labels = c("treatment", "control"))

# Create a binary variable for female or male
gender <- gl(2, 1, labels = c("female", "male"))
```


```R
# Interact the factors by combining them
interaction(treatment, gender)
```




    [1] treatment.female control.male    
    Levels: treatment.female control.female treatment.male control.male
