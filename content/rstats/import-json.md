Title: Importing a JSON file into R
Slug: import-json
Summary: Importing a JSON file into R
Date: 2016-05-01 12:00
Category: R Stats
Tags: Data Wrangling
Authors: Chris Albon



Source: http://stackoverflow.com/questions/13004813/downloading-json-data-into-r?lq=1


```R
# Load libraries
library(RJSONIO)
library(RCurl)
```


```R
# grab the data
raw_data <- getURL("http://swapi.co/api/people/1/?format=json")
```


```R
# Then covert from JSON into a list in R
data <- fromJSON(raw_data)
length(data)
```


```R
# We can coerce this to a data.frame
final_data <- do.call(rbind, data)
```


```R
# Then write it to a flat csv file
# write.csv(final_data, "final_data.csv")
```




    [1] 16




```R
final_data
```




               [,1]                               
    name       "Luke Skywalker"                   
    height     "172"                              
    mass       "77"                               
    hair_color "blond"                            
    skin_color "fair"                             
    eye_color  "blue"                             
    birth_year "19BBY"                            
    gender     "male"                             
    homeworld  "http://swapi.co/api/planets/1/"   
    films      "http://swapi.co/api/films/1/"     
    species    "http://swapi.co/api/species/1/"   
    vehicles   "http://swapi.co/api/vehicles/14/"
    starships  "http://swapi.co/api/starships/12/"
    created    "2014-12-09T13:50:51.644000Z"      
    edited     "2014-12-20T21:17:56.891000Z"      
    url        "http://swapi.co/api/people/1/"    
               [,2]                               
    name       "Luke Skywalker"                   
    height     "172"                              
    mass       "77"                               
    hair_color "blond"                            
    skin_color "fair"                             
    eye_color  "blue"                             
    birth_year "19BBY"                            
    gender     "male"                             
    homeworld  "http://swapi.co/api/planets/1/"   
    films      "http://swapi.co/api/films/2/"     
    species    "http://swapi.co/api/species/1/"   
    vehicles   "http://swapi.co/api/vehicles/30/"
    starships  "http://swapi.co/api/starships/22/"
    created    "2014-12-09T13:50:51.644000Z"      
    edited     "2014-12-20T21:17:56.891000Z"      
    url        "http://swapi.co/api/people/1/"    
               [,3]                               
    name       "Luke Skywalker"                   
    height     "172"                              
    mass       "77"                               
    hair_color "blond"                            
    skin_color "fair"                             
    eye_color  "blue"                             
    birth_year "19BBY"                            
    gender     "male"                             
    homeworld  "http://swapi.co/api/planets/1/"   
    films      "http://swapi.co/api/films/3/"     
    species    "http://swapi.co/api/species/1/"   
    vehicles   "http://swapi.co/api/vehicles/14/"
    starships  "http://swapi.co/api/starships/12/"
    created    "2014-12-09T13:50:51.644000Z"      
    edited     "2014-12-20T21:17:56.891000Z"      
    url        "http://swapi.co/api/people/1/"    
               [,4]                               
    name       "Luke Skywalker"                   
    height     "172"                              
    mass       "77"                               
    hair_color "blond"                            
    skin_color "fair"                             
    eye_color  "blue"                             
    birth_year "19BBY"                            
    gender     "male"                             
    homeworld  "http://swapi.co/api/planets/1/"   
    films      "http://swapi.co/api/films/6/"     
    species    "http://swapi.co/api/species/1/"   
    vehicles   "http://swapi.co/api/vehicles/30/"
    starships  "http://swapi.co/api/starships/22/"
    created    "2014-12-09T13:50:51.644000Z"      
    edited     "2014-12-20T21:17:56.891000Z"      
    url        "http://swapi.co/api/people/1/"    
