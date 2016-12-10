Title: Simple Venn Diagram
Slug: simple-venn-diagram
Summary: Simple Venn Diagram
Date: 2016-05-01 12:00
Category: R Stats
Tags: Data Visualization
Authors: Chris Albon


Original source: http://stackoverflow.com/questions/8713994/venn-diagram-in-r-proportional-and-color-shading-possible-semi-transparency-sup


```R
# load the venneuler package
require(venneuler)
```

    Loading required package: venneuler
    Loading required package: rJava



```R
# run the package on some simulated data
v <- venneuler(c(A = 100, B = 200, "A&B" = 50))
```


```R
# plot it
plot(v)
```


![png]({filename}/images/simple-venn-diagram_files/simple-venn-diagram_3_0.png)
