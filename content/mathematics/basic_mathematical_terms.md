Title: Basic Mathematical Terms In Python
Slug: basic_mathematical_terms_in_python
Summary: Basically mathematical terms with short descriptions.
Date: 2016-08-12 12:00  
Category: Mathematics  
Tags: Basics   
Authors: Chris Albon  


```python
import math
```

### Ratio ###

Two quantities divided by eachother, $\frac{x}{y}$. Often written as $x:y$.


```python
x = 2
y = 3

x/y
```




    0.6666666666666666



### Proportion ###

One variable divided by the sum of itself and another variable: $\left | \frac{x}{x+y} \right |$. Proportions range from 0 to 1.


```python
x = 2
y = 3

abs(x/(x+y))
```




    0.4



### Percentage###

Proportions multiplied by 100: $\left | \frac{x}{x+y} \right | \times 100 $


```python
x = 2
y = 3

abs(x/(x+y))*100
```




    40.0



### Functions ###

Functions assigns something to each element of a domain. $f\left ( x \right ): A \rightarrow B$ means "Function x maps A to B"


```python
A = 4

# Create a function called x
def x(_range):
    B = 5
    return _range + B

x(A)
```




    9



### Exponential Function ###

Multiplication of a number by itself. Example: $y^{3} = y \times y \times y$


```python
y = 3

# y*y*y
y**3
```




    27



### Logarithmic Function ###

Inverse of exponential function, transforming exponential functions to linear functions. Logarithms tell you how many times to multiple a base to get a value. Example: $log_{a}a^{x} = x$


```python
a = 5.0
x = 4.0

math.log(a**x,a)
```




    4.0



### Natural Log ###

Logarithmic Function with a base of $e$, where $e\approx 2.7183$


```python
x = 4

math.log(x)
```




    1.3862943611198906



### Sequence ###

An ordered list of numbers. Example: $x = \left \{ 1,5,100,2,5 \right \}$. The $ith$ individual member of a sequence, $x$ is denoted $x_{i}$.


```python
x = [1,5,100,2,5]

x
```




    [1, 5, 100, 2, 5]



### Series ###

The sum of a sequence, or put another way, a sequence with plus signs between elements. Example: $\sum_{i=1}^{n}x_{i}$ is the sum of the first to the $nth$ member of a sequence, $x$.


```python
x = [1,5,100,2,5]

sum(x)
```




    113



### Derivative ###

The instanteous rate of change of a function. Can be thought of as the slope between two points, $a$ and $b$ as the distance between them approaches being infinitely small.

### Definite integral ###

The area under a curve.

### Local extrema, local maxima, local minima

A high or low point of a function.

### Global extrema, global maxima, global minima ###

The highest or lowest point of a function.

### Taylor Series ###

Describing a function by using the information contained in the deriviatives of the function.

### Critical Point ###

Any point in a function where the first derivative is 0 or doesn't exist. Basically any point where something interesting might happen.

### Inflection Point ###

A point of a function where the curve switches from concave to convex or vice versa.

### Stationary Point ###

A point of a function where the first derivative is 0. Can be thought of as either a peak or a valley floor.

### Saddle Point ###

A point of a functon where both the first and second derivative is 0.

### Concave ###

A function where the rate of increase slows as the value of the function gets bigger. Another way to think about it: if plotted in 2d, a convex function curves towards the ground.

### Convex ###

A function where the rate of increase speeds up as the value of the function gets bigger. Another way to think about it: if plotted in 2d, a convex function curves towards the sky.

### Conditional Probability ###

The probability an event occurs given whether or not another event occurs.

$Pr\left ( y\mid x = 4 \right )$ is the probability y occurs given that the event x=4 occurs.

### Combination ###

From n items, choose k items, ignoring the order in which you choose them: $\binom{n}{k}$

### Odds and Odds Ratios ###

The odds of an event are the probability of an event occurs over the probability of an event not occuring: $\frac{Pr(x)}{Pr(~x)}$

The odds ratio of two events, $x$ and $y$ are the odds of the two events:

$\frac{Pr(x)/Pr(~x)}{Pr(y)/Pr(~y)}$

### Random Variable ###

A random variable is a variable that can take an array of values, with the probability it takes a particular value determined by some random process.

A distribution of a random variable is the probability of each possible value being realized.

### Probability Mass Function & Probability Distribution Function ###

A function that defines the probability of each possible value occuring in a discrete (PMF) or continous (PDF) function.

### Bernoulli Distribution ###

Applies only to binary random variables only (e.g. coin flips). It's PMF is written as:

$$ Pr(Y = y\mid p)=\begin{cases}
1-p & \text{ for } y = 0\\
p & \text{ for } y= 1
\end{cases} $$

The Bernoulli distribution describes the ferquencey of two outcomes over repeated observations. It is built upon the assumption that the events of independent of eachother, meaning the outcome of one coin flip doesn't not affect the outcome of the second coin flip (from Moore and Siegel).

### Binomial Distribution ###

The PMF of the binomial distribution is:

$$ Pr(Y = y\mid n,p) = \binom{n}{y}p^{y}(1-p)^{n-y}$$

The binomial distribution describes any discrete distribution with three or more observations where (1) each observation is composed of a binary outcome, (2) the observations are independent, and (3) we have a record of the number of times one value was obtained (from Moore and Siegel).

### Poisson Distribution ###

The Poisson distribution the number of times you observe one event, two events, three events, etc over a fixed period of time. Put another way, it describes the distribution of event counts for rare, random events (from Moore and Siegel).

$$Pr(Y=y|u)=\frac{u^y}{y!\times e^u}$$

For example, the Poisson distribution would describe the probability of observing 10 wars in a century.

### Negative Binomial Distribution ###

The NB distribution describes the number of events occuring prior to observing the kth non-event. For example, the number of successful surgeries performed before the 6th failed surgery.

### Expectation Of Random Variables ###

The most likely value a random variable takes. Written $E[X]$.

### Moments Of A Distribution ###

Moments of a distribution are the parameters used to describe a distribution.

- First moment: Mean
- Second moment: Variance
- Third moment: Skewness
- Fourth moment: Kurtosis (flatness or peakedness)

### Uniform Distribution ###

Assigns an equal probability to all possible events.

### Gaussian-Normal Distribution ###

The bell curve. Defined by two moments: mean and variance.

### Logistic Distribution ###

Often used to model binary outcomes. Defined by two moments: mean and variance.

### Exponential Distribution ###

The exponential distribution describes events produced by a process with a constant risk of failure (from Moore and Siegel).

### Pareto Distribution ###

A distribution in which prior values affect later values.

### Gamma Distribution ###

While the exponential distribution assumes contant risk, the Gamma distribution allows risk to vary over a number of periods.

### Weibull Distribution ###

"[Weibull distribution] can be interpreted as if several processes are running in parallel, with the first to stop ending the duration. This is the weakest link mechanism, as when the failure of some part causes a machine to break down and the total operating time of the machine is the duration." (Lindsey 1995, p. 133)

### Chi-squared Distribution ###

"The sum of squares of n independent variables each distributed according to a standard normal distribution is distributed according to a chi-squared distribution." (Moore and Siegel)

### Student's t Distribution ###

This distribution looks like a normal distribution when N is big enough, but with thicker tails when N is small.

### Vector ###

An 'arrow' in n-dimensional space. For example, in a 2d coordinate plane, the vector (2,3) is x=2 and y=3.

### Length Of A Vector ###

If you think of a 2d coordinate plane, and have a vector (x,y), then you have a point at x,y. The distance from 0 (the origin) to x,y is the vector's length.

The length of vector $a$ is denoted $\left \| a \right \|$ and is calculated $\sqrt{a_{1}^{2}+a_{2}^{2}+...+a_{n}^{2}}$

### Vector Addition ###

To add two vectors, add each corresponding element. For example, for vectors $\boldsymbol{a}$ and $\boldsymbol{b}$, the sum would be $(a_{1}+b_{1}, a_{2}+b_{2}, ... a_{n}+b_{n})$

