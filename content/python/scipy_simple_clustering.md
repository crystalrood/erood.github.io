Title: Simple Clustering With SciPy
Slug: scipy_simple_clustering
Summary: Simple Clustering With SciPy
Date: 2016-05-01 12:00
Category: Python
Tags: Other
Authors: Chris Albon



### Import modules


```python
import numpy as np
%matplotlib inline
import matplotlib.pyplot as plt
from scipy.cluster import vq
```

### Create coordinates for battles for each year of the war


```python
# create 100 coordinate pairs (i.e. two values), then add 5 to all of them
year_1 = np.random.randn(100, 2) + 5

# create 30 coordinatee pairs (i.e. two values), then subtract 5 to all of them
year_2 = np.random.randn(30, 2) - 5

# create 50 coordinatee pairs (i.e. two values)
year_3 = np.random.randn(50, 2)
```

### View the first 3 entries of each year of battles


```python
print('year 1 battles:',  year_1[0:3])
print('year 2 battles:', year_2[0:3])
print('year 3 battles:', year_3[0:3])
```

    year 1 battles: [[ 3.87032104  4.93418141]
     [ 4.47603646  3.23230121]
     [ 6.15905943  4.55274026]]
    year 2 battles: [[-3.55642932 -3.13125097]
     [-5.83295449 -5.75787649]
     [-5.12144789 -5.00466761]]
    year 3 battles: [[-0.27557365 -0.65002898]
     [ 0.94593878 -0.46056352]
     [ 0.91003511  0.27888337]]


### Pool all three years of coordinates


```python
# vertically stack year_1, year_2, and year_3 elements
battles = np.vstack([year_1, year_2, year_3])
```

### Cluster the battle locations into three groups


```python
# calculate the centroid coordinates of each cluster 
# and the variance of all the clusters
centroids, variance  = vq.kmeans(battles, 3)
```

### View the centroid coordinate for each of the three clusters


```python
centroids
```




    array([[ 4.89478443,  5.00806609],
           [ 0.16770004,  0.01639683],
           [-5.06447231, -4.99956259]])



### View the variance of the clusters (they all share the same)


```python
variance
```




    1.2382236882037887



### Seperate the battle data into clusters


```python
identified, distance = vq.vq(battles, centroids)
```

### View the cluster of each battle


```python
identified
```

### View the distance of each individual battle from their cluster's centroid


```python
distance
```

### Index the battles data by the cluster to which they belong


```python
cluster_1 = battles[identified == 0]
cluster_2 = battles[identified == 1]
cluster_3 = battles[identified == 2]
```

### Print the first three coordinate pairs of each cluster


```python
print(cluster_1[0:3])
print(cluster_2[0:3])
print(cluster_3[0:3])
```

    [[ 3.87032104  4.93418141]
     [ 4.47603646  3.23230121]
     [ 6.15905943  4.55274026]]
    [[-0.27557365 -0.65002898]
     [ 0.94593878 -0.46056352]
     [ 0.91003511  0.27888337]]
    [[-3.55642932 -3.13125097]
     [-5.83295449 -5.75787649]
     [-5.12144789 -5.00466761]]


### Plot all the battles, color each battle by cluster


```python
# create a scatter plot there the x-axis is the first column of battles
# the y-axis is the second column of battles, the size is 100, and
# the color of each point is determined by the indentified variable
plt.scatter(battles[:,0], battles[:,1], s=100, c=identified)
```




    <matplotlib.collections.PathCollection at 0x10771b890>




![png]({filename}/images/scipy_simple_clustering/output_26_1.png)

