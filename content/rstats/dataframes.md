Title: Data Frames
Slug: dataframes
Summary: Data Frames
Date: 2016-05-01 12:00
Category: R Stats
Tags: Basics
Authors: Chris Albon




```R
# Create two variables of 50 observations, note that we only use 10 month names, because to be combined into a dataset all variables must have the same number of lengths OR be a multiple of the longest length.
percent.sms <- runif(50)
state <- state.name
month <- month.name[1:10]
```


```R
# Create a dataframe of those two variables
usa <- data.frame(state, percent.sms, month)
```


```R
# Find the number of columns in the data frame
length(usa)
```




    [1] 3




```R
# Select the second and third rows of the first two columns
usa[2:3, -3]
```




        state percent.sms
    2  Alaska   0.5466144
    3 Arizona   0.3224463




```R
# Select the second and third rows of the first column
usa[[1]][2:3]
```




    [1] Alaska  Arizona
    50 Levels: Alabama Alaska Arizona Arkansas California Colorado ... Wyoming




```R
# Select the second and third rows of the first column
usa$state[2:3]
```




    [1] Alaska  Arizona
    50 Levels: Alabama Alaska Arizona Arkansas California Colorado ... Wyoming




```R
# Transpose the data frame
usa.t <- t(usa)
```


```R
usa.t
```




                [,1]          [,2]          [,3]          [,4]         
    state       "Alabama"     "Alaska"      "Arizona"     "Arkansas"   
    percent.sms "0.289356397" "0.546614370" "0.322446264" "0.667867042"
    month       "January"     "February"    "March"       "April"      
                [,5]          [,6]          [,7]          [,8]         
    state       "California"  "Colorado"    "Connecticut" "Delaware"   
    percent.sms "0.030940904" "0.515846089" "0.993535078" "0.054146395"
    month       "May"         "June"        "July"        "August"     
                [,9]          [,10]         [,11]         [,12]        
    state       "Florida"     "Georgia"     "Hawaii"      "Idaho"      
    percent.sms "0.713894582" "0.006578350" "0.005815321" "0.422469396"
    month       "September"   "October"     "January"     "February"   
                [,13]         [,14]         [,15]         [,16]        
    state       "Illinois"    "Indiana"     "Iowa"        "Kansas"     
    percent.sms "0.613361941" "0.584833625" "0.574096752" "0.561261341"
    month       "March"       "April"       "May"         "June"       
                [,17]         [,18]         [,19]         [,20]        
    state       "Kentucky"    "Louisiana"   "Maine"       "Maryland"   
    percent.sms "0.915215752" "0.110033265" "0.250408646" "0.508217647"
    month       "July"        "August"      "September"   "October"    
                [,21]           [,22]         [,23]         [,24]        
    state       "Massachusetts" "Michigan"    "Minnesota"   "Mississippi"
    percent.sms "0.274783572"   "0.572157144" "0.839305733" "0.980407253"
    month       "January"       "February"    "March"       "April"      
                [,25]         [,26]         [,27]         [,28]        
    state       "Missouri"    "Montana"     "Nebraska"    "Nevada"     
    percent.sms "0.683278756" "0.211364157" "0.820996565" "0.664138581"
    month       "May"         "June"        "July"        "August"     
                [,29]           [,30]         [,31]         [,32]        
    state       "New Hampshire" "New Jersey"  "New Mexico"  "New York"   
    percent.sms "0.958563818"   "0.479107255" "0.619247351" "0.561255713"
    month       "September"     "October"     "January"     "February"   
                [,33]            [,34]          [,35]         [,36]        
    state       "North Carolina" "North Dakota" "Ohio"        "Oklahoma"   
    percent.sms "0.368069716"    "0.963833767"  "0.945773752" "0.864754913"
    month       "March"          "April"        "May"         "June"       
                [,37]         [,38]          [,39]          [,40]           
    state       "Oregon"      "Pennsylvania" "Rhode Island" "South Carolina"
    percent.sms "0.059036551" "0.424518585"  "0.131782993"  "0.362164821"   
    month       "July"        "August"       "September"    "October"       
                [,41]          [,42]         [,43]         [,44]        
    state       "South Dakota" "Tennessee"   "Texas"       "Utah"       
    percent.sms "0.082731801"  "0.314073189" "0.042029392" "0.466627718"
    month       "January"      "February"    "March"       "April"      
                [,45]         [,46]         [,47]         [,48]          
    state       "Vermont"     "Virginia"    "Washington"  "West Virginia"
    percent.sms "0.560203050" "0.715840876" "0.077936989" "0.814920678"  
    month       "May"         "June"        "July"        "August"       
                [,49]         [,50]        
    state       "Wisconsin"   "Wyoming"    
    percent.sms "0.287602357" "0.953510491"
    month       "September"   "October"    
