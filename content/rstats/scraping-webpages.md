Title: Scraping Web Pages
Slug: scraping-webpages
Summary: Scraping Web Pages
Date: 2016-05-01 12:00
Category: R Stats
Tags: Basics
Authors: Chris Albon


Original source: Learning R


```R
# Load RCurl Library
library(RCurl)
```


```R
# Create a string with the URL to the website
time_url <- "http://tycho.usno.navy.mil/cgi-bin/timer.pl"
```


```R
# Download the HTML
time_page <- getURL(time_url)
```


```R
# Use concatenate and view the html in a pretty way
cat(time_page)
```

    <!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 3.2 Final"//EN>
    <html>
    <body>
    <TITLE>What time is it?</TITLE>
    <H2> US Naval Observatory Master Clock Time</H2> <H3><PRE>
    <BR>Mar. 14, 18:14:26 UTC		Universal Time
    <BR>Mar. 14, 02:14:26 PM EDT		Eastern Time
    <BR>Mar. 14, 01:14:26 PM CDT		Central Time
    <BR>Mar. 14, 12:14:26 PM MDT		Mountain Time
    <BR>Mar. 14, 11:14:26 AM PDT		Pacific Time
    <BR>Mar. 14, 10:14:26 AM AKDT	Alaska Time
    <BR>Mar. 14, 08:14:26 AM HAST	Hawaii-Aleutian Time
    </PRE></H3><P><A HREF="http://www.usno.navy.mil"> US Naval Observatory</A>

    </body></html>




```R
# load XML library
library(XML)
```


```R
# parse the HTML
time_doc <- htmlParse(time_page); time_doc
```




    <!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 3.2 Final">
    <html><body>
    <p>/EN&gt;

    </p>
    <title>What time is it?</title>
    <h2> US Naval Observatory Master Clock Time</h2> <h3><pre>
    <br>Mar. 14, 18:14:26 UTC		Universal Time
    <br>Mar. 14, 02:14:26 PM EDT		Eastern Time
    <br>Mar. 14, 01:14:26 PM CDT		Central Time
    <br>Mar. 14, 12:14:26 PM MDT		Mountain Time
    <br>Mar. 14, 11:14:26 AM PDT		Pacific Time
    <br>Mar. 14, 10:14:26 AM AKDT	Alaska Time
    <br>Mar. 14, 08:14:26 AM HAST	Hawaii-Aleutian Time
    </pre></h3>
    <p><a href="http://www.usno.navy.mil"> US Naval Observatory</a>

    </p>
    </body></html>





```R
# extract everything within the "pre" tag. The // denotes that we are searching the entire document. The [[1]] refers to the fact we are not moving a list to pre but moving the contents of the list.
pre <- xpathSApply(time_doc, "//pre")[[1]]
```


```R
# split along newline \n, divides up each time
values <- strsplit(xmlValue(pre), "\n")[[1]][-1]
```


```R
# split along the tabs \t+ divides each time into time the time and timezone
times <- strsplit(values, "\t+")
```


```R
times
```




    [[1]]
    [1] "Mar. 14, 18:14:26 UTC" "Universal Time"       

    [[2]]
    [1] "Mar. 14, 02:14:26 PM EDT" "Eastern Time"            

    [[3]]
    [1] "Mar. 14, 01:14:26 PM CDT" "Central Time"            

    [[4]]
    [1] "Mar. 14, 12:14:26 PM MDT" "Mountain Time"           

    [[5]]
    [1] "Mar. 14, 11:14:26 AM PDT" "Pacific Time"            

    [[6]]
    [1] "Mar. 14, 10:14:26 AM AKDT" "Alaska Time"              

    [[7]]
    [1] "Mar. 14, 08:14:26 AM HAST" "Hawaii-Aleutian Time"     
