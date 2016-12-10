Title: Create High-Res Plots In R
Slug: high-res-plots
Summary: Create High-Res Plots In R
Date: 2016-05-01 12:00
Category: R Stats
Tags: Data Visualization
Authors: Chris Albon




```R
## Generate 100,000 normally distributed observations
x <- rnorm(100000)
```


```R
# Create a 1600x1600 png at 300px/in
png("100kPoints300dpi.png", units = "px", width=1600, height=1600, res=300)
```


```R
# Plot the 100 points on the png
plot(x, main="100,000 points", col=adjustcolor("black", alpha=0.2))
dev.off()
```


![png]({filename}/images/high-res-plots_files/high-res-plots_3_0.png)





    quartz_off_screen
                    3
