# R Basics #
## Install RStudio on Windows ##
[FIRST Install R Programming Language](https://cran.rstudio.com/)
[Install RStudio](https://www.rstudio.com/products/rstudio/download/#download)

RStudio new file: File/New File/R Script

## RStudio Layout ##
All four panels are configurable. The layout discussed is the default layout for RStudio. 
You can change the default layout by going to Tools -> Options…

[A Beginner's Guide to R: Introduction](http://www.computerworld.com/article/2497143/business-intelligence/business-intelligence-beginner-s-guide-to-r-introduction.html)by Sharon Machlis.

[Quick Guide to R Layout](http://dss.princeton.edu/training/RStudio101.pdf)

## Demystifying R ##
We recommend anyone new to R and RStudio to try Swirl (statistics with interactive R learning). Swirl is a software package for the R statistical programming language. Its purpose is to teach statistics and R commands interactively.

Type the following commands in the Console, pressing Enter or Return after each line:
```
install.packages("swirl")
library(swirl)
swirl()
```
Note that the > symbol at the beginning of the line is R's prompt for you type something into the console. We include it here so you know that the above commands are to be typed into the console and not elsewhere. The part you type begins after >. 

## swirl ##
```
| You can exit swirl and return to the R prompt (>) at any time by pressing the Esc key. If you
| are already at the prompt, type bye() to exit and save your progress. When you exit properly,
| you'll see a short message letting you know you've done so.

| When you are at the R prompt (>):
| -- Typing skip() allows you to skip the current question.
| -- Typing play() lets you experiment with R on your own; swirl will ignore what you do...
| -- UNTIL you type nxt() which will regain swirl's attention.
| -- Typing bye() causes swirl to exit. Your progress will be saved.
| -- Typing main() returns you to swirl's main menu.
| -- Typing info() displays these options again.

| Let's get started!
```
```
| Leaving swirl now. Type swirl() to resume.
```
```
#The arrow-like
# '<-' symbol is the assignment operator in R, similar to the
# equal sign '=' in other programming languages. The c() is a
# generic function that combines arguments, in this case the
# names of people, to form a vector.
```

## Getting Help ##
[Quick R](http://www.statmethods.net/)
[R Cookbook](http://www.cookbook-r.com/)
[R-Bloggers](https://www.r-bloggers.com/)
[StackOverflow About R](https://stackoverflow.com/tags/r/info)
[StackOverflow R FAQ](https://stackoverflow.com/questions/tagged/r-faq%20)
[Google's R Style Guide](https://google.github.io/styleguide/Rguide.xml)

## Read and Subset Data ##
[Loading Data and Basic Formatting in R](http://flowingdata.com/2015/02/18/loading-data-and-basic-formatting-in-r/)
[How to SUbset Data](http://www.statmethods.net/management/subset.html)

**Current Working Directory**
```R
getwd()
```

**Change Working Directory**
```R
setwd('')  #with forward slash '/'
```
**Read .csv**
```R
stateInfo<-read.csv('stateData.csv')   #stateInfo is the variable
```
## R Markdown Ducuments ##
**Add Chunks**
```Ctrl + Alt + I```
**Use KNIT HTML**

install and load knitr:
```
install.packages('knitr', dependencies = T)
library(knitr)
```

The str() and summary() functions are helpful commands when working with a new data set.
The str() function gives us the variable names and their types.
The summary() function gives us an idea of the values a variable can take on.

```{r}
data(mtcars)
str(mtcars)

subset(mtcars, mpg >=30 | hp <=60)
# same as below:
mtcars[mtcars$mpg>=30 | mtcars$hp<60,]
```
## Install ggplot2 libraty ##
```
install.packages('ggplot2', dependencies = T)
library(ggplot2)
```
## ggplot2 ##
```R
library(ggplot2)
qplot(data = reddit, x = age.range)
```
[Learn how to set and order factor levels](http://stats.idre.ucla.edu/r/modules/factor-variables/)
 **Setting Levels of Ordered Factors**
```R
reddit <- read.csv('reddit.csv')
table(reddit$employment.status)

str(reddit)
levels(reddit$age.range)

library(ggplot2)
qplot(data = reddit, x = age.range)

# Setting levels of Ordered Factors Solution
reddit$age.range <- ordered(reddit$age.range, levels = c('Under 18', '18-24','25-34','35-44','45-54','55-64','65 of Above'))
qplot(data = reddit, x = age.range)

# Alternate Solution
reddit$age.range <- factor(reddit$age.range, levels = c('Under 18', '18-24','25-34','35-44','45-54','55-64','65 of Above'), ordered = T)
qplot(data = reddit, x = age.range)
```
## Data Munging ##
[Loading data into R](http://flowingdata.com/2015/02/18/loading-data-and-basic-formatting-in-r/)
[Tidy Data](http://vita.had.co.nz/papers/tidy-data.pdf)
[Tidy Data Presentation](http://courses.had.co.nz.s3-website-us-east-1.amazonaws.com/12-rice-bdsi/slides/07-tidy-data.pdf)

# Explore One Variable #
## Pseudo_facebook User Data ##
**Reading in Data
```{r}
getwd()
list.files()
pf <- read.csv('pseudo_facebook.tsv', sep = '\t')
names(pf)
```
## Histogram Of Users' Birthdays ##
[How to read Histograms and use them in R](http://flowingdata.com/2014/02/27/how-to-read-histograms-and-use-them-in-r/)

**ggthemes**
```
install.packages('ggthemes', dependencies = TRUE)
library(ggthemes)
```

Chris is using ```theme_minimal()``` with the font size set to 24, which is why his output might look slightly different than yours. You can set the same theme in R by running the following code, or you can set the theme to a choice of your own. 
```theme_set(theme_minimal(24))```

Instead of using the qplot() function, you can also use the ggplot() function to create the histogram:
```
ggplot(aes(x = dob_day), data = pf) +
  geom_histogram(binwidth = 1) +
  scale_x_continuous(breaks = 1:31)
```
**Moira's Investigation**
[Moira's Investigation](http://hci.stanford.edu/publications/2013/invisibleaudience/invisibleaudience.pdf)
 
## Faceting ##
[Faceting in ggplot2](http://www.cookbook-r.com/Graphs/Facets_(ggplot2)/)
**Equivalent ggplot syntax:**
```
ggplot(data = pf, aes(x = dob_day)) +
  geom_histogram(binwidth = 1) +
  scale_x_continuous(breaks = 1:31) +
  facet_wrap(~dob_month)
```
**Facet Syntax**
```facet_wrap(formula)```
```facet_wrap(~variable)```
```facet_grid(formula)```
```facet_grid(vertical~horizontal)```
 ## Friend Count ##
Create a histogram of friend_count using the ```qplot()``` syntax. We'll also accept the ```ggplot()``` syntax if you are familiar with it but additional parameters for setting the bin width or color won't be accepted. Keep it simple.
```R
ggplot(aes(x = friend_count), data = pf) +
  geom_histogram()
```
**Limitint The Axes**
[Scales in ggplot2](http://ggplot2.tidyverse.org/reference/scale_continuous.html)
```
ggplot(aes(x = friend_count), data = pf) +
  geom_histogram() +
  scale_x_continuous(limits = c(0, 1000))
```
**Adjusting The Bin Width**
Original code:
```
qplot(x = friend_count, data = pf, binwidth = 25) +
  scale_x_continuous(limits = c(0, 1000), breaks = seq(0, 1000, 50))
```

Equivalent ggplot syntax:
```
ggplot(aes(x = friend_count), data = pf) +
  geom_histogram(binwidth = 25) +
  scale_x_continuous(limits = c(0, 1000), breaks = seq(0, 1000, 50))
```

In the alternate solution below, the period or dot in the formula for ```facet_grid()``` represents all of the other variables in the data set. Essentially, this notation splits up the data by gender and produces three histograms, each having their own row.
```
qplot(x = friend_count, data = pf) +
  facet_grid(gender ~ .)
```

Equivalent ggplot syntax:
```
ggplot(aes(x = friend_count), data = pf) +
  geom_histogram() +
  scale_x_continuous(limits = c(0, 1000), breaks = seq(0, 1000, 50)) +
  facet_wrap(~gender)
```

**Consider gender**
```
qplot(x = friend_count, data = pf, binwidth = 25) +
  scale_x_continuous(limits = c(0, 1000), breaks = seq(0, 1000, 50)) + facet_wrap(~gender)
```

## Omitting NA Observations (subset) ##
```
ggplot(aes(x = friend_count), data = subset(pf, !is.na(gender))) +
  geom_histogram() +
  scale_x_continuous(limits = c(0, 1000), breaks = seq(0, 1000, 50)) +
  facet_wrap(~gender)
```
**Statistics 'By' Gender**
```
by(pf$friend_count, pf$gender, summary)
```

**Median is more robust statistic than mean.**

## Tenure ##
The parameter ```color``` determines the color outline of objects in a plot.

The parameter ```fill``` determines the color of the area inside objects in a plot.

You might notice how the color ```black``` and the hex code color of ```#099DD9``` (a shade of blue) are wrapped inside of ```I()```. The ```I()``` functions stand for 'as is' and tells ```qplot``` to use them as colors.

[ggplot theme documentation](http://ggplot2.tidyverse.org/reference/theme.html)

Equivalent ggplot syntax for plots:
```
ggplot(aes(x = tenure), data = pf) +
  geom_histogram(binwidth = 30, color = 'black', fill = '#099DD9')

ggplot(aes(x = tenure/365), data = pf) +
  geom_histogram(binwidth = .25, color = 'black', fill = '#F79420')
```

**Labeling Plots**
```
ggplot(aes(x = tenure / 365), data = pf) +
  geom_histogram(color = 'black', fill = '#F79420') +
  scale_x_continuous(breaks = seq(1, 7, 1), limits = c(0, 7)) +
  xlab('Number of years using Facebook') +
  ylab('Number of users in sample')
```

**User Ages**
```
qplot(x = age, data = pf, 
	  color = I('black'), fill = I('#5768A8'))
```

## Transforming Data ##
[Create Multiple Plots in One Image Output](http://lightonphiri.org/blog/ggplot2-multiple-plots-in-one-graph-using-gridextra)
[Add Log or Sqrt Scales to an Axis](http://ggplot2.tidyverse.org/reference/scale_continuous.html)
[Assumptinos of Linear Regression](https://en.wikipedia.org/wiki/Linear_regression#Assumptions)
[Normal Distribution](https://en.wikipedia.org/wiki/Normal_distribution)
[Log Transformations of Data](https://www.r-statistics.com/2013/05/log-transformations-for-skewed-and-wide-distributions-from-practical-data-science-with-r/)

**Engagements Variables**
very long tails

**Over-dispersed**

**Transform variable by taking the log**
Either use natural log, log base 2 or log base 10.
Also we can use other functions such as square root, to see patterns more clearly, without being distracted by the tails.
A lot of common statistical techniques, like linear regression, are based on the assumption that variables have normal distributions.
```R
p1 <- ggplot(aes(x = friend_count), data = pf) + geom_histogram()
p2 <- p1 + scale_x_log10()
p3 <- p1 + scale_x_sqrt()

grid.arrange(p1, p2, p3, ncol = 1)
```
other syntax to realize
```
p1 <- qplot(x = friend_count, data = pf)
p2 <- qplot(x = log10(friend_count + 1), data = pf)
p3 <- qplot(x = sqrt(friend_count), data = pf)

grid.arrange(p1, p2, p3 ncol = 1)
```
##Frequency Polygons##
Note that the shape of the frequency polygon depends on how our bins are set up - the height of the lines are the same as the bars in individual histograms, but the lines are easier to make a comparison with since they are on the same axis.

```R
ggplot(aes(x = friend_count, y = ..count../sum(..count..)),
       data = subset(pf, !is.na(gender))) +
  geom_freqpoly(aes(color = gender), binwidth=10) +
  scale_x_continuous(limits = c(0, 1000), breaks = seq(0, 1000, 50)) +
  xlab('Friend Count') +
  ylab('Proportion of users with that friend count')
```