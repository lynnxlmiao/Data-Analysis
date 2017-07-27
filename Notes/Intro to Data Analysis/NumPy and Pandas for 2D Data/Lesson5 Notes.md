# NumPy and Pandas for 2D Data #
## Corrected vs. Uncorrected Standard Deviation ##
By default, Pandas' `std()` function computes the standard deviation using Bessel's correction. Calling `std(ddof=0)` ensures that Bessel's correction will not be used.
## Pearson's r in NumPy ##
NumPy's corrcoef() function can be used to calculate Pearson's r, also known as the correlation coefficient.
see: https://docs.scipy.org/doc/numpy/reference/generated/numpy.corrcoef.html
in Pearson's r, calling std(ddof=0) ensures that Bessel's correction will not be used.
![](http://i.imgur.com/SN4NP5V.png)
![](http://i.imgur.com/loUNHcc.jpg)
## Pandas Axis Names ##
![](http://i.imgur.com/WQQkU5y.png)
## DataFrame applymap() ##
![](http://i.imgur.com/gj7PZd5.png)
## DataFrame apply() ##
![](http://i.imgur.com/9oQwx7e.png)
![](http://i.imgur.com/WJuLnYE.png)
## NumPy's and Panda's .std() ##
Note that the type of standard deviation calculated by default is different between numpy's .std() and pandas' .std() functions. **By default, numpy calculates a population standard deviation, with "ddof = 0".** **On the other hand, pandas calculates a sample standard deviation, with "ddof = 1". **If we know all of the scores, then we have a population - so to standardize using pandas, we need to set "ddof = 0".
## Combining Pandas DataFrame ##
![](http://i.imgur.com/7EFW6IH.png)
## Plotting with DataFrames ##
Just like Pandas Series, DataFrames also have a plot() method. If `df` is a DataFrame, then `df.plot()` will produce a line plot with a different colored line for each variable in the DataFrame. This can be a convenient way to get a quick look at your data, especially for small DataFrames, but for more complicated plots you will usually want to use matplotlib directly.
## groupby() with as_index=False ##
```python
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

values = np.array([1, 3, 2, 4, 1, 6, 4])
example_df = pd.DataFrame({
    'value': values,
    'even': values % 2 == 0,
    'above_three': values > 3 
}, index=['a', 'b', 'c', 'd', 'e', 'f', 'g'])
```
```python 
# groupby() with as_index=False
first_even = example_df.groupby('even', as_index=False).first()
print first_even
print '\n'
print first_even['even'] # Causes an error. 'even' is no longer a column in the DataFrame
```
    even  above_three  value
0  False        False      1
1   True        False      2


0    False
1     True
Name: even, dtype: bool

```python
first_even = example_df.groupby('even').first()
print first_even
```
       above_three  value
even                     
False        False      1
True         False      2
## 3D data in NumPy ##
NumPy arrays can have arbitrarily many dimensions. Just like you can create a 1D array from a list, and a 2D array from a list of lists, you can create a 3D array from a list of lists of lists, and so on. For example, the following code would create a 3D array:
```python
a = np.array([
    [['A1a', 'A1b', 'A1c'], ['A2a', 'A2b', 'A2c']],
    [['B1a', 'B1b', 'B1c'], ['B2a', 'B2b', 'B2c']]
])
```
see: http://pandas.pydata.org/pandas-docs/stable/dsintro.html#panel