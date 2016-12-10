Title: Cleaning Strings
Slug: cleaning-strings
Summary: Cleaning Strings
Date: 2016-05-01 12:00
Category: R Stats
Tags: Data Wrangling
Authors: Chris Albon


Original source: Learning R

R includes grep, grepl, regexpr, sub, and gsub to handle strings. However they can be clunky, so the stringr package provides a "UI" for these functions to making working with them easier.


```R
# Load LearningR package
library(learningr)

# Load english_monarchs data from the LearningR package
data(english_monarchs, package = "learningr")

# Load Stringr Library
library(stringr)
```


```R
# detect commas in the domain variable, meaning that during that time a monarch had multiple territories (domains)
multiple_kingdoms <- str_detect(english_monarchs$domain, fixed(",")); multiple_kingdoms
```




      [1] FALSE FALSE FALSE FALSE FALSE FALSE FALSE FALSE FALSE FALSE FALSE FALSE
     [13] FALSE FALSE FALSE FALSE  TRUE  TRUE  TRUE  TRUE FALSE  TRUE  TRUE  TRUE
     [25]  TRUE  TRUE FALSE FALSE FALSE FALSE FALSE FALSE FALSE FALSE FALSE FALSE
     [37] FALSE FALSE FALSE FALSE FALSE FALSE FALSE FALSE FALSE FALSE FALSE FALSE
     [49] FALSE FALSE FALSE FALSE FALSE FALSE FALSE FALSE FALSE FALSE FALSE FALSE
     [61] FALSE FALSE FALSE FALSE FALSE FALSE FALSE FALSE FALSE FALSE FALSE FALSE
     [73] FALSE FALSE FALSE FALSE FALSE FALSE FALSE FALSE FALSE  TRUE  TRUE  TRUE
     [85]  TRUE  TRUE  TRUE  TRUE  TRUE FALSE FALSE FALSE FALSE FALSE  TRUE FALSE
     [97] FALSE FALSE FALSE FALSE FALSE FALSE FALSE FALSE FALSE FALSE FALSE FALSE
    [109] FALSE FALSE FALSE FALSE FALSE FALSE FALSE FALSE FALSE FALSE FALSE FALSE
    [121] FALSE FALSE FALSE FALSE FALSE FALSE FALSE FALSE FALSE FALSE FALSE FALSE
    [133] FALSE FALSE FALSE FALSE FALSE FALSE FALSE FALSE FALSE FALSE FALSE FALSE
    [145] FALSE FALSE FALSE FALSE FALSE FALSE FALSE FALSE FALSE FALSE FALSE FALSE
    [157] FALSE FALSE FALSE FALSE FALSE FALSE FALSE FALSE FALSE FALSE FALSE FALSE
    [169] FALSE FALSE FALSE FALSE FALSE FALSE FALSE FALSE FALSE FALSE FALSE FALSE
    [181] FALSE FALSE FALSE FALSE FALSE FALSE FALSE FALSE FALSE FALSE FALSE FALSE
    [193] FALSE FALSE FALSE FALSE FALSE FALSE FALSE FALSE FALSE FALSE FALSE FALSE
    [205] FALSE FALSE FALSE FALSE FALSE FALSE FALSE FALSE FALSE FALSE FALSE FALSE
    [217] FALSE FALSE FALSE FALSE FALSE FALSE FALSE FALSE FALSE FALSE FALSE FALSE
    [229] FALSE FALSE FALSE FALSE FALSE FALSE FALSE FALSE FALSE FALSE FALSE FALSE
    [241] FALSE FALSE FALSE FALSE FALSE FALSE FALSE FALSE FALSE FALSE FALSE FALSE
    [253] FALSE FALSE FALSE FALSE FALSE FALSE FALSE




