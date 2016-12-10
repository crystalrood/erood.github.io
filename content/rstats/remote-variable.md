Title: Removing Variables
Slug: remote-variable
Summary: Removing Variables
Date: 2016-05-01 12:00
Category: R Stats
Tags: Basics
Authors: Chris Albon




```R
# Create two variables of 50 observations
percent.sms <- runif(50)
location <- state.name
```


```R
percent.sms
location
```




     [1] 0.58913023 0.54043206 0.14073087 0.68065186 0.74324175 0.75807962
     [7] 0.29425877 0.27024361 0.95795936 0.59034216 0.56754098 0.59455496
    [13] 0.21656371 0.60917559 0.73271437 0.22795936 0.45305943 0.42421408
    [19] 0.40083340 0.17028350 0.88662551 0.17400449 0.42711263 0.10408158
    [25] 0.43336437 0.32618460 0.90744570 0.53893304 0.36471753 0.29214559
    [31] 0.91914909 0.83578129 0.10637126 0.15559371 0.35368828 0.19322608
    [37] 0.23442976 0.33605854 0.17083567 0.87818844 0.51282318 0.89569921
    [43] 0.65206229 0.06575875 0.81599312 0.99551732 0.04941348 0.80749258
    [49] 0.68767939 0.21466972






     [1] "Alabama"        "Alaska"         "Arizona"        "Arkansas"      
     [5] "California"     "Colorado"       "Connecticut"    "Delaware"      
     [9] "Florida"        "Georgia"        "Hawaii"         "Idaho"         
    [13] "Illinois"       "Indiana"        "Iowa"           "Kansas"        
    [17] "Kentucky"       "Louisiana"      "Maine"          "Maryland"      
    [21] "Massachusetts"  "Michigan"       "Minnesota"      "Mississippi"   
    [25] "Missouri"       "Montana"        "Nebraska"       "Nevada"        
    [29] "New Hampshire"  "New Jersey"     "New Mexico"     "New York"      
    [33] "North Carolina" "North Dakota"   "Ohio"           "Oklahoma"      
    [37] "Oregon"         "Pennsylvania"   "Rhode Island"   "South Carolina"
    [41] "South Dakota"   "Tennessee"      "Texas"          "Utah"          
    [45] "Vermont"        "Virginia"       "Washington"     "West Virginia"
    [49] "Wisconsin"      "Wyoming"       




```R
# Remove the location variable
rm(location)
```


```R
percent.sms
location
```




     [1] 0.58913023 0.54043206 0.14073087 0.68065186 0.74324175 0.75807962
     [7] 0.29425877 0.27024361 0.95795936 0.59034216 0.56754098 0.59455496
    [13] 0.21656371 0.60917559 0.73271437 0.22795936 0.45305943 0.42421408
    [19] 0.40083340 0.17028350 0.88662551 0.17400449 0.42711263 0.10408158
    [25] 0.43336437 0.32618460 0.90744570 0.53893304 0.36471753 0.29214559
    [31] 0.91914909 0.83578129 0.10637126 0.15559371 0.35368828 0.19322608
    [37] 0.23442976 0.33605854 0.17083567 0.87818844 0.51282318 0.89569921
    [43] 0.65206229 0.06575875 0.81599312 0.99551732 0.04941348 0.80749258
    [49] 0.68767939 0.21466972




    Error in eval(expr, envir, enclos): object 'location' not found
