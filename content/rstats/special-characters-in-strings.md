Title: Special Characters In Strings
Slug: special-characters-in-strings
Summary: Special Characters In Strings
Date: 2016-05-01 12:00
Category: R Stats
Tags: Basics
Authors: Chris Albon



There are some special characters that can be added to strings by placing certain characters in the string. To view these characters we use cat() because the default print() converts these escape characters into regular characters.


```R
# Add a tab
cat("cat\tdog")
```

    cat	dog


```R
# Add a line break
cat("cat\ndog")
```

    cat
    dog
