Title: Import XML
Slug: import-xml
Summary: Import XML
Date: 2016-05-01 12:00
Category: R Stats
Tags: Data Wrangling
Authors: Chris Albon


Original source: http://giventhedata.blogspot.com/2012/06/r-and-web-for-beginners-part-ii-xml-in.html


```R
# load XML library
library(XML)
```


```R
# save the URL as a string element
xml.url <- "http://www.w3schools.com/xml/plant_catalog.xml"
```


```R
# parse the xml file from the web
xmlfile <- xmlTreeParse(xml.url); xmlfile
```




    $doc
    $file
    [1] "http://www.w3schools.com/xml/plant_catalog.xml"

    $version
    [1] "1.0"

    $children
    $children$CATALOG
    <CATALOG>
     <PLANT>
      <COMMON>Bloodroot</COMMON>
      <BOTANICAL>Sanguinaria canadensis</BOTANICAL>
      <ZONE>4</ZONE>
      <LIGHT>Mostly Shady</LIGHT>
      <PRICE>$2.44</PRICE>
      <AVAILABILITY>031599</AVAILABILITY>
     </PLANT>
     <PLANT>
      <COMMON>Columbine</COMMON>
      <BOTANICAL>Aquilegia canadensis</BOTANICAL>
      <ZONE>3</ZONE>
      <LIGHT>Mostly Shady</LIGHT>
      <PRICE>$9.37</PRICE>
      <AVAILABILITY>030699</AVAILABILITY>
     </PLANT>
     <PLANT>
      <COMMON>Marsh Marigold</COMMON>
      <BOTANICAL>Caltha palustris</BOTANICAL>
      <ZONE>4</ZONE>
      <LIGHT>Mostly Sunny</LIGHT>
      <PRICE>$6.81</PRICE>
      <AVAILABILITY>051799</AVAILABILITY>
     </PLANT>
     <PLANT>
      <COMMON>Cowslip</COMMON>
      <BOTANICAL>Caltha palustris</BOTANICAL>
      <ZONE>4</ZONE>
      <LIGHT>Mostly Shady</LIGHT>
      <PRICE>$9.90</PRICE>
      <AVAILABILITY>030699</AVAILABILITY>
     </PLANT>
     <PLANT>
      <COMMON>Dutchman&apos;s-Breeches</COMMON>
      <BOTANICAL>Dicentra cucullaria</BOTANICAL>
      <ZONE>3</ZONE>
      <LIGHT>Mostly Shady</LIGHT>
      <PRICE>$6.44</PRICE>
      <AVAILABILITY>012099</AVAILABILITY>
     </PLANT>
     <PLANT>
      <COMMON>Ginger, Wild</COMMON>
      <BOTANICAL>Asarum canadense</BOTANICAL>
      <ZONE>3</ZONE>
      <LIGHT>Mostly Shady</LIGHT>
      <PRICE>$9.03</PRICE>
      <AVAILABILITY>041899</AVAILABILITY>
     </PLANT>
     <PLANT>
      <COMMON>Hepatica</COMMON>
      <BOTANICAL>Hepatica americana</BOTANICAL>
      <ZONE>4</ZONE>
      <LIGHT>Mostly Shady</LIGHT>
      <PRICE>$4.45</PRICE>
      <AVAILABILITY>012699</AVAILABILITY>
     </PLANT>
     <PLANT>
      <COMMON>Liverleaf</COMMON>
      <BOTANICAL>Hepatica americana</BOTANICAL>
      <ZONE>4</ZONE>
      <LIGHT>Mostly Shady</LIGHT>
      <PRICE>$3.99</PRICE>
      <AVAILABILITY>010299</AVAILABILITY>
     </PLANT>
     <PLANT>
      <COMMON>Jack-In-The-Pulpit</COMMON>
      <BOTANICAL>Arisaema triphyllum</BOTANICAL>
      <ZONE>4</ZONE>
      <LIGHT>Mostly Shady</LIGHT>
      <PRICE>$3.23</PRICE>
      <AVAILABILITY>020199</AVAILABILITY>
     </PLANT>
     <PLANT>
      <COMMON>Mayapple</COMMON>
      <BOTANICAL>Podophyllum peltatum</BOTANICAL>
      <ZONE>3</ZONE>
      <LIGHT>Mostly Shady</LIGHT>
      <PRICE>$2.98</PRICE>
      <AVAILABILITY>060599</AVAILABILITY>
     </PLANT>
     <PLANT>
      <COMMON>Phlox, Woodland</COMMON>
      <BOTANICAL>Phlox divaricata</BOTANICAL>
      <ZONE>3</ZONE>
      <LIGHT>Sun or Shade</LIGHT>
      <PRICE>$2.80</PRICE>
      <AVAILABILITY>012299</AVAILABILITY>
     </PLANT>
     <PLANT>
      <COMMON>Phlox, Blue</COMMON>
      <BOTANICAL>Phlox divaricata</BOTANICAL>
      <ZONE>3</ZONE>
      <LIGHT>Sun or Shade</LIGHT>
      <PRICE>$5.59</PRICE>
      <AVAILABILITY>021699</AVAILABILITY>
     </PLANT>
     <PLANT>
      <COMMON>Spring-Beauty</COMMON>
      <BOTANICAL>Claytonia Virginica</BOTANICAL>
      <ZONE>7</ZONE>
      <LIGHT>Mostly Shady</LIGHT>
      <PRICE>$6.59</PRICE>
      <AVAILABILITY>020199</AVAILABILITY>
     </PLANT>
     <PLANT>
      <COMMON>Trillium</COMMON>
      <BOTANICAL>Trillium grandiflorum</BOTANICAL>
      <ZONE>5</ZONE>
      <LIGHT>Sun or Shade</LIGHT>
      <PRICE>$3.90</PRICE>
      <AVAILABILITY>042999</AVAILABILITY>
     </PLANT>
     <PLANT>
      <COMMON>Wake Robin</COMMON>
      <BOTANICAL>Trillium grandiflorum</BOTANICAL>
      <ZONE>5</ZONE>
      <LIGHT>Sun or Shade</LIGHT>
      <PRICE>$3.20</PRICE>
      <AVAILABILITY>022199</AVAILABILITY>
     </PLANT>
     <PLANT>
      <COMMON>Violet, Dog-Tooth</COMMON>
      <BOTANICAL>Erythronium americanum</BOTANICAL>
      <ZONE>4</ZONE>
      <LIGHT>Shade</LIGHT>
      <PRICE>$9.04</PRICE>
      <AVAILABILITY>020199</AVAILABILITY>
     </PLANT>
     <PLANT>
      <COMMON>Trout Lily</COMMON>
      <BOTANICAL>Erythronium americanum</BOTANICAL>
      <ZONE>4</ZONE>
      <LIGHT>Shade</LIGHT>
      <PRICE>$6.94</PRICE>
      <AVAILABILITY>032499</AVAILABILITY>
     </PLANT>
     <PLANT>
      <COMMON>Adder&apos;s-Tongue</COMMON>
      <BOTANICAL>Erythronium americanum</BOTANICAL>
      <ZONE>4</ZONE>
      <LIGHT>Shade</LIGHT>
      <PRICE>$9.58</PRICE>
      <AVAILABILITY>041399</AVAILABILITY>
     </PLANT>
     <PLANT>
      <COMMON>Anemone</COMMON>
      <BOTANICAL>Anemone blanda</BOTANICAL>
      <ZONE>6</ZONE>
      <LIGHT>Mostly Shady</LIGHT>
      <PRICE>$8.86</PRICE>
      <AVAILABILITY>122698</AVAILABILITY>
     </PLANT>
     <PLANT>
      <COMMON>Grecian Windflower</COMMON>
      <BOTANICAL>Anemone blanda</BOTANICAL>
      <ZONE>6</ZONE>
      <LIGHT>Mostly Shady</LIGHT>
      <PRICE>$9.16</PRICE>
      <AVAILABILITY>071099</AVAILABILITY>
     </PLANT>
     <PLANT>
      <COMMON>Bee Balm</COMMON>
      <BOTANICAL>Monarda didyma</BOTANICAL>
      <ZONE>4</ZONE>
      <LIGHT>Shade</LIGHT>
      <PRICE>$4.59</PRICE>
      <AVAILABILITY>050399</AVAILABILITY>
     </PLANT>
     <PLANT>
      <COMMON>Bergamot</COMMON>
      <BOTANICAL>Monarda didyma</BOTANICAL>
      <ZONE>4</ZONE>
      <LIGHT>Shade</LIGHT>
      <PRICE>$7.16</PRICE>
      <AVAILABILITY>042799</AVAILABILITY>
     </PLANT>
     <PLANT>
      <COMMON>Black-Eyed Susan</COMMON>
      <BOTANICAL>Rudbeckia hirta</BOTANICAL>
      <ZONE>Annual</ZONE>
      <LIGHT>Sunny</LIGHT>
      <PRICE>$9.80</PRICE>
      <AVAILABILITY>061899</AVAILABILITY>
     </PLANT>
     <PLANT>
      <COMMON>Buttercup</COMMON>
      <BOTANICAL>Ranunculus</BOTANICAL>
      <ZONE>4</ZONE>
      <LIGHT>Shade</LIGHT>
      <PRICE>$2.57</PRICE>
      <AVAILABILITY>061099</AVAILABILITY>
     </PLANT>
     <PLANT>
      <COMMON>Crowfoot</COMMON>
      <BOTANICAL>Ranunculus</BOTANICAL>
      <ZONE>4</ZONE>
      <LIGHT>Shade</LIGHT>
      <PRICE>$9.34</PRICE>
      <AVAILABILITY>040399</AVAILABILITY>
     </PLANT>
     <PLANT>
      <COMMON>Butterfly Weed</COMMON>
      <BOTANICAL>Asclepias tuberosa</BOTANICAL>
      <ZONE>Annual</ZONE>
      <LIGHT>Sunny</LIGHT>
      <PRICE>$2.78</PRICE>
      <AVAILABILITY>063099</AVAILABILITY>
     </PLANT>
     <PLANT>
      <COMMON>Cinquefoil</COMMON>
      <BOTANICAL>Potentilla</BOTANICAL>
      <ZONE>Annual</ZONE>
      <LIGHT>Shade</LIGHT>
      <PRICE>$7.06</PRICE>
      <AVAILABILITY>052599</AVAILABILITY>
     </PLANT>
     <PLANT>
      <COMMON>Primrose</COMMON>
      <BOTANICAL>Oenothera</BOTANICAL>
      <ZONE>3 - 5</ZONE>
      <LIGHT>Sunny</LIGHT>
      <PRICE>$6.56</PRICE>
      <AVAILABILITY>013099</AVAILABILITY>
     </PLANT>
     <PLANT>
      <COMMON>Gentian</COMMON>
      <BOTANICAL>Gentiana</BOTANICAL>
      <ZONE>4</ZONE>
      <LIGHT>Sun or Shade</LIGHT>
      <PRICE>$7.81</PRICE>
      <AVAILABILITY>051899</AVAILABILITY>
     </PLANT>
     <PLANT>
      <COMMON>Blue Gentian</COMMON>
      <BOTANICAL>Gentiana</BOTANICAL>
      <ZONE>4</ZONE>
      <LIGHT>Sun or Shade</LIGHT>
      <PRICE>$8.56</PRICE>
      <AVAILABILITY>050299</AVAILABILITY>
     </PLANT>
     <PLANT>
      <COMMON>Jacob&apos;s Ladder</COMMON>
      <BOTANICAL>Polemonium caeruleum</BOTANICAL>
      <ZONE>Annual</ZONE>
      <LIGHT>Shade</LIGHT>
      <PRICE>$9.26</PRICE>
      <AVAILABILITY>022199</AVAILABILITY>
     </PLANT>
     <PLANT>
      <COMMON>Greek Valerian</COMMON>
      <BOTANICAL>Polemonium caeruleum</BOTANICAL>
      <ZONE>Annual</ZONE>
      <LIGHT>Shade</LIGHT>
      <PRICE>$4.36</PRICE>
      <AVAILABILITY>071499</AVAILABILITY>
     </PLANT>
     <PLANT>
      <COMMON>California Poppy</COMMON>
      <BOTANICAL>Eschscholzia californica</BOTANICAL>
      <ZONE>Annual</ZONE>
      <LIGHT>Sun</LIGHT>
      <PRICE>$7.89</PRICE>
      <AVAILABILITY>032799</AVAILABILITY>
     </PLANT>
     <PLANT>
      <COMMON>Shooting Star</COMMON>
      <BOTANICAL>Dodecatheon</BOTANICAL>
      <ZONE>Annual</ZONE>
      <LIGHT>Mostly Shady</LIGHT>
      <PRICE>$8.60</PRICE>
      <AVAILABILITY>051399</AVAILABILITY>
     </PLANT>
     <PLANT>
      <COMMON>Snakeroot</COMMON>
      <BOTANICAL>Cimicifuga</BOTANICAL>
      <ZONE>Annual</ZONE>
      <LIGHT>Shade</LIGHT>
      <PRICE>$5.63</PRICE>
      <AVAILABILITY>071199</AVAILABILITY>
     </PLANT>
     <PLANT>
      <COMMON>Cardinal Flower</COMMON>
      <BOTANICAL>Lobelia cardinalis</BOTANICAL>
      <ZONE>2</ZONE>
      <LIGHT>Shade</LIGHT>
      <PRICE>$3.02</PRICE>
      <AVAILABILITY>022299</AVAILABILITY>
     </PLANT>
    </CATALOG>


    attr(,"class")
    [1] "XMLDocumentContent"

    $dtd
    $external
    NULL

    $internal
    NULL

    attr(,"class")
    [1] "DTDList"

    attr(,"class")
    [1] "XMLDocument"         "XMLAbstractDocument"




