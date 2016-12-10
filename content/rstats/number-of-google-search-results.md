Title: Find Approximate Number Of Google Search Results For A String
Slug: number-of-google-search-results
Summary: Find Approximate Number Of Google Search Results For A String
Date: 2016-05-01 12:00
Category: R Stats
Tags: Other
Authors: Chris Albon


Original source: https://gist.github.com/drewconway/791559


```R
# load the RCurl package
require(RCurl)

# load the xml package
require(XML)
```

    Loading required package: RCurl
    Loading required package: bitops
    Loading required package: XML



```R
# create a google.counts functions
google.counts<-function(s){
  # take the variable "s" and paste it into a google search url
  search.url<-paste("http://www.google.com/search?q=",gsub(" ","+",s),sep="")
  # grab the html contents of the search results page
  search.html<-getURL(search.url)
  # format the html contents
  parse.search<-htmlTreeParse(search.html,useInternalNodes = TRUE)
  # find a div with the id "resultStats"
  search.nodes<-getNodeSet(parse.search,"//div[@id='resultStats']")
  # Take the entire tag, remove tags themselves (xmlValue), seperate every string by the spaces (strsplit), and take the second string (strsplit()[[1]][2]).
  search.value<-strsplit(xmlValue(search.nodes[[1]])," ",fixed=TRUE)[[1]][2]
  # display, as numeric, the number of search results
  return(as.numeric(gsub(",","",search.value,fixed=TRUE)))
}
```


```R
# an example of using the library
google.counts("frogs")
```




    [1] 44200000
