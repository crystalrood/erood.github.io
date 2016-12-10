Title: Linear Regression In scikit-learn
Slug: linear_regression_scikit-learn  
Summary: A simple example of linear regression in scikit-learn
Date: 2016-08-19 12:00  
Category: Machine Learning  
Tags: Basics  
Authors: Chris Albon  

Sources: [scikit-learn](http://scikit-learn.org/stable/auto_examples/linear_model/plot_ols.html#example-linear-model-plot-ols-py), [DrawMyData](http://robertgrantstats.co.uk/drawmydata.html).

The purpose of this tutorial is to give a brief introduction into the logic of statistical model building used in machine learning. If you want to read more about the theory behind this tutorial, check out [An Introduction To Statistical Learning](https://www.amazon.com/Introduction-Statistical-Learning-Applications-Statistics/dp/1461471370).

Let us get started.

## Preliminary


```python
import pandas as pd
from sklearn import linear_model
import random
import numpy as np
%matplotlib inline
```

## Load Data

With those libraries added, let us load the dataset (the dataset is avaliable in his site's GitHub repo).


```python
# Load the data
df = pd.read_csv('../data/simulated_data/battledeaths_n300_cor99.csv')

# Shuffle the data's rows (This is only necessary because of the way I created
# the data using DrawMyData. This would not normally be necessary with a real analysis).
df = df.sample(frac=1) hi
```

## Explore Data

Let us take a look at the first few rows of the data just to get an idea about it.


```python
# View the first few rows
df.head()
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>friendly_battledeaths</th>
      <th>enemy_battledeaths</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>173</th>
      <td>28.4615</td>
      <td>26.5385</td>
    </tr>
    <tr>
      <th>257</th>
      <td>9.7436</td>
      <td>7.6923</td>
    </tr>
    <tr>
      <th>162</th>
      <td>20.0000</td>
      <td>10.3846</td>
    </tr>
    <tr>
      <th>12</th>
      <td>12.8205</td>
      <td>10.3846</td>
    </tr>
    <tr>
      <th>111</th>
      <td>63.8462</td>
      <td>61.9231</td>
    </tr>
  </tbody>
</table>
</div>



Now let us plot the data so we can see it's structure.


```python
# Plot the two variables against eachother
df.plot(x='friendly_battledeaths', y='enemy_battledeaths', kind='scatter')
```




    <matplotlib.axes._subplots.AxesSubplot at 0x11a9fc710>





![png]({filename}/images/linear_regression_scikitlearn/output_12_1.png)

## Break Data Up Into Training And Test Datasets

Now for the real work. To judge how how good our model is, we need something to test it against. We can accomplish this using a technique called cross-validation. Cross-validation can get much more complicated and powerful, but in this example we are going do the most simple version of this technique.

### Steps

1. Divide the dataset into two datasets: A 'training' dataset that we will use to train our model and a 'test' dataset that we will use to judge the accuracy of that model.
2. Train the model on the 'training' data.
3. Apply that model to the test data's X variable, creating the model's guesses for the test data's Ys.
4. Compare how close the model's predictions for the test data's Ys were to the actual test data Ys.


```python
# Create our predictor/independent variable
# and our response/dependent variable
X = df['friendly_battledeaths']
y = df['enemy_battledeaths']

# Create our test data from the first 30 observations
X_test = X[0:30].reshape(-1,1)
y_test = y[0:30]

# Create our training data from the remaining observations
X_train = X[30:].reshape(-1,1)
y_train = y[30:]
```

## Train The Linear Model

Let us train the model using our training data.


```python
# Create an object that is an ols regression
ols = linear_model.LinearRegression()
```


```python
# Train the model using our training data
model = ols.fit(X_train, y_train)
```

## View The Results

Here are some basic outputs of the model, notably the coefficient and the R-squared score.


```python
# View the training model's coefficient
model.coef_
```




    array([ 0.9770556])




```python
# View the R-Squared score
model.score(X_test, y_test)
```




    0.98719951914847326



Now that we have used the training data to train a model, called `model`, we can apply it to the test data's Xs to make predictions of the test data's Ys.

Previously we used `X_train` and `y_train` to train a linear regression model, which we stored as a variable called `model`. The code `model.predict(X_test)` applies the trained model to the `X_test` data, data the model has never seen before to make predicted values of Y.

This can easily be seen by simply running the code:


```python
# Run the model on X_test and show the first five results
list(model.predict(X_test)[0:5])
```




    [27.238901424783169,
     8.9504723858776192,
     18.971545454685064,
     11.956774765407825,
     61.811720758841012]



This array of values is the model's best guesses for the values of the test data's Ys. Compare them to the actual test data Y values:


```python
# View the first five test Y values
list(y_test)[0:5]
```




    [26.538499999999999,
     7.6923000000000004,
     10.384600000000001,
     10.384600000000001,
     61.923099999999998]



Our model predicts that the first observation in the test data will have a Y value of 27.24. Actual Y value for that observation was 26.54. That means the model's prediction was $27.24 - 26.54 = 0.8$ off, this is called the residual of that observation.

The difference between the model's predicted values and the actual values is how is we judge as model's accuracy, because a perfectly accurate model would have residuals of zero.

However, to judge a model, we want a single statistic (number) that we can use as a measure. We want this measure to capture the difference between the predicted values and the actual values across all observations in the data.

The most common statistic used for quantitative Ys is the **residual sum of squares**:

$$ RSS = \sum_{i=1}^{n}(y_{i}-f(x_{i}))^{2} $$

Don't let the mathematical notation throw you off:

 - $f(x_{i})$ is the model we trained: `model.predict(X_test)`
 - $y_{i}$ is the test data's y: `y_test`
 - $^{2}$ is the exponent: `**2`
 - $\sum_{i=1}^{n}$ is the summation: `.sum()`

In the residual sum of squares, for each observation we find the difference between the model's predicted Y and the actual Y, then square that difference to make all the values positive. Then we add all those squared differences together to get a single number. The final result is a statistic representing how far the model's predictions were from the real values.


```python
# Apply the model we created using the training data
# to the test data, and calculate the RSS.
((y_test - model.predict(X_test)) **2).sum()
```




    352.1634102396179



Note: You can also use Mean Squared Error, which is RSS divided by the degrees of freedom. But I find it helpful to think in terms of RSS.


```python
# Calculate the MSE
np.mean((model.predict(X_test) - y_test) **2)
```




    11.738780341320597



What does the model's RSS of 352.16 mean? Mathematically, it is the sum of the squared errors (obviously). But substantly 352.16 has little real meaning. Then why is RSS so fundamental to everything we do? **Because it lets us compare models.**

Does 352.16 mean our model is good? On it's own we don't realy have a good answer. But what if we trained a second model -- with different independent variables -- and applied that model to the same test data and got an RSS of 200? Then we would know that the second model is better! And that hunt for the best model is very often our goal.
