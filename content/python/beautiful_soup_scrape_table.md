Title: Scraping a HTML with Beauitful Soup  
Slug: beautiful_soup_scrape_table  
Summary: Scraping a HTML with Beauitful Soup  
Date: 2016-05-01 12:00  
Category: Python  
Tags: Web Scraping  
Authors: Chris Albon  


```python
# Import required modules
import requests
from bs4 import BeautifulSoup
import pandas as pd
```

### Create a dataframe. We will scrape iPython's HTML table output


```python
# Create a values as dictionary of lists
raw_data = {'first_name': ['Jason', 'Molly', 'Tina', 'Jake', 'Amy'],
        'last_name': ['Miller', 'Jacobson', 'Ali', 'Milner', 'Cooze'],
        'age': [42, 52, 36, 24, 73],
        'preTestScore': [4, 24, 31, 2, 3],
        'postTestScore': [25, 94, 57, 62, 70]}

# Create a dataframe
raw_df = pd.DataFrame(raw_data, columns = ['first_name', 'last_name', 'age', 'preTestScore', 'postTestScore'])

# View a dataframe
raw_df
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>first_name</th>
      <th>last_name</th>
      <th>age</th>
      <th>preTestScore</th>
      <th>postTestScore</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Jason</td>
      <td>Miller</td>
      <td>42</td>
      <td>4</td>
      <td>25</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Molly</td>
      <td>Jacobson</td>
      <td>52</td>
      <td>24</td>
      <td>94</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Tina</td>
      <td>Ali</td>
      <td>36</td>
      <td>31</td>
      <td>57</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Jake</td>
      <td>Milner</td>
      <td>24</td>
      <td>2</td>
      <td>62</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Amy</td>
      <td>Cooze</td>
      <td>73</td>
      <td>3</td>
      <td>70</td>
    </tr>
  </tbody>
</table>
</div>



### Download the HTML and create a Beautiful Soup object


```python
# Create a variable with the URL to this tutorial
url = 'http://nbviewer.ipython.org/github/chrisalbon/code_py/blob/master/beautiful_soup_scrape_table.ipynb'

# Scrape the HTML at the url
r = requests.get(url)

# Turn the HTML into a Beautiful Soup object
soup = BeautifulSoup(r.text, 'lxml')
```

### Parse the Beautiful Soup object


```python
# Create four variables to score the scraped data in
first_name = []
last_name = []
age = []
preTestScore = []
postTestScore = []

# Create an object of the first object that is class=dataframe
table = soup.find(class_='dataframe')

# Find all the <tr> tag pairs, skip the first one, then for each.
for row in table.find_all('tr')[1:]:
    # Create a variable of all the <td> tag pairs in each <tr> tag pair,
    col = row.find_all('td')

    # Create a variable of the string inside 1st <td> tag pair,
    column_1 = col[0].string.strip()
    # and append it to first_name variable
    first_name.append(column_1)

    # Create a variable of the string inside 2nd <td> tag pair,
    column_2 = col[1].string.strip()
    # and append it to last_name variable
    last_name.append(column_2)

    # Create a variable of the string inside 3rd <td> tag pair,
    column_3 = col[2].string.strip()
    # and append it to age variable
    age.append(column_3)

    # Create a variable of the string inside 4th <td> tag pair,
    column_4 = col[3].string.strip()
    # and append it to preTestScore variable
    preTestScore.append(column_4)

    # Create a variable of the string inside 5th <td> tag pair,
    column_5 = col[4].string.strip()
    # and append it to postTestScore variable
    postTestScore.append(column_5)

# Create a variable of the value of the columns
columns = {'first_name': first_name, 'last_name': last_name, 'age': age, 'preTestScore': preTestScore, 'postTestScore': postTestScore}

# Create a dataframe from the columns variable
df = pd.DataFrame(columns)
```


```python
# View the dataframe
df
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>age</th>
      <th>first_name</th>
      <th>last_name</th>
      <th>postTestScore</th>
      <th>preTestScore</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>42</td>
      <td>Jason</td>
      <td>Miller</td>
      <td>25</td>
      <td>4</td>
    </tr>
    <tr>
      <th>1</th>
      <td>52</td>
      <td>Molly</td>
      <td>Jacobson</td>
      <td>94</td>
      <td>24</td>
    </tr>
    <tr>
      <th>2</th>
      <td>36</td>
      <td>Tina</td>
      <td>Ali</td>
      <td>57</td>
      <td>31</td>
    </tr>
    <tr>
      <th>3</th>
      <td>24</td>
      <td>Jake</td>
      <td>Milner</td>
      <td>62</td>
      <td>2</td>
    </tr>
    <tr>
      <th>4</th>
      <td>73</td>
      <td>Amy</td>
      <td>Cooze</td>
      <td>70</td>
      <td>3</td>
    </tr>
  </tbody>
</table>
</div>
