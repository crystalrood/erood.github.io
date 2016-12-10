Title: Plot Points On A Map
Slug: plots-on-map
Summary: Plot Points On A Map
Date: 2016-05-01 12:00
Category: R Stats
Tags: Data Visualization
Authors: Chris Albon


Original source: http://stackoverflow.com/questions/11056738/plotting-points-from-a-data-frame-using-openstreetmap


```R
# load the ggmap package
library(ggmap)
```

    Warning message:
    : package ‘ggmap’ was built under R version 3.1.3Loading required package: ggplot2



```R
# make a data frame with the long/lat of three stores and their names
stores <- data.frame(
  name=c("Commercial","Union","Bedford"),
  longitude=c(-70.25042295455933,-70.26050806045532,-70.27726650238037),
  latitude=c(43.657471302616806,43.65663299041943,43.66091757424481)
)
```


```R
# create vector with the long/lat with two opposite corner of the map to mark the zoom level. Specifically, the first value is the bottom left of the map and the second value is the top right
downtown.pdx <- c(-70.2954, 43.64278, -70.2350, 43.68093)
```


```R
# Fetch map from stamen (use source = "osm" for open street maps)
portland <- get_map(location = downtown.pdx, source = "stamen")
```

    Map from URL : http://tile.stamen.com/terrain/14/4992/5977.jpg
    Map from URL : http://tile.stamen.com/terrain/14/4993/5977.jpg
    Map from URL : http://tile.stamen.com/terrain/14/4994/5977.jpg
    Map from URL : http://tile.stamen.com/terrain/14/4995/5977.jpg
    Map from URL : http://tile.stamen.com/terrain/14/4992/5978.jpg
    Map from URL : http://tile.stamen.com/terrain/14/4993/5978.jpg
    Map from URL : http://tile.stamen.com/terrain/14/4994/5978.jpg
    Map from URL : http://tile.stamen.com/terrain/14/4995/5978.jpg
    Map from URL : http://tile.stamen.com/terrain/14/4992/5979.jpg
    Map from URL : http://tile.stamen.com/terrain/14/4993/5979.jpg
    Map from URL : http://tile.stamen.com/terrain/14/4994/5979.jpg
    Map from URL : http://tile.stamen.com/terrain/14/4995/5979.jpg
    Map from URL : http://tile.stamen.com/terrain/14/4992/5980.jpg
    Map from URL : http://tile.stamen.com/terrain/14/4993/5980.jpg
    Map from URL : http://tile.stamen.com/terrain/14/4994/5980.jpg
    Map from URL : http://tile.stamen.com/terrain/14/4995/5980.jpg



```R
# view the map
portlandMap <- ggmap(portland)
```


```R
# add the points to the map
portlandMap <- portlandMap + geom_point(data = stores, aes(x = longitude, y = latitude), size = 5)
```


```R
# Add lavels for the points
portlandMap + geom_text(data = stores, aes(label = name, x = longitude+.001, y = latitude), hjust = 0)
```









![png]({filename}/images/plots-on-map_files/plots-on-map_7_1.png)
