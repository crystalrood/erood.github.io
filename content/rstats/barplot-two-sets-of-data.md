Title: Bar Graph Of Two Sets Of Data
Slug: barplot-two-sets-of-data
Summary: Bar Graph Of Two Sets Of Data
Date: 2016-05-01 12:00
Category: R Stats
Tags: Data Visualization
Authors: Chris Albon




```R
# Create a variable of rain fall in Spain
spain <- c(0.0001, 0.0059, 0.0855, 0.9082)

# Create a variable of rain fall in Yemen
yemen <- c(0.54, 0.813, 0.379, 0.35)

# create a two row matrix with spain and yemen
rainfall <- rbind(spain, yemen)
```


```R
# Create a bar graph with paired data (using "beside = TRUE") and with the names of some months
mp <- barplot(rainfall, beside = TRUE, ylim = c(0, 1), names.arg = c("March", "April", "May", "June"))

# Draw the bar values above the bars
text(mp, rainfall, labels = format(rainfall, 4), pos = 3, cex = .75)
```


![png]({filename}/images/barplot-two-sets-of-data_files/barplot-two-sets-of-data_2_0.png)



![png]({filename}/images/barplot-two-sets-of-data_files/barplot-two-sets-of-data_2_1.png)
