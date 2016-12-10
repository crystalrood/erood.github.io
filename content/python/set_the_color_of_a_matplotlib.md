Title: Set The Color Of A Matplotlib Plot
Slug: set_the_color_of_a_matplotlib
Summary: Set The Color Of A Matplotlib Plot
Date: 2016-05-01 12:00
Category: Python
Tags: Data Visualization
Authors: Chris Albon



### Import numpy and matplotlib.pyplot


```python
%matplotlib inline
import numpy as np
import matplotlib.pyplot as plt
```

### Create some simulated data.


```python
n = 100
r = 2 * np.random.rand(n)
theta = 2 * np.pi * np.random.rand(n)
area = 200 * r**2 * np.random.rand(n)
colors = theta
```

### Create a scatterplot using the a colormap.
Full list of colormaps: http://wiki.scipy.org/Cookbook/Matplotlib/Show_colormaps


```python
c = plt.scatter(theta, r, c=colors, s=area, cmap=plt.cm.RdYlGn)
```


![png]({filename}/images/set_the_color_of_a_matplotlib/output_6_0.png)



```python
c1 = plt.scatter(theta, r, c=colors, s=area, cmap=plt.cm.Blues)
```


![png]({filename}/images/set_the_color_of_a_matplotlib/output_7_0.png)



```python
c2 = plt.scatter(theta, r, c=colors, s=area, cmap=plt.cm.BrBG)
```


![png]({filename}/images/set_the_color_of_a_matplotlib/output_8_0.png)



```python
c3 = plt.scatter(theta, r, c=colors, s=area, cmap=plt.cm.Greens)
```


![png]({filename}/images/set_the_color_of_a_matplotlib/output_9_0.png)



```python
c4 = plt.scatter(theta, r, c=colors, s=area, cmap=plt.cm.RdGy)
```


![png]({filename}/images/set_the_color_of_a_matplotlib/output_10_0.png)



```python
c5 = plt.scatter(theta, r, c=colors, s=area, cmap=plt.cm.YlOrRd)
```


![png]({filename}/images/set_the_color_of_a_matplotlib/output_11_0.png)



```python
c6 = plt.scatter(theta, r, c=colors, s=area, cmap=plt.cm.autumn)
```


![png]({filename}/images/set_the_color_of_a_matplotlib/output_12_0.png)



```python
c7 = plt.scatter(theta, r, c=colors, s=area, cmap=plt.cm.binary)
```


![png]({filename}/images/set_the_color_of_a_matplotlib/output_13_0.png)



```python
c8 = plt.scatter(theta, r, c=colors, s=area, cmap=plt.cm.gist_earth)
```


![png]({filename}/images/set_the_color_of_a_matplotlib/output_14_0.png)



```python
c9 = plt.scatter(theta, r, c=colors, s=area, cmap=plt.cm.gist_heat)
```


![png]({filename}/images/set_the_color_of_a_matplotlib/output_15_0.png)



```python
c10 = plt.scatter(theta, r, c=colors, s=area, cmap=plt.cm.hot)
```


![png]({filename}/images/set_the_color_of_a_matplotlib/output_16_0.png)



```python
c11 = plt.scatter(theta, r, c=colors, s=area, cmap=plt.cm.spring)
```


![png]({filename}/images/set_the_color_of_a_matplotlib/output_17_0.png)



```python
c12 = plt.scatter(theta, r, c=colors, s=area, cmap=plt.cm.summer)
```


![png]({filename}/images/set_the_color_of_a_matplotlib/output_18_0.png)



```python
c12 = plt.scatter(theta, r, c=colors, s=area, cmap=plt.cm.winter)
```


![png]({filename}/images/set_the_color_of_a_matplotlib/output_19_0.png)



```python
c13 = plt.scatter(theta, r, c=colors, s=area, cmap=plt.cm.bone)
```


![png]({filename}/images/set_the_color_of_a_matplotlib/output_20_0.png)



```python
c14 = plt.scatter(theta, r, c=colors, s=area, cmap=plt.cm.cool)
```


![png]({filename}/images/set_the_color_of_a_matplotlib/output_21_0.png)



```python
c15 = plt.scatter(theta, r, c=colors, s=area, cmap=plt.cm.YlGn)
```


![png]({filename}/images/set_the_color_of_a_matplotlib/output_22_0.png)



```python
c16 = plt.scatter(theta, r, c=colors, s=area, cmap=plt.cm.RdBu)
```


![png]({filename}/images/set_the_color_of_a_matplotlib/output_23_0.png)



```python
c17 = plt.scatter(theta, r, c=colors, s=area, cmap=plt.cm.PuOr)
```


![png]({filename}/images/set_the_color_of_a_matplotlib/output_24_0.png)



```python
c18 = plt.scatter(theta, r, c=colors, s=area, cmap=plt.cm.Oranges)
```


![png]({filename}/images/set_the_color_of_a_matplotlib/output_25_0.png)



```python

```