```R
# access the top node, skipping over DTD and the comment. In other words, get straight to the data and ignore the other stuff.
xmltop <- xmlRoot(xmlfile); xmltop
```




    <CATALOG>
     <PLANT>
      <COMMON>Bloodroot</COMMON>
      <BOTANICAL>Sanguinaria canadensis</BOTANICAL>
      <ZONE>4</ZONE>
      <LIGHT>Mostly Shady</LIGHT>
      <PRICE>$2.44</PRICE>
      <AVAILABILITY>031599</AVAILABILITY>
     </PLANT>
     <PLANT>
      <COMMON>Columbine</COMMON>
      <BOTANICAL>Aquilegia canadensis</BOTANICAL>
      <ZONE>3</ZONE>
      <LIGHT>Mostly Shady</LIGHT>
      <PRICE>$9.37</PRICE>
      <AVAILABILITY>030699</AVAILABILITY>
     </PLANT>
     <PLANT>
      <COMMON>Marsh Marigold</COMMON>
      <BOTANICAL>Caltha palustris</BOTANICAL>
      <ZONE>4</ZONE>
      <LIGHT>Mostly Sunny</LIGHT>
      <PRICE>$6.81</PRICE>
      <AVAILABILITY>051799</AVAILABILITY>
     </PLANT>
     <PLANT>
      <COMMON>Cowslip</COMMON>
      <BOTANICAL>Caltha palustris</BOTANICAL>
      <ZONE>4</ZONE>
      <LIGHT>Mostly Shady</LIGHT>
      <PRICE>$9.90</PRICE>
      <AVAILABILITY>030699</AVAILABILITY>
     </PLANT>
     <PLANT>
      <COMMON>Dutchman&apos;s-Breeches</COMMON>
      <BOTANICAL>Dicentra cucullaria</BOTANICAL>
      <ZONE>3</ZONE>
      <LIGHT>Mostly Shady</LIGHT>
      <PRICE>$6.44</PRICE>
      <AVAILABILITY>012099</AVAILABILITY>
     </PLANT>
     <PLANT>
      <COMMON>Ginger, Wild</COMMON>
      <BOTANICAL>Asarum canadense</BOTANICAL>
      <ZONE>3</ZONE>
      <LIGHT>Mostly Shady</LIGHT>
      <PRICE>$9.03</PRICE>
      <AVAILABILITY>041899</AVAILABILITY>
     </PLANT>
     <PLANT>
      <COMMON>Hepatica</COMMON>
      <BOTANICAL>Hepatica americana</BOTANICAL>
      <ZONE>4</ZONE>
      <LIGHT>Mostly Shady</LIGHT>
      <PRICE>$4.45</PRICE>
      <AVAILABILITY>012699</AVAILABILITY>
     </PLANT>
     <PLANT>
      <COMMON>Liverleaf</COMMON>
      <BOTANICAL>Hepatica americana</BOTANICAL>
      <ZONE>4</ZONE>
      <LIGHT>Mostly Shady</LIGHT>
      <PRICE>$3.99</PRICE>
      <AVAILABILITY>010299</AVAILABILITY>
     </PLANT>
     <PLANT>
      <COMMON>Jack-In-The-Pulpit</COMMON>
      <BOTANICAL>Arisaema triphyllum</BOTANICAL>
      <ZONE>4</ZONE>
      <LIGHT>Mostly Shady</LIGHT>
      <PRICE>$3.23</PRICE>
      <AVAILABILITY>020199</AVAILABILITY>
     </PLANT>
     <PLANT>
      <COMMON>Mayapple</COMMON>
      <BOTANICAL>Podophyllum peltatum</BOTANICAL>
      <ZONE>3</ZONE>
      <LIGHT>Mostly Shady</LIGHT>
      <PRICE>$2.98</PRICE>
      <AVAILABILITY>060599</AVAILABILITY>
     </PLANT>
     <PLANT>
      <COMMON>Phlox, Woodland</COMMON>
      <BOTANICAL>Phlox divaricata</BOTANICAL>
      <ZONE>3</ZONE>
      <LIGHT>Sun or Shade</LIGHT>
      <PRICE>$2.80</PRICE>
      <AVAILABILITY>012299</AVAILABILITY>
     </PLANT>
     <PLANT>
      <COMMON>Phlox, Blue</COMMON>
      <BOTANICAL>Phlox divaricata</BOTANICAL>
      <ZONE>3</ZONE>
      <LIGHT>Sun or Shade</LIGHT>
      <PRICE>$5.59</PRICE>
      <AVAILABILITY>021699</AVAILABILITY>
     </PLANT>
     <PLANT>
      <COMMON>Spring-Beauty</COMMON>
      <BOTANICAL>Claytonia Virginica</BOTANICAL>
      <ZONE>7</ZONE>
      <LIGHT>Mostly Shady</LIGHT>
      <PRICE>$6.59</PRICE>
      <AVAILABILITY>020199</AVAILABILITY>
     </PLANT>
     <PLANT>
      <COMMON>Trillium</COMMON>
      <BOTANICAL>Trillium grandiflorum</BOTANICAL>
      <ZONE>5</ZONE>
      <LIGHT>Sun or Shade</LIGHT>
      <PRICE>$3.90</PRICE>
      <AVAILABILITY>042999</AVAILABILITY>
     </PLANT>
     <PLANT>
      <COMMON>Wake Robin</COMMON>
      <BOTANICAL>Trillium grandiflorum</BOTANICAL>
      <ZONE>5</ZONE>
      <LIGHT>Sun or Shade</LIGHT>
      <PRICE>$3.20</PRICE>
      <AVAILABILITY>022199</AVAILABILITY>
     </PLANT>
     <PLANT>
      <COMMON>Violet, Dog-Tooth</COMMON>
      <BOTANICAL>Erythronium americanum</BOTANICAL>
      <ZONE>4</ZONE>
      <LIGHT>Shade</LIGHT>
      <PRICE>$9.04</PRICE>
      <AVAILABILITY>020199</AVAILABILITY>
     </PLANT>
     <PLANT>
      <COMMON>Trout Lily</COMMON>
      <BOTANICAL>Erythronium americanum</BOTANICAL>
      <ZONE>4</ZONE>
      <LIGHT>Shade</LIGHT>
      <PRICE>$6.94</PRICE>
      <AVAILABILITY>032499</AVAILABILITY>
     </PLANT>
     <PLANT>
      <COMMON>Adder&apos;s-Tongue</COMMON>
      <BOTANICAL>Erythronium americanum</BOTANICAL>
      <ZONE>4</ZONE>
      <LIGHT>Shade</LIGHT>
      <PRICE>$9.58</PRICE>
      <AVAILABILITY>041399</AVAILABILITY>
     </PLANT>
     <PLANT>
      <COMMON>Anemone</COMMON>
      <BOTANICAL>Anemone blanda</BOTANICAL>
      <ZONE>6</ZONE>
      <LIGHT>Mostly Shady</LIGHT>
      <PRICE>$8.86</PRICE>
      <AVAILABILITY>122698</AVAILABILITY>
     </PLANT>
     <PLANT>
      <COMMON>Grecian Windflower</COMMON>
      <BOTANICAL>Anemone blanda</BOTANICAL>
      <ZONE>6</ZONE>
      <LIGHT>Mostly Shady</LIGHT>
      <PRICE>$9.16</PRICE>
      <AVAILABILITY>071099</AVAILABILITY>
     </PLANT>
     <PLANT>
      <COMMON>Bee Balm</COMMON>
      <BOTANICAL>Monarda didyma</BOTANICAL>
      <ZONE>4</ZONE>
      <LIGHT>Shade</LIGHT>
      <PRICE>$4.59</PRICE>
      <AVAILABILITY>050399</AVAILABILITY>
     </PLANT>
     <PLANT>
      <COMMON>Bergamot</COMMON>
      <BOTANICAL>Monarda didyma</BOTANICAL>
      <ZONE>4</ZONE>
      <LIGHT>Shade</LIGHT>
      <PRICE>$7.16</PRICE>
      <AVAILABILITY>042799</AVAILABILITY>
     </PLANT>
     <PLANT>
      <COMMON>Black-Eyed Susan</COMMON>
      <BOTANICAL>Rudbeckia hirta</BOTANICAL>
      <ZONE>Annual</ZONE>
      <LIGHT>Sunny</LIGHT>
      <PRICE>$9.80</PRICE>
      <AVAILABILITY>061899</AVAILABILITY>
     </PLANT>
     <PLANT>
      <COMMON>Buttercup</COMMON>
      <BOTANICAL>Ranunculus</BOTANICAL>
      <ZONE>4</ZONE>
      <LIGHT>Shade</LIGHT>
      <PRICE>$2.57</PRICE>
      <AVAILABILITY>061099</AVAILABILITY>
     </PLANT>
     <PLANT>
      <COMMON>Crowfoot</COMMON>
      <BOTANICAL>Ranunculus</BOTANICAL>
      <ZONE>4</ZONE>
      <LIGHT>Shade</LIGHT>
      <PRICE>$9.34</PRICE>
      <AVAILABILITY>040399</AVAILABILITY>
     </PLANT>
     <PLANT>
      <COMMON>Butterfly Weed</COMMON>
      <BOTANICAL>Asclepias tuberosa</BOTANICAL>
      <ZONE>Annual</ZONE>
      <LIGHT>Sunny</LIGHT>
      <PRICE>$2.78</PRICE>
      <AVAILABILITY>063099</AVAILABILITY>
     </PLANT>
     <PLANT>
      <COMMON>Cinquefoil</COMMON>
      <BOTANICAL>Potentilla</BOTANICAL>
      <ZONE>Annual</ZONE>
      <LIGHT>Shade</LIGHT>
      <PRICE>$7.06</PRICE>
      <AVAILABILITY>052599</AVAILABILITY>
     </PLANT>
     <PLANT>
      <COMMON>Primrose</COMMON>
      <BOTANICAL>Oenothera</BOTANICAL>
      <ZONE>3 - 5</ZONE>
      <LIGHT>Sunny</LIGHT>
      <PRICE>$6.56</PRICE>
      <AVAILABILITY>013099</AVAILABILITY>
     </PLANT>
     <PLANT>
      <COMMON>Gentian</COMMON>
      <BOTANICAL>Gentiana</BOTANICAL>
      <ZONE>4</ZONE>
      <LIGHT>Sun or Shade</LIGHT>
      <PRICE>$7.81</PRICE>
      <AVAILABILITY>051899</AVAILABILITY>
     </PLANT>
     <PLANT>
      <COMMON>Blue Gentian</COMMON>
      <BOTANICAL>Gentiana</BOTANICAL>
      <ZONE>4</ZONE>
      <LIGHT>Sun or Shade</LIGHT>
      <PRICE>$8.56</PRICE>
      <AVAILABILITY>050299</AVAILABILITY>
     </PLANT>
     <PLANT>
      <COMMON>Jacob&apos;s Ladder</COMMON>
      <BOTANICAL>Polemonium caeruleum</BOTANICAL>
      <ZONE>Annual</ZONE>
      <LIGHT>Shade</LIGHT>
      <PRICE>$9.26</PRICE>
      <AVAILABILITY>022199</AVAILABILITY>
     </PLANT>
     <PLANT>
      <COMMON>Greek Valerian</COMMON>
      <BOTANICAL>Polemonium caeruleum</BOTANICAL>
      <ZONE>Annual</ZONE>
      <LIGHT>Shade</LIGHT>
      <PRICE>$4.36</PRICE>
      <AVAILABILITY>071499</AVAILABILITY>
     </PLANT>
     <PLANT>
      <COMMON>California Poppy</COMMON>
      <BOTANICAL>Eschscholzia californica</BOTANICAL>
      <ZONE>Annual</ZONE>
      <LIGHT>Sun</LIGHT>
      <PRICE>$7.89</PRICE>
      <AVAILABILITY>032799</AVAILABILITY>
     </PLANT>
     <PLANT>
      <COMMON>Shooting Star</COMMON>
      <BOTANICAL>Dodecatheon</BOTANICAL>
      <ZONE>Annual</ZONE>
      <LIGHT>Mostly Shady</LIGHT>
      <PRICE>$8.60</PRICE>
      <AVAILABILITY>051399</AVAILABILITY>
     </PLANT>
     <PLANT>
      <COMMON>Snakeroot</COMMON>
      <BOTANICAL>Cimicifuga</BOTANICAL>
      <ZONE>Annual</ZONE>
      <LIGHT>Shade</LIGHT>
      <PRICE>$5.63</PRICE>
      <AVAILABILITY>071199</AVAILABILITY>
     </PLANT>
     <PLANT>
      <COMMON>Cardinal Flower</COMMON>
      <BOTANICAL>Lobelia cardinalis</BOTANICAL>
      <ZONE>2</ZONE>
      <LIGHT>Shade</LIGHT>
      <PRICE>$3.02</PRICE>
      <AVAILABILITY>022299</AVAILABILITY>
     </PLANT>
    </CATALOG>




