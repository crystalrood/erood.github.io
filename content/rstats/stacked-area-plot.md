Title: Stacked Area Plot
Slug: stacked-area-plot
Summary: Stacked Area Plot
Date: 2016-05-01 12:00
Category: R Stats
Tags: Data Visualization
Authors: Chris Albon



Source: http://www.r-bloggers.com/a-nifty-area-plot-or-a-bootleg-of-a-ggplot-geom/


```R
# load the ggplot2 package
library(ggplot2)

# load the reshape package
library(reshape)

# set the random seed
set.seed(3)
```


```R
# create a sequence
t.step <- seq(0,20)
```


```R
# create some group names
grps <- letters[1:10]
```


```R
# create simulated data for group values across time
grp.dat <- runif(length(t.step)*length(grps),5,15)
```


```R
# create data frame
grp.dat <- matrix(grp.dat,nrow=length(t.step),ncol=length(grps))
grp.dat <- data.frame(grp.dat,row.names=t.step)
names(grp.dat) <- grps
```


```R
#reshape the data
p.dat <- data.frame(step=row.names(grp.dat),grp.dat,stringsAsFactors=F)
p.dat <- melt(p.dat,id='step')
p.dat$step <- as.numeric(p.dat$step)
```


```R
#create plots
p <- ggplot(p.dat, aes(x=step,y=value)) + theme(legend.position="none")
```


```R
p + geom_area(aes(fill=variable))
```









![png]({filename}/images/stacked-area-plot_files/stacked-area-plot_8_1.png)



```R
p + geom_area(aes(fill=variable),position='fill')
```









![png]({filename}/images/stacked-area-plot_files/stacked-area-plot_9_1.png)
