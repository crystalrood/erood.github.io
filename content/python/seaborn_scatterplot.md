Title: Creating Scatterplots with Seaborn
Slug: seaborn_scatterplot
Summary: Creating Scatterplots with Seaborn
Date: 2016-05-01 12:00
Category: Python
Tags: Data Visualization
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

df['x'] = random.sample(range(1, 1000), 5)
df['y'] = random.sample(range(1, 1000), 5)
df['z'] = [1,0,0,1,0]
df['k'] = ['male','male','male','female','female']
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
      <th>z</th>
      <th>k</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td> 859</td>
      <td> 714</td>
      <td> 1</td>
      <td>   male</td>
    </tr>
    <tr>
      <th>1</th>
      <td>  70</td>
      <td> 321</td>
      <td> 0</td>
      <td>   male</td>
    </tr>
    <tr>
      <th>2</th>
      <td> 378</td>
      <td>  12</td>
      <td> 0</td>
      <td>   male</td>
    </tr>
    <tr>
      <th>3</th>
      <td> 737</td>
      <td>  93</td>
      <td> 1</td>
      <td> female</td>
    </tr>
    <tr>
      <th>4</th>
      <td> 375</td>
      <td> 956</td>
      <td> 0</td>
      <td> female</td>
    </tr>
  </tbody>
</table>
</div>



## Scatterplot


```python
sns.set_context("notebook", font_scale=1.1)
sns.set_style("ticks")


sns.lmplot('x', 'y', 
           data=df, 
           fit_reg=False, 
           dropna=True,
           hue="z",  
           scatter_kws={"marker": "D", 
                        "s": 100})
plt.title('Histogram of IQ')
plt.xlabel('Time')
plt.ylabel('Deaths')
```




    <matplotlib.text.Text at 0x10b4a0850>




![png]({filename}/images/seaborn_scatterplot/output_6_1.png)

