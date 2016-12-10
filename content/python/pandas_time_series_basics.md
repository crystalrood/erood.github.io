Title: Pandas Time Series Basics
Slug: pandas_time_series_basics
Summary: Pandas Time Series Basics
Date: 2016-05-01 12:00
Category: Python
Tags: Data Wrangling
Authors: Chris Albon



### Import modules


```python
from datetime import datetime
import pandas as pd
%matplotlib inline
import matplotlib.pyplot as pyplot
```

### Create a dataframe


```python
data = {'date': ['2014-05-01 18:47:05.069722', '2014-05-01 18:47:05.119994', '2014-05-02 18:47:05.178768', '2014-05-02 18:47:05.230071', '2014-05-02 18:47:05.230071', '2014-05-02 18:47:05.280592', '2014-05-03 18:47:05.332662', '2014-05-03 18:47:05.385109', '2014-05-04 18:47:05.436523', '2014-05-04 18:47:05.486877'], 
        'battle_deaths': [34, 25, 26, 15, 15, 14, 26, 25, 62, 41]}
df = pd.DataFrame(data, columns = ['date', 'battle_deaths'])
print(df)
```

                             date  battle_deaths
    0  2014-05-01 18:47:05.069722             34
    1  2014-05-01 18:47:05.119994             25
    2  2014-05-02 18:47:05.178768             26
    3  2014-05-02 18:47:05.230071             15
    4  2014-05-02 18:47:05.230071             15
    5  2014-05-02 18:47:05.280592             14
    6  2014-05-03 18:47:05.332662             26
    7  2014-05-03 18:47:05.385109             25
    8  2014-05-04 18:47:05.436523             62
    9  2014-05-04 18:47:05.486877             41
    
    [10 rows x 2 columns]


### Convert df['date'] from string to datetime


```python
df['date'] = pd.to_datetime(df['date'])
```

### Set df['date'] as the index and delete the column


```python
df.index = df['date']
del df['date']
df
```




<div style="max-height:1000px;max-width:1500px;overflow:auto;">
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>battle_deaths</th>
    </tr>
    <tr>
      <th>date</th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2014-05-01 18:47:05.069722</th>
      <td> 34</td>
    </tr>
    <tr>
      <th>2014-05-01 18:47:05.119994</th>
      <td> 25</td>
    </tr>
    <tr>
      <th>2014-05-02 18:47:05.178768</th>
      <td> 26</td>
    </tr>
    <tr>
      <th>2014-05-02 18:47:05.230071</th>
      <td> 15</td>
    </tr>
    <tr>
      <th>2014-05-02 18:47:05.230071</th>
      <td> 15</td>
    </tr>
    <tr>
      <th>2014-05-02 18:47:05.280592</th>
      <td> 14</td>
    </tr>
    <tr>
      <th>2014-05-03 18:47:05.332662</th>
      <td> 26</td>
    </tr>
    <tr>
      <th>2014-05-03 18:47:05.385109</th>
      <td> 25</td>
    </tr>
    <tr>
      <th>2014-05-04 18:47:05.436523</th>
      <td> 62</td>
    </tr>
    <tr>
      <th>2014-05-04 18:47:05.486877</th>
      <td> 41</td>
    </tr>
  </tbody>
</table>
<p>10 rows × 1 columns</p>
</div>



### View all observations that occured in 2014


```python
df['2014']
```




<div style="max-height:1000px;max-width:1500px;overflow:auto;">
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>battle_deaths</th>
    </tr>
    <tr>
      <th>date</th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2014-05-01 18:47:05.069722</th>
      <td> 34</td>
    </tr>
    <tr>
      <th>2014-05-01 18:47:05.119994</th>
      <td> 25</td>
    </tr>
    <tr>
      <th>2014-05-02 18:47:05.178768</th>
      <td> 26</td>
    </tr>
    <tr>
      <th>2014-05-02 18:47:05.230071</th>
      <td> 15</td>
    </tr>
    <tr>
      <th>2014-05-02 18:47:05.230071</th>
      <td> 15</td>
    </tr>
    <tr>
      <th>2014-05-02 18:47:05.280592</th>
      <td> 14</td>
    </tr>
    <tr>
      <th>2014-05-03 18:47:05.332662</th>
      <td> 26</td>
    </tr>
    <tr>
      <th>2014-05-03 18:47:05.385109</th>
      <td> 25</td>
    </tr>
    <tr>
      <th>2014-05-04 18:47:05.436523</th>
      <td> 62</td>
    </tr>
    <tr>
      <th>2014-05-04 18:47:05.486877</th>
      <td> 41</td>
    </tr>
  </tbody>