```R
# index domains where multiple_kingdoms is true. Show name and domain columns for those rows where it is true.
english_monarchs[multiple_kingdoms, c("name", "domain")]
```




                              name                    domain
    17                        Offa       East Anglia, Mercia
    18                        Offa East Anglia, Kent, Mercia
    19           Offa and Ecgfrith East Anglia, Kent, Mercia
    20                    Ecgfrith East Anglia, Kent, Mercia
    22                C\u009cnwulf East Anglia, Kent, Mercia
    23   C\u009cnwulf and Cynehelm East Anglia, Kent, Mercia
    24                C\u009cnwulf East Anglia, Kent, Mercia
    25                    Ceolwulf East Anglia, Kent, Mercia
    26                   Beornwulf       East Anglia, Mercia
    82      Ecgbehrt and Æthelwulf              Kent, Wessex
    83      Ecgbehrt and Æthelwulf      Kent, Mercia, Wessex
    84      Ecgbehrt and Æthelwulf              Kent, Wessex
    85    Æthelwulf and Æðelstan I              Kent, Wessex
    86                   Æthelwulf              Kent, Wessex
    87 Æthelwulf and Æðelberht III              Kent, Wessex
    88               Æðelberht III              Kent, Wessex
    89                  Æthelred I              Kent, Wessex
    95                       Oswiu       Mercia, Northumbria




```R
# detect either a comma or an "and" in the ruler variable, meaning that a domain had multiple rulers
multiple_rulers <- str_detect(english_monarchs$name, ",|and")
```


```R
# index domains where multiple rulers was true and that data isn't missing
english_monarchs$name[multiple_rulers & !is.na(multiple_rulers)]

# since individual rulers are split up by a comma or an and, we can split them up. The output is a list.
individual_rulers <- str_split(english_monarchs$name, ", | and ")
```




     [1] Sigeberht and Ecgric                       
     [2] Hun, Beonna and Alberht                    
     [3] Offa and Ecgfrith                          
     [4] C\u009cnwulf and Cynehelm                  
     [5] Sighere and Sebbi                          
     [6] Sigeheard and Swaefred                     
     [7] Eorcenberht and Eormenred                  
     [8] Oswine, Swæfbehrt, Swæfheard               
     [9] Swæfbehrt, Swæfheard, Wihtred              
    [10] Æðelberht II, Ælfric and Eadberht I        
    [11] Æðelberht II and Eardwulf                  
    [12] Eadberht II, Eanmund and Sigered           
    [13] Heaberht and Ecgbehrt II                   
    [14] Ecgbehrt and Æthelwulf                     
    [15] Ecgbehrt and Æthelwulf                     
    [16] Ecgbehrt and Æthelwulf                     
    [17] Æthelwulf and Æðelstan I                   
    [18] Æthelwulf and Æðelberht III                
    [19] Penda and Eowa                             
    [20] Penda and Peada                            
    [21] Æthelred, Lord of the Mercians             
    [22] Æthelflæd, Lady of the Mercians            
    [23] Ælfwynn, Second Lady of the Mercians       
    [24] Hálfdan and Eowils                         
    [25] Noðhelm and Watt                           
    [26] Noðhelm and Bryni                          
    [27] Noðhelm and Osric                          
    [28] Noðhelm and Æðelstan                       
    [29] Ælfwald, Oslac and Osmund                  
    [30] Ælfwald, Ealdwulf, Oslac and Osmund        
    [31] Ælfwald, Ealdwulf, Oslac, Osmund and Oswald
    [32] Cenwalh and Seaxburh                       
    211 Levels: Adda Æðelbehrt Æðelberht I ... Wulfhere




```R
# take a look at the data
head(individual_rulers[sapply(individual_rulers, length) > 1])
```




    [[1]]
    [1] "Sigeberht" "Ecgric"   

    [[2]]
    [1] "Hun"     "Beonna"  "Alberht"

    [[3]]
    [1] "Offa"     "Ecgfrith"

    [[4]]
    [1] "C\u009cnwulf" "Cynehelm"    

    [[5]]
    [1] "Sighere" "Sebbi"  

    [[6]]
    [1] "Sigeheard" "Swaefred"