To add the lengths of two vectors, the process is the same:


$$\left \| \boldsymbol{a} + \boldsymbol{b} \right \| = \sqrt{(a_{1}+b_{1})^{2}+(a_{2}+b_{2})^{2}+...+(a_{n}+b_{n})^{2}}$$


### Multiply A Scalar By A Vector ###

Simply multiply each element of the vector by the scalar. For example:

$$c\boldsymbol{x} = (cx_{1}, cx_{2}, ... cx_{x})$$

### Dot Product ###

One way of thinking about the dot product is that if two vectors are imagined as two arrows pointing out into a 2nd coordinate plane, the dot product is the vector starting at one endpoint and going to the other endpoint.

Because if two vectors are perpendicular then the dot product is 0 (because the cosine of the angle they create is 0), the dot product is used to tell you if two vectors are perpendicular/orthogonal/independent.

$$\boldsymbol{a} \cdot  \boldsymbol{b} = a_{1}b_{1} + a_{2}b_{2} + ... a_{n}b_{n}$$

### Matrix ###

A matrix is a rectangular table of numbers of variables that contains rows and columns. It is typically described as an $n \times m$ matrix, meaning $n$ nows and $m$ columns.

$$A_{3x3} = \begin{pmatrix}
a_{11} & a_{12} & a_{31}\\
a_{21} &  a_{22}& a_{32}\\
a_{31} & a_{32} & a_{33}
\end{pmatrix}$$

### Scalar Matrix Multiplication ###

To multiply a scalar by a matrix, simply multiply each element of the matrix by the scalar.

$$2 \times \begin{bmatrix}
1 & 2\\
3 & 4
\end{bmatrix} = \begin{bmatrix}
2 & 4\\
6 & 8
\end{bmatrix}$$

### Matrix Multiplication ###

To multiply two matrices, it is simply the dot product of the each of first matrix's rows and the second matrix's columns.

$$\begin{bmatrix}
1 & 2\\
3 & 4\\
5 & 6
\end{bmatrix}\times  \begin{bmatrix}
1 &  2& 3\\ 4 &  5& 6
\end{bmatrix} = \begin{bmatrix}
(1\times1) + (2\times4)&  (1\times2) + (2\times5)& (1\times3) + (2\times6)\\
(3\times1) + (4\times4) &  (3\times2) + (4\times5)& (3\times3) + (4\times6)\\
(5\times1) + (6\times4) & (5\times2) + (6\times5) & (5\times3) + (6\times6)
\end{bmatrix} $$

### Trace Of A Matrix ###

The trace of a matrix is the sum of it's diagonal elements.

### Identity Matrix ###

A square matrix of $1$ on the diagonal elements and $0$ everywhere else.

$$\begin{bmatrix}
1 & 0\\
0 & 1
\end{bmatrix}$$

### Inverse Of A Matrix ###

The inverse of a matrix, $\boldsymbol{A}$, is a second matrix, $\boldsymbol{A}^{-1}$, such that $\boldsymbol{A} \cdot \boldsymbol{A}^{-1} = \boldsymbol{I}$, where $\boldsymbol{I}$ is an identity matrix.

### Matrix Rank ###

The rank of a matrix is the maximum number of linearly independent rows or columns.

### Eigenvalue and Eigenvector ###

An eigenvalue of a matrix is the solution to $A\boldsymbol{x}=\lambda\boldsymbol{x}$, where $\boldsymbol{x}$ is called the eigenvector, and $\lambda$ is called the eigenvalue.

If the eigenvector $\boldsymbol{x}$ is multiplied by $A$, then $\boldsymbol{x}$ ends up as a scalar multiple of itself that always stays pointed in the same direction but just gets longer or shorter. The $\lambda$ tells us how much longer or shorter it is.

In some cases like Markov Chains, researchers think of the eigenvector, $\boldsymbol{x}$, as the state of the system, and $A$ as the transition matrix between states.

### Markov Chains ##

Markov processes are memoryless, meaning there is no dependence between the present state and the past state. A Markov chain is a stochastic process that is memoryless.
