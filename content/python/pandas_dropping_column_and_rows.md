Title: Dropping Rows And Columns In pandas Dataframe
Slug: pandas_dropping_column_and_rows
Summary: Dropping Rows And Columns In pandas Dataframe
Date: 2016-05-01 12:00
Category: Python
Tags: Data Wrangling
Authors: Chris Albon



### Import modules


```python
import pandas as pd
```

### Create a dataframe 


```python
data = {'name': ['Jason', 'Molly', 'Tina', 'Jake', 'Amy'], 
        'year': [2012, 2012, 2013, 2014, 2014], 
        'reports': [4, 24, 31, 2, 3]}
df = pd.DataFrame(data, index = ['Cochice', 'Pima', 'Santa Cruz', 'Maricopa', 'Yuma'])
df
```




<div style="max-height:1000px;max-width:1500px;overflow:auto;">
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>name</th>
      <th>reports</th>
      <th>year</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Cochice</th>
      <td> Jason</td>
      <td>  4</td>
      <td> 2012</td>
    </tr>
    <tr>
      <th>Pima</th>
      <td> Molly</td>
      <td> 24</td>
      <td> 2012</td>
    </tr>
    <tr>
      <th>Santa Cruz</th>
      <td>  Tina</td>
      <td> 31</td>
      <td> 2013</td>
    </tr>
    <tr>
      <th>Maricopa</th>
      <td>  Jake</td>
      <td>  2</td>
      <td> 2014</td>
    </tr>
    <tr>
      <th>Yuma</th>
      <td>   Amy</td>
      <td>  3</td>
      <td> 2014</td>
    </tr>
  </tbody>
</table>
<p>5 rows × 3 columns</p>
</div>



### Drop an observation (row)


```python
df.drop(['Cochice', 'Pima'])
```




<div style="max-height:1000px;max-width:1500px;overflow:auto;">
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>name</th>
      <th>reports</th>
      <th>year</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Santa Cruz</th>
      <td> Tina</td>
      <td> 31</td>
      <td> 2013</td>
    </tr>
    <tr>
      <th>Maricopa</th>
      <td> Jake</td>
      <td>  2</td>
      <td> 2014</td>
    </tr>
    <tr>
      <th>Yuma</th>
      <td>  Amy</td>
      <td>  3</td>
      <td> 2014</td>
    </tr>
  </tbody>
</table>
<p>3 rows × 3 columns</p>
</div>



### Drop a variable (column)

Note: axis=1 denotes that we are referring to a column, not a row


```python
df.drop('reports', axis=1)
```




<div style="max-height:1000px;max-width:1500px;overflow:auto;">
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>name</th>
      <th>year</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Cochice</th>
      <td> Jason</td>
      <td> 2012</td>
    </tr>
    <tr>
      <th>Pima</th>
      <td> Molly</td>
      <td> 2012</td>
    </tr>
    <tr>
      <th>Santa Cruz</th>
      <td>  Tina</td>
      <td> 2013</td>
    </tr>
    <tr>
      <th>Maricopa</th>
      <td>  Jake</td>
      <td> 2014</td>
    </tr>
    <tr>
      <th>Yuma</th>
      <td>   Amy</td>
      <td> 2014</td>
    </tr>
  </tbody>
</table>
<p>5 rows × 2 columns</p>
</div>



### Drop a row if it contains a certain value (in this case, "Tina")

Specifically: Create a new dataframe called df that includes all rows where the value of a cell in the name column does not equal "Tina"


```python
df = df[df.name != 'Tina']
df
```




<div style="max-height:1000px;max-width:1500px;overflow:auto;">
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>name</th>
      <th>reports</th>
      <th>year</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Cochice</th>
      <td> Jason</td>
      <td>  4</td>
      <td> 2012</td>
    </tr>
    <tr>
      <th>Pima</th>
      <td> Molly</td>
      <td> 24</td>
      <td> 2012</td>
    </tr>
    <tr>
      <th>Maricopa</th>
      <td>  Jake</td>
      <td>  2</td>
      <td> 2014</td>
    </tr>
    <tr>
      <th>Yuma</th>
      <td>   Amy</td>
      <td>  3</td>
      <td> 2014</td>
    </tr>
  </tbody>
</table>
<p>4 rows × 3 columns</p>
</div>


