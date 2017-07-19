# NumPy and Pandas for 1D Data #
## 1D Data Structures ##
![](http://i.imgur.com/OblAeTs.png)
## NumPy Arrays compared with Pythons Lists ##
![](http://i.imgur.com/yIErGG5.png)
**np.array**
```python
import numpy as np

# First 20 countries with employment data
countries = np.array([
    'Afghanistan', 'Albania', 'Algeria', 'Angola', 'Argentina',
    'Armenia', 'Australia', 'Austria', 'Azerbaijan', 'Bahamas',
    'Bahrain', 'Bangladesh', 'Barbados', 'Belarus', 'Belgium',
    'Belize', 'Benin', 'Bhutan', 'Bolivia',
    'Bosnia and Herzegovina'
])
```
```python
# Employment data in 2007 for those 20 countries
employment = np.array([
    55.70000076,  51.40000153,  50.5       ,  75.69999695,
    58.40000153,  40.09999847,  61.5       ,  57.09999847,
    60.90000153,  66.59999847,  60.40000153,  68.09999847,
    66.90000153,  53.40000153,  48.59999847,  56.79999924,
    71.59999847,  58.40000153,  70.40000153,  41.20000076
])
```
**Accessing elements**
```python
# Change False to True for each block of code to see what it does

# Accessing elements
if False:
    print countries[0]
    print countries[3]

# Slicing
if False:
    print countries[0:3]
    print countries[:3]
    print countries[17:]
    print countries[:]

# Element types
if False:
    print countries.dtype
    print employment.dtype
    print np.array([0, 1, 2, 3]).dtype
    print np.array([1.0, 1.5, 2.0, 2.5]).dtype
    print np.array([True, False, True]).dtype
    print np.array(['AL', 'AK', 'AZ', 'AR', 'CA']).dtype
```
**NumPy Functions**
```python
# Numpy functions
if False:
    print employment.mean()
    print employment.std()
    print employment.max()
    print employment.sum()
```
**.argmax() returns the index of the max item**
```python
def max_employment(countries, employment):
    '''
    Fill in this function to return the name of the country
    with the highest employment in the given employment
    data, and the employment in that country.
    '''
    
    for i in range(len(employment)):
        i = employment.argmax()
        max_country = countries[i]
        max_value = employment[i]
        

    return (max_country, max_value)
```
![](http://i.imgur.com/Hi2rB1G.png)
![](http://i.imgur.com/8W8KwVr.png)
![](http://i.imgur.com/5T250Ub.png)
## Bitwise Operations ##
In NumPy, `a & b` performs a bitwise and of `a` and `b`. This is not necessarily the same as a **logical and**, if you wanted to see if matching terms in two integer vectors were non-zero. However, if `a` and `b` are both arrays of booleans, rather than integers, **bitwise and** and **logical and** are the same thing. If you want to perform a **logical and** on integer vectors, then you can use the NumPy function `np.logical_and(a, b)` or convert them into boolean vectors first.

Similarly, `a | b` performs a **bitwise or**, and `~a` performs a **bitwise not**. However, if your arrays contain booleans, these will be the same as performing **logical or** and **logical not**. NumPy also has similar functions for performing these logical operations on integer-valued arrays.

For the quiz, assume that the number of males and females are equal i.e. we can take a simple average to get an overall completion rate.

In the solution, we may want to `/ 2.` instead of just `/ 2`. This is because in Python 2, dividing an integer by another integer (`2`) drops fractions, so if our inputs are also integers, we may end up losing information. If we divide by a float (`2.`) then we will definitely retain decimal values.
**NumPY Index Arrays**
![](http://i.imgur.com/NPirGJS.png)
**+ vs. +=**
![](http://i.imgur.com/b8cJ4Au.png)
![](http://i.imgur.com/QEGAFNQ.png)
**IMPORTANT: In-Place vs. Not In-Place**
See different behavior here for modifying a NumPy array:
![](http://i.imgur.com/mtkNTeG.png)
**pandas.Series.idxmax**
Series.idxmax(axis=None, skipna=True, *args, **kwargs)[source]
Index of first occurrence of maximum of values.
http://pandas.pydata.org/pandas-docs/stable/generated/pandas.Series.idxmax.html
`Parameters:`	`skipna : boolean, default True. Exclude NA/null values`
`Returns:`	`idxmax : Index of maximum of values`

**pandas.Series.loc vs. pandas.Series.iloc**
- `loc` works on labels in the index.
- `iloc` works on the positions in the index (so it only takes integers).
- `ix` usually tries to behave like `loc` but falls back to behaving like `iloc` if the label is not in the index.

**Filling Missing Values**
Remember that Jupyter notebooks will just print out the results of the last expression run in a code cell as though a print expression was run. If you want to save the results of your operations for later, remember to assign the results to a variable or, for some Pandas functions like .dropna(), use inplace = True to modify the starting object without needing to reassign it.

**Add two pandas.series without NaN**
```python
s1.add(s2, fill_value = 0)
```
or
```python
s = s1 + s2
s.fillna(0)
```

**Pandas Series apply()**
```python
s = pd.Series([1, 2, 3, 4, 5])
def add_one(x):
    return x + 1
print s.apply(add_one)
```
result:
0  2
1  3
2  4
3  5
4  6
dtype: int64

**Plotting in Pandas**
If the variable data is a NumPy array or a Pandas Series, just like if it is a list, the code:
```python
import matplotlib.pyplot as plt
plt.hist(data)
```
will create a histogram of the data.
Pandas also has built-in plotting that uses matplotlib behind the scenes, so if `data` is a Series, you can create a histogram using `data.hist()`.

There's no difference between these two in this case, but sometimes the Pandas wrapper can be more convenient. For example, you can make a line plot of a series using `data.plot`(). The index of the Series will be used for the x-axis and the values for the y-axis.
 If you're running plotting code locally, you may need to add the line `plt.show()` depending on your setup.
```python
%pylab inline
employment_us.plot()
```