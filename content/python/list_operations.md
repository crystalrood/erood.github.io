Title: List Operations
Slug: list_operations
Summary: List Operations
Date: 2016-05-01 12:00
Category: Python
Tags: Basics
Authors: Chris Albon



### Create a list of simulated data


```python
countries = ["Spain", "Japan", "Kenya", "Tanzania", "Ghana"]
```

### Add an item to the end of the list

Note: If the appending item contains multiple items, it is nested.


```python
countries.append("Nigeria"); countries
```




    ['Spain', 'Japan', 'Kenya', 'Tanzania', 'Ghana', 'Nigeria']



### Add all items of a list to a list


```python
countries.extend(["France", "Switzerland", "China"]); countries
```




    ['Spain',
     'Japan',
     'Kenya',
     'Tanzania',
     'Ghana',
     'Nigeria',
     'France',
     'Switzerland',
     'China']



### Insert Italy into the second position of the list countries


```python
countries.insert(1, "Italy"); countries
```




    ['Spain',
     'Italy',
     'Japan',
     'Kenya',
     'Tanzania',
     'Ghana',
     'Nigeria',
     'France',
     'Switzerland',
     'China']



### Remove Spain from the list countries


```python
countries.remove("Spain"); countries
```




    ['Italy',
     'Japan',
     'Kenya',
     'Tanzania',
     'Ghana',
     'Nigeria',
     'France',
     'Switzerland',
     'China']



### Delete the second item from the list countries


```python
del countries[1]; countries
```




    ['Italy',
     'Kenya',
     'Tanzania',
     'Ghana',
     'Nigeria',
     'France',
     'Switzerland',
     'China']



### Remove the third item from the list, and returns it (i.e. "pops it out")


```python
countries
```




    ['Italy',
     'Kenya',
     'Tanzania',
     'Ghana',
     'Nigeria',
     'France',
     'Switzerland',
     'China']




```python
countries.pop(3)
```




    'Ghana'




```python
countries
```




    ['Italy', 'Kenya', 'Tanzania', 'Nigeria', 'France', 'Switzerland', 'China']



### Return the index of the first item that matches "Kenya"


```python
kenya = countries.index("Kenya"); kenya
```




    1



### Count all number of times "Kenya" appears in the list countries


```python
kenya_count = countries.count("Kenya"); kenya_count
```




    1



### Sort the list in alphabetical order


```python
countries.sort(); countries
```




    ['China', 'France', 'Italy', 'Kenya', 'Nigeria', 'Switzerland', 'Tanzania']



### Reverse the elements of the list


```python
countries.reverse(); countries
```




    ['Tanzania', 'Switzerland', 'Nigeria', 'Kenya', 'Italy', 'France', 'China']



### Copy the list, same as countries[:]


```python
countries_copy = countries.copy(); countries_copy
```




    ['Tanzania', 'Switzerland', 'Nigeria', 'Kenya', 'Italy', 'France', 'China']



### Remove all the items from the list countries


```python
countries.clear(); countries
```




    []