</table>
<p>10 rows × 1 columns</p>
</div>



### View all observations that occured in May 2014


```python
df['2014-05']
```




<div style="max-height:1000px;max-width:1500px;overflow:auto;">
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>battle_deaths</th>
    </tr>
    <tr>
      <th>date</th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2014-05-01 18:47:05.069722</th>
      <td> 34</td>
    </tr>
    <tr>
      <th>2014-05-01 18:47:05.119994</th>
      <td> 25</td>
    </tr>
    <tr>
      <th>2014-05-02 18:47:05.178768</th>
      <td> 26</td>
    </tr>
    <tr>
      <th>2014-05-02 18:47:05.230071</th>
      <td> 15</td>
    </tr>
    <tr>
      <th>2014-05-02 18:47:05.230071</th>
      <td> 15</td>
    </tr>
    <tr>
      <th>2014-05-02 18:47:05.280592</th>
      <td> 14</td>
    </tr>
    <tr>
      <th>2014-05-03 18:47:05.332662</th>
      <td> 26</td>
    </tr>
    <tr>
      <th>2014-05-03 18:47:05.385109</th>
      <td> 25</td>
    </tr>
    <tr>
      <th>2014-05-04 18:47:05.436523</th>
      <td> 62</td>
    </tr>
    <tr>
      <th>2014-05-04 18:47:05.486877</th>
      <td> 41</td>
    </tr>
  </tbody>
</table>
<p>10 rows × 1 columns</p>
</div>



### Observations after May 3rd, 2014


```python
df[datetime(2014, 5, 3):]
```




<div style="max-height:1000px;max-width:1500px;overflow:auto;">
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>battle_deaths</th>
    </tr>
    <tr>
      <th>date</th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2014-05-03 18:47:05.332662</th>
      <td> 26</td>
    </tr>
    <tr>
      <th>2014-05-03 18:47:05.385109</th>
      <td> 25</td>
    </tr>
    <tr>
      <th>2014-05-04 18:47:05.436523</th>
      <td> 62</td>
    </tr>
    <tr>
      <th>2014-05-04 18:47:05.486877</th>
      <td> 41</td>
    </tr>
  </tbody>
</table>
<p>4 rows × 1 columns</p>
</div>



### Observations between May 3rd and May 4th


```python
df['5/3/2014':'5/4/2014']
```




<div style="max-height:1000px;max-width:1500px;overflow:auto;">
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>battle_deaths</th>
    </tr>
    <tr>
      <th>date</th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2014-05-03 18:47:05.332662</th>
      <td> 26</td>
    </tr>
    <tr>
      <th>2014-05-03 18:47:05.385109</th>
      <td> 25</td>
    </tr>
    <tr>
      <th>2014-05-04 18:47:05.436523</th>
      <td> 62</td>
    </tr>
    <tr>
      <th>2014-05-04 18:47:05.486877</th>
      <td> 41</td>
    </tr>
  </tbody>
</table>
<p>4 rows × 1 columns</p>
</div>



### Truncation observations after May 2nd 2014


```python
df.truncate(after='5/3/2014')
```




<div style="max-height:1000px;max-width:1500px;overflow:auto;">
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>battle_deaths</th>
    </tr>
    <tr>
      <th>date</th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2014-05-01 18:47:05.069722</th>
      <td> 34</td>
    </tr>
    <tr>
      <th>2014-05-01 18:47:05.119994</th>
      <td> 25</td>
    </tr>
    <tr>
      <th>2014-05-02 18:47:05.178768</th>
      <td> 26</td>
    </tr>
    <tr>
      <th>2014-05-02 18:47:05.230071</th>
      <td> 15</td>
    </tr>
    <tr>
      <th>2014-05-02 18:47:05.230071</th>
      <td> 15</td>
    </tr>
    <tr>
      <th>2014-05-02 18:47:05.280592</th>
      <td> 14</td>
    </tr>
  </tbody>
</table>
<p>6 rows × 1 columns</p>
</div>



