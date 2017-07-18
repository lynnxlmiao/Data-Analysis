# Part 3 Data Analysis Process #

## Syntax Unicode Error ##
See below code when opening a file:

```python
import unicodecsv

with open('C:\Files\Udacity\Data Analyst Nanodegree\Part 3\Lesson 3 Data Analysis Process Resources\enrollments.csv',
  'rb') as f:
reader = unicodecsv.DictReader(f)
enrollments = list(reader)

print(enrollments[1])
```

Run result shows:

```python
    C:\Users\MXL92\AppData\Local\Programs\Python\Python36\python.exe "C:/Files/Workspaces/PyCharm/Data Analysis.py"
      File "C:/Files/Workspaces/PyCharm/Data Analysis.py", line 3

    with open('C:\Files\Udacity\Data Analyst Nanodegree\Part 3\Lesson 3 Data Analysis Process Resources\enrollments.csv',
     ^
    SyntaxError: (unicode error) 'unicodeescape' codec can't decode bytes in position 8-12: truncated \UXXXXXXXX escape
    
    Process finished with exit code 1
```

The problem here is the file path: C:\Files`**\U**`dacity\Data Analyst Nanodegree\Part 3\Lesson 3 Data Analysis Process Resources\enrollments.csv, 
the first backslash in the string is being interpreted as a special character, in fact because it's followed by a "U" it's being interpreted as the start of a unicode code point.

Three ways to solve this error:
See: https://stackoverflow.com/questions/18084554/why-do-i-get-a-syntaxerror-for-a-unicode-escape-in-my-file-path
Use a raw string, double your slashes or use forward slashes instead:
```python
    r'C:\Users\expoperialed\Desktop\Python'
    'C:\\Users\\expoperialed\\Desktop\\Python'
    'C:/Users/expoperialed/Desktop/Python'
```
In regular python strings, the `\U` character combination signals a extended Unicode codepoint escape.


## Removing an Element from a Dictionary ##
-call `.pop` on the dictionary, returns the item that was removed.
-call `.del` on the dictionary, returns the nutated dictionary.
```python
del d[key]
```
see: https://stackoverflow.com/questions/5844672/delete-an-item-from-a-dictionary
However, this mutates the existing dictionary so the contents of the dictionary changes for anybody else who has a reference to the same instance. To return a new dictionary, make a copy of the dictionary:
```python
def removekey(d, key):
    r = dict(d)
    del r[key]
    return r
```

## Create a dictionary (defaultdict) ##
```python
engagement_by_account = defaultdict(list)
```
It allows to specify a default value. In this case, it specified `list`, means if I ever try to look up a key in the dictionary and that key is not there, I'll get the empty list instead. This will be helpful.

## Making histograms in Python ##
To make a histogram in Python, you can use the matplotlib library, which comes with Anaconda. The following code will make a histogram of an example list of data points called data.
```python
data = [1, 2, 1, 3, 3, 1, 4, 2]

%matplotlib inline
import matplotlib.pyplot as plt
plt.hist(data)
```
The line %matplotlib inline is specifically for IPython notebook, and causes your plots to appear in your notebook rather than a new window. If you are not using IPython notebook, you should not include this line, and instead you should add the line plt.show() at the bottom to show the plot in a new window.
```python
%pylab inline
```
Add this so that the plots would show up within my notebook and not in a separate window.

**Adding labels and titles**
In matplotlib, you can add axis labels using `plt.xlabel("Label for x axis")` and `plt.ylabel("Label for y axis")`. For histograms, you usually only need an x-axis label, but for other plot types a y-axis label may also be needed. You can also add a title using `plt.title("Title of plot")`.

**Making plots look nicer with seaborn**
You can automatically make matplotlib plots look nicer using the seaborn library. This library is not automatically included with Anaconda, but Anaconda includes something called a package manager to make it easier to add new libraries. The package manager is called conda, and to use it, you should open the Command Prompt (on a PC) or terminal (on Mac or Linux), and type the command `conda install seaborn`.

If you are using a different Python installation than Anaconda, you may have a different package manager. The most common ones are pip and easy_install, and you can use them with the commands `pip install seaborn` or `easy_install seaborn` respectively.

Once you have installed seaborn, you can import it anywhere in your code using the line `import seaborn as sns`. Then any plot you make afterwards will automatically look better. Give it a try!

If you're wondering why the abbreviation for seaborn is sns, it's because seaborn was named after the character Samuel Norman Seaborn from the show The West Wing, and sns are his initials.

The seaborn package also includes some extra functions you can use to make complex plots that would be difficult in matplotlib. We won't be covering those in this course, but if you'd like to see what functions seaborn has available, you can look through the documentation.

**Adding extra arguments to your plot**
You'll also frequently want to add some arguments to your plot to tune how it looks. You can see what arguments are available on the documentation page for the hist function. One common argument to pass is the `bins` argument, which sets the number of bins used by your histogram. For example, `plt.hist(data, bins=20)` would make sure your histogram has 20 bins.

