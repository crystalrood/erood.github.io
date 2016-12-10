Title: Group Data By Time
Slug: pandas_group_data_by_time
Summary: Group Data By Time
Date: 2016-03-11 12:00
Category: Python
Tags: Data Wrangling
Authors: Chris Albon

On March 13, 2016, version 0.18.0 of pandas was released, with significant changes in how the resampling function operates. This tutorial follows v0.18.0 and will not work for previous versions of pandas.

First let's load the modules we care about

## Preliminaries


```python
# Import required packages
import pandas as pd
import datetime
import numpy as np
```

Next, let's create some sample data that we can group by time as an sample. In this example I am creating a dataframe with two columns with 365 rows. One column is a date, the second column is a numeric value.

## Create Data


```python
# Create a datetime variable for today
base = datetime.datetime.today()
# Create a list variable that creates 365 days of rows of datetime values
date_list = [base - datetime.timedelta(days=x) for x in range(0, 365)]
```


```python
# Create a list variable of 365 numeric values
score_list = list(np.random.randint(low=1, high=1000, size=365))
```


```python
# Create an empty dataframe
df = pd.DataFrame()

# Create a column from the datetime variable
df['datetime'] = date_list
# Convert that column into a datetime datatype
df['datetime'] = pd.to_datetime(df['datetime'])
# Set the datetime column as the index
df.index = df['datetime']
# Create a column from the numeric score variable
df['score'] = score_list
```


```python
# Let's take a took at the data
df.head()
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>datetime</th>
      <th>score</th>
    </tr>
    <tr>
      <th>datetime</th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2016-03-11 21:27:36.859714</th>
      <td>2016-03-11 21:27:36.859714</td>
      <td>459</td>
    </tr>
    <tr>
      <th>2016-03-10 21:27:36.859714</th>
      <td>2016-03-10 21:27:36.859714</td>
      <td>153</td>
    </tr>
    <tr>
      <th>2016-03-09 21:27:36.859714</th>
      <td>2016-03-09 21:27:36.859714</td>
      <td>458</td>
    </tr>
    <tr>
      <th>2016-03-08 21:27:36.859714</th>
      <td>2016-03-08 21:27:36.859714</td>
      <td>310</td>
    </tr>
    <tr>
      <th>2016-03-07 21:27:36.859714</th>
      <td>2016-03-07 21:27:36.859714</td>
      <td>376</td>
    </tr>
  </tbody>
</table>
</div>



## Group Data By Date

In pandas, the most common way to group by time is to use the `.resample()` function. In v0.18.0 this function is two-stage. This means that `df.resample('M')` creates an object to which we can apply other functions (`mean`, `count`, `sum`, etc.)


```python
# Group the data by month, and take the mean for each group (i.e. each month)
df.resample('M').mean()
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>score</th>
    </tr>
    <tr>
      <th>datetime</th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2015-03-31</th>
      <td>509.421053</td>
    </tr>
    <tr>
      <th>2015-04-30</th>
      <td>543.100000</td>
    </tr>
    <tr>
      <th>2015-05-31</th>
      <td>520.709677</td>
    </tr>
    <tr>
      <th>2015-06-30</th>
      <td>473.100000</td>
    </tr>
    <tr>
      <th>2015-07-31</th>
      <td>521.677419</td>
    </tr>
    <tr>
      <th>2015-08-31</th>
      <td>410.580645</td>
    </tr>
    <tr>
      <th>2015-09-30</th>
      <td>491.933333</td>
    </tr>
    <tr>
      <th>2015-10-31</th>
      <td>447.322581</td>
    </tr>
    <tr>
      <th>2015-11-30</th>
      <td>488.166667</td>
    </tr>
    <tr>
      <th>2015-12-31</th>
      <td>473.193548</td>
    </tr>
    <tr>
      <th>2016-01-31</th>
      <td>444.129032</td>
    </tr>
    <tr>
      <th>2016-02-29</th>
      <td>555.965517</td>
    </tr>
    <tr>
      <th>2016-03-31</th>
      <td>445.545455</td>
    </tr>
  </tbody>
</table>
</div>




```python
# Group the data by month, and take the sum for each group (i.e. each month)
df.resample('M').sum()
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>score</th>
    </tr>
    <tr>
      <th>datetime</th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2015-03-31</th>
      <td>9679</td>
    </tr>
    <tr>
      <th>2015-04-30</th>
      <td>16293</td>
    </tr>
    <tr>
      <th>2015-05-31</th>
      <td>16142</td>
    </tr>
    <tr>
      <th>2015-06-30</th>
      <td>14193</td>
    </tr>
    <tr>
      <th>2015-07-31</th>
      <td>16172</td>
    </tr>
    <tr>
      <th>2015-08-31</th>
      <td>12728</td>
    </tr>
    <tr>
      <th>2015-09-30</th>
      <td>14758</td>
    </tr>
    <tr>
      <th>2015-10-31</th>
      <td>13867</td>
    </tr>
    <tr>
      <th>2015-11-30</th>
      <td>14645</td>
    </tr>
    <tr>
      <th>2015-12-31</th>
      <td>14669</td>
    </tr>
    <tr>
      <th>2016-01-31</th>
      <td>13768</td>
    </tr>
    <tr>
      <th>2016-02-29</th>
      <td>16123</td>
    </tr>
    <tr>
      <th>2016-03-31</th>
      <td>4901</td>
    </tr>
  </tbody>
</table>
</div>



## Grouping Options

There are many options for grouping. You can learn more about them in [Pandas's timeseries docs](http://pandas.pydata.org/pandas-docs/stable/timeseries.html), however, I have also listed them below for your convenience.

| Value | Description |
|---|---|
|B   |    business day frequency |
|C   |    custom business day frequency (experimental) |
|D   |    calendar day frequency |
|W   |    weekly frequency |
|M   |    month end frequency |
|BM  |    business month end frequency |
|CBM |    custom business month end frequency | |
|MS  |    month start frequency |
|BMS |    business month start frequency |
|CBMS|    custom business month start frequency |
|Q   |    quarter end frequency |
|BQ  |    business quarter endfrequency |
|QS  |    quarter start frequency |
|BQS |    business quarter start frequency |
|A   |    year end frequency |
|BA  |    business year end frequency |
|AS  |    year start frequency |
|BAS |    business year start frequency |
|BH  |    business hour frequency |
|H   |    hourly frequency |
|T   |    minutely frequency |
|S   |    secondly frequency |
|L   |    milliseconds |
|U   |    microseconds |
|N   |    nanoseconds |
