Title: Select Rows That Have A Certain Value
Slug: pandas_select_rows_containing_values
Summary: Select Rows That Have A Certain Value
Date: 2016-05-01 12:00
Category: Python
Tags: Data Wrangling
Authors: Chris Albon




```python
import pandas as pd
```


```python
# Create an example dataframe
data = {'name': ['Jason', 'Molly'], 
        'country': [['Syria', 'Lebanon'],['Spain', 'Morocco']]}
df = pd.DataFrame(data)
df
```




<div style="max-height:1000px;max-width:1500px;overflow:auto;">
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>country</th>
      <th>name</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td> [Syria, Lebanon]</td>
      <td> Jason</td>
    </tr>
    <tr>
      <th>1</th>
      <td> [Spain, Morocco]</td>
      <td> Molly</td>
    </tr>
  </tbody>
</table>
</div>




```python
df[df['country'].map(lambda country: 'Syria' in country)]
```




<div style="max-height:1000px;max-width:1500px;overflow:auto;">
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>country</th>
      <th>name</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td> [Syria, Lebanon]</td>
      <td> Jason</td>
    </tr>
  </tbody>
</table>
</div>