```R
# extract XML-values with xmlSApply. More specifically, this turns each $PLANT node into it's own row, each tag into a column, and each value within the tag into an element
plantcat <- xmlSApply(xmltop, function(x) xmlSApply(x, xmlValue)); plantcat
```




                 PLANT                    PLANT                  PLANT             
    COMMON       "Bloodroot"              "Columbine"            "Marsh Marigold"  
    BOTANICAL    "Sanguinaria canadensis" "Aquilegia canadensis" "Caltha palustris"
    ZONE         "4"                      "3"                    "4"               
    LIGHT        "Mostly Shady"           "Mostly Shady"         "Mostly Sunny"    
    PRICE        "$2.44"                  "$9.37"                "$6.81"           
    AVAILABILITY "031599"                 "030699"               "051799"          
                 PLANT              PLANT                 PLANT             
    COMMON       "Cowslip"          "Dutchman's-Breeches" "Ginger, Wild"    
    BOTANICAL    "Caltha palustris" "Dicentra cucullaria" "Asarum canadense"
    ZONE         "4"                "3"                   "3"               
    LIGHT        "Mostly Shady"     "Mostly Shady"        "Mostly Shady"    
    PRICE        "$9.90"            "$6.44"               "$9.03"           
    AVAILABILITY "030699"           "012099"              "041899"          
                 PLANT                PLANT                PLANT                
    COMMON       "Hepatica"           "Liverleaf"          "Jack-In-The-Pulpit"
    BOTANICAL    "Hepatica americana" "Hepatica americana" "Arisaema triphyllum"
    ZONE         "4"                  "4"                  "4"                  
    LIGHT        "Mostly Shady"       "Mostly Shady"       "Mostly Shady"       
    PRICE        "$4.45"              "$3.99"              "$3.23"              
    AVAILABILITY "012699"             "010299"             "020199"             
                 PLANT                  PLANT              PLANT             
    COMMON       "Mayapple"             "Phlox, Woodland"  "Phlox, Blue"     
    BOTANICAL    "Podophyllum peltatum" "Phlox divaricata" "Phlox divaricata"
    ZONE         "3"                    "3"                "3"               
    LIGHT        "Mostly Shady"         "Sun or Shade"     "Sun or Shade"    
    PRICE        "$2.98"                "$2.80"            "$5.59"           
    AVAILABILITY "060599"               "012299"           "021699"          
                 PLANT                 PLANT                  
    COMMON       "Spring-Beauty"       "Trillium"             
    BOTANICAL    "Claytonia Virginica" "Trillium grandiflorum"
    ZONE         "7"                   "5"                    
    LIGHT        "Mostly Shady"        "Sun or Shade"         
    PRICE        "$6.59"               "$3.90"                
    AVAILABILITY "020199"              "042999"               
                 PLANT                   PLANT                   
    COMMON       "Wake Robin"            "Violet, Dog-Tooth"     
    BOTANICAL    "Trillium grandiflorum" "Erythronium americanum"
    ZONE         "5"                     "4"                     
    LIGHT        "Sun or Shade"          "Shade"                 
    PRICE        "$3.20"                 "$9.04"                 
    AVAILABILITY "022199"                "020199"                
                 PLANT                    PLANT                    PLANT           
    COMMON       "Trout Lily"             "Adder's-Tongue"         "Anemone"       
    BOTANICAL    "Erythronium americanum" "Erythronium americanum" "Anemone blanda"
    ZONE         "4"                      "4"                      "6"             
    LIGHT        "Shade"                  "Shade"                  "Mostly Shady"  
    PRICE        "$6.94"                  "$9.58"                  "$8.86"         
    AVAILABILITY "032499"                 "041399"                 "122698"        
                 PLANT                PLANT            PLANT           
    COMMON       "Grecian Windflower" "Bee Balm"       "Bergamot"      
    BOTANICAL    "Anemone blanda"     "Monarda didyma" "Monarda didyma"
    ZONE         "6"                  "4"              "4"             
    LIGHT        "Mostly Shady"       "Shade"          "Shade"         
    PRICE        "$9.16"              "$4.59"          "$7.16"         
    AVAILABILITY "071099"             "050399"         "042799"        
                 PLANT              PLANT        PLANT        PLANT               
    COMMON       "Black-Eyed Susan" "Buttercup"  "Crowfoot"   "Butterfly Weed"    
    BOTANICAL    "Rudbeckia hirta"  "Ranunculus" "Ranunculus" "Asclepias tuberosa"
    ZONE         "Annual"           "4"          "4"          "Annual"            
    LIGHT        "Sunny"            "Shade"      "Shade"      "Sunny"             
    PRICE        "$9.80"            "$2.57"      "$9.34"      "$2.78"             
    AVAILABILITY "061899"           "061099"     "040399"     "063099"            
                 PLANT        PLANT       PLANT          PLANT         
    COMMON       "Cinquefoil" "Primrose"  "Gentian"      "Blue Gentian"
    BOTANICAL    "Potentilla" "Oenothera" "Gentiana"     "Gentiana"    
    ZONE         "Annual"     "3 - 5"     "4"            "4"           
    LIGHT        "Shade"      "Sunny"     "Sun or Shade" "Sun or Shade"
    PRICE        "$7.06"      "$6.56"     "$7.81"        "$8.56"       
    AVAILABILITY "052599"     "013099"    "051899"       "050299"      
                 PLANT                  PLANT                 
    COMMON       "Jacob's Ladder"       "Greek Valerian"      
    BOTANICAL    "Polemonium caeruleum" "Polemonium caeruleum"
    ZONE         "Annual"               "Annual"              
    LIGHT        "Shade"                "Shade"               
    PRICE        "$9.26"                "$4.36"               
    AVAILABILITY "022199"               "071499"              
                 PLANT                      PLANT           PLANT       
    COMMON       "California Poppy"         "Shooting Star" "Snakeroot"
    BOTANICAL    "Eschscholzia californica" "Dodecatheon"   "Cimicifuga"
    ZONE         "Annual"                   "Annual"        "Annual"    
    LIGHT        "Sun"                      "Mostly Shady"  "Shade"     
    PRICE        "$7.89"                    "$8.60"         "$5.63"     
    AVAILABILITY "032799"                   "051399"        "071199"    
                 PLANT               
    COMMON       "Cardinal Flower"   
    BOTANICAL    "Lobelia cardinalis"
    ZONE         "2"                 
    LIGHT        "Shade"             
    PRICE        "$3.02"             
    AVAILABILITY "022299"            




```R
# get the data in a data-frame and have a look at the first rows and columns. The t() function transposes the plantcat variable
plantcat_df <- data.frame(t(plantcat),row.names=NULL)
head(plantcat_df)
```




                   COMMON              BOTANICAL ZONE        LIGHT PRICE
    1           Bloodroot Sanguinaria canadensis    4 Mostly Shady $2.44
    2           Columbine   Aquilegia canadensis    3 Mostly Shady $9.37
    3      Marsh Marigold       Caltha palustris    4 Mostly Sunny $6.81
    4             Cowslip       Caltha palustris    4 Mostly Shady $9.90
    5 Dutchman's-Breeches    Dicentra cucullaria    3 Mostly Shady $6.44
    6        Ginger, Wild       Asarum canadense    3 Mostly Shady $9.03
      AVAILABILITY
    1       031599
    2       030699
    3       051799
    4       030699
    5       012099
    6       041899