### Observations of May 2014


```python
df.ix['5-2014']
```




<div style="max-height:1000px;max-width:1500px;overflow:auto;">
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>battle_deaths</th>
    </tr>
    <tr>
      <th>date</th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2014-05-01 18:47:05.069722</th>
      <td> 34</td>
    </tr>
    <tr>
      <th>2014-05-01 18:47:05.119994</th>
      <td> 25</td>
    </tr>
    <tr>
      <th>2014-05-02 18:47:05.178768</th>
      <td> 26</td>
    </tr>
    <tr>
      <th>2014-05-02 18:47:05.230071</th>
      <td> 15</td>
    </tr>
    <tr>
      <th>2014-05-02 18:47:05.230071</th>
      <td> 15</td>
    </tr>
    <tr>
      <th>2014-05-02 18:47:05.280592</th>
      <td> 14</td>
    </tr>
    <tr>
      <th>2014-05-03 18:47:05.332662</th>
      <td> 26</td>
    </tr>
    <tr>
      <th>2014-05-03 18:47:05.385109</th>
      <td> 25</td>
    </tr>
    <tr>
      <th>2014-05-04 18:47:05.436523</th>
      <td> 62</td>
    </tr>
    <tr>
      <th>2014-05-04 18:47:05.486877</th>
      <td> 41</td>
    </tr>
  </tbody>
</table>
<p>10 rows × 1 columns</p>
</div>



### Count the number of observations per timestamp


```python
df.groupby(level=0).count()
```




<div style="max-height:1000px;max-width:1500px;overflow:auto;">
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>battle_deaths</th>
    </tr>
    <tr>
      <th>date</th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2014-05-01 18:47:05.069722</th>
      <td> 1</td>
    </tr>
    <tr>
      <th>2014-05-01 18:47:05.119994</th>
      <td> 1</td>
    </tr>
    <tr>
      <th>2014-05-02 18:47:05.178768</th>
      <td> 1</td>
    </tr>
    <tr>
      <th>2014-05-02 18:47:05.230071</th>
      <td> 2</td>
    </tr>
    <tr>
      <th>2014-05-02 18:47:05.280592</th>
      <td> 1</td>
    </tr>
    <tr>
      <th>2014-05-03 18:47:05.332662</th>
      <td> 1</td>
    </tr>
    <tr>
      <th>2014-05-03 18:47:05.385109</th>
      <td> 1</td>
    </tr>
    <tr>
      <th>2014-05-04 18:47:05.436523</th>
      <td> 1</td>
    </tr>
    <tr>
      <th>2014-05-04 18:47:05.486877</th>
      <td> 1</td>
    </tr>
  </tbody>
</table>
<p>9 rows × 1 columns</p>
</div>



### 

### Mean value of battle_deaths per day


```python
df.resample('D', how='mean')
```




<div style="max-height:1000px;max-width:1500px;overflow:auto;">
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>battle_deaths</th>
    </tr>
    <tr>
      <th>date</th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2014-05-01</th>
      <td> 29.5</td>
    </tr>
    <tr>
      <th>2014-05-02</th>
      <td> 17.5</td>
    </tr>
    <tr>
      <th>2014-05-03</th>
      <td> 25.5</td>
    </tr>
    <tr>
      <th>2014-05-04</th>
      <td> 51.5</td>
    </tr>
  </tbody>
</table>
<p>4 rows × 1 columns</p>
</div>



### Total value of battle_deaths per day


```python
df.resample('D', how='sum')
```




<div style="max-height:1000px;max-width:1500px;overflow:auto;">
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>battle_deaths</th>
    </tr>
    <tr>
      <th>date</th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2014-05-01</th>
      <td>  59</td>
    </tr>
    <tr>
      <th>2014-05-02</th>
      <td>  70</td>
    </tr>
    <tr>
      <th>2014-05-03</th>
      <td>  51</td>
    </tr>
    <tr>
      <th>2014-05-04</th>
      <td> 103</td>
    </tr>
  </tbody>
</table>
<p>4 rows × 1 columns</p>
</div>



### Plot of the total battle deaths per day


```python
df.resample('D', how='sum').plot()
```




    <matplotlib.axes.AxesSubplot at 0x10809de50>




![png]({filename}/images/pandas_time_series_basics/output_29_1.png)

