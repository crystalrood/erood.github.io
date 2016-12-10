Title: Using Seaborn To Visualize A Pandas Dataframe
Slug: pandas_with_seaborn
Summary: Using Seaborn To Visualize A Pandas Dataframe
Date: 2016-05-01 12:00
Category: Python
Tags: Data Wrangling
Authors: Chris Albon



## Preliminaries


```python
import pandas as pd
%matplotlib inline
import random
import matplotlib.pyplot as plt
import seaborn as sns
```


```python
df = pd.DataFrame()

df['x'] = random.sample(range(1, 100), 25)
df['y'] = random.sample(range(1, 100), 25)
```


```python
df.head()
```




<div style="max-height:1000px;max-width:1500px;overflow:auto;">
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>x</th>
      <th>y</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td> 14</td>
      <td> 52</td>
    </tr>
    <tr>
      <th>1</th>
      <td> 88</td>
      <td> 92</td>
    </tr>
    <tr>
      <th>2</th>
      <td> 39</td>
      <td> 69</td>
    </tr>
    <tr>
      <th>3</th>
      <td> 19</td>
      <td> 98</td>
    </tr>
    <tr>
      <th>4</th>
      <td> 60</td>
      <td> 76</td>
    </tr>
  </tbody>
</table>
</div>



## Scatterplot


```python
sns.lmplot('x', 'y', data=df, fit_reg=False)
```




    <seaborn.axisgrid.FacetGrid at 0x10dc2b1d0>




![png]({filename}/images/pandas_with_seaborn/output_6_1.png)


## Density Plot


```python
sns.kdeplot(df.y)
```




    <matplotlib.axes._subplots.AxesSubplot at 0x10c30e050>




![png]({filename}/images/pandas_with_seaborn/output_8_1.png)



```python
sns.kdeplot(df.y, df.x)
```




    <matplotlib.axes._subplots.AxesSubplot at 0x10c5536d0>




![png]({filename}/images/pandas_with_seaborn/output_9_1.png)



```python
sns.distplot(df.x)
```




    <matplotlib.axes._subplots.AxesSubplot at 0x10b669550>




![png]({filename}/images/pandas_with_seaborn/output_10_1.png)


## Histogram


```python
plt.hist(df.x, alpha=.3)
sns.rugplot(df.x);
```


![png]({filename}/images/pandas_with_seaborn/output_12_0.png)


## Boxplot 


```python
sns.boxplot([df.y, df.x])
```




    <matplotlib.axes._subplots.AxesSubplot at 0x10a5c9b50>




![png]({filename}/images/pandas_with_seaborn/output_14_1.png)


## Violin Plot


```python
sns.violinplot([df.y, df.x])
```




    <matplotlib.axes._subplots.AxesSubplot at 0x10dca4b50>




![png]({filename}/images/pandas_with_seaborn/output_16_1.png)


## Heatmap


```python
sns.heatmap([df.y, df.x], annot=True, fmt="d")
```




    <matplotlib.axes._subplots.AxesSubplot at 0x10dab5110>




![png]({filename}/images/pandas_with_seaborn/output_18_1.png)


## Clustermap


```python
sns.clustermap(df)
```




    <seaborn.matrix.ClusterGrid at 0x10de304d0>




![png]({filename}/images/pandas_with_seaborn/output_20_1.png)

