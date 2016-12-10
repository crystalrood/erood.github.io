Title: Creating Lists From Dictionary Keys And Values
Slug: create_list_from_dictionary_keys_and_values
Summary: Creating Lists From Dictionary Keys And Values
Date: 2016-05-01 12:00
Category: Python
Tags: Data Wrangling
Authors: Chris Albon



### Create a dictionary


```python
dict = {'county': ['Cochice', 'Pima', 'Santa Cruz', 'Maricopa', 'Yuma'], 
        'year': [2012, 2012, 2013, 2014, 2014], 
        'fireReports': [4, 24, 31, 2, 3]}
```

### Create a list from the dictionary keys


```python
# Create a list to place the dictionary keys in
dictionaryKeys = []

# For each key in the dictionary's keys,
for key in dict.keys():
    # add the key to dictionaryKeys
    dictionaryKeys.append(key)

# View the dictionaryKeys list
dictionaryKeys
```




    ['year', 'county', 'fireReports']



### Create a list from the  dictionary values


```python
# Create a list to place the dictionary values in
dictionaryValues = []

# For each key in the dictionary's Values,
for x in dict.values():
    # add the key to dictionaryValues
    dictionaryValues.append(x)

# View the dictionaryValues list
dictionaryValues
```




    [[2012, 2012, 2013, 2014, 2014],
     ['Cochice', 'Pima', 'Santa Cruz', 'Maricopa', 'Yuma'],
     [4, 24, 31, 2, 3]]


