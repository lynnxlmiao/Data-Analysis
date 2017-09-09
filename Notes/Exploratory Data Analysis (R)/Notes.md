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
```R
theme_set(theme_minimal(24))
```

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
Note that sum(..count..) will sum across color, so the proportions displayed are based on total users. To plot these proportions within each group, you can try y = ..density...

Equivalent ggplot syntax for solution video:

```R
ggplot(aes(x = www_likes), data = subset(pf, !is.na(gender))) +
  geom_freqpoly(aes(color = gender)) +
  scale_x_log10()
```

## Likes on the Web ##
```R
by(pf$www_likes, pf$gender, sum)
```

## Box Plots ##
[How to read and use a Boxplot](http://flowingdata.com/2008/02/15/how-to-read-and-use-a-box-and-whisker-plot/)
```R
qplot(x = gender, y = friend_count, 
      data = subset(pf, !is.na(gender)),
	  geom = 'boxplot', ylim = c(0, 1000))

qplot(x = gender, y = friend_count, 
      data = subset(pf, !is.na(gender)),
	  geom = 'boxplot') + 
  scale_y_continuous(limits = c(0,1000))

qplot(x = gender, y = friend_count,
      data = subset(pf, !is.na(gender)),
      geom = 'boxplot') +
  coord_cartesian(ylim = c(0, 1000))
```

## Box Plots, Quartiles, and Friend Requests ##
```R
qplot(x = gender, y = friend_count, 
      data = subset(pf, !is.no(gender)),
      geom = 'boxplot') + 
   coord_cartesion(ylim = c(0, 250))

by(pf$friend_count, pf$gender, summary)
```
## Getting Logical ##
```R
summary(pf$mobile_likes)

summary(pf$mobile_likes > 0)

mobile_check_in <- NA  # This creates a new variable in the data frame with NA values.
pf$mobile_check_in <- ifelse(pf$mobile_likes > 0, 1, 0)
pf$mobile_check_in <- factor(pf$mobile_check_in)
summary(pf$mobile_check_in)
```
The ```sum()``` function will not work since ```mobile_check_in``` is a factor variable. You can use the ```length()``` function to determine the number of values in a vector.
We could have also made ```mobile_check_in``` to hold boolean values. The ```sum()```function will work on booleans (true is 1, false is 0).

```R
summary(pf$mobile_check_in)
sum(pf$mobile_check_in == 1)/length(pf$mobile_check_in)
```

##Data Wrangling with R##
Data munging or data wrangling can take up much of a data scientist's or data analyst's time. There are two R packages that make these tasks easier in R: tidyr and dplyr.
**tidyr**-a package that reshapes the layout of your data
**dplyr**-a package that helps you transform tidy, tabular data
Review [Data Wrangling in R](https://s3.amazonaws.com/udacity-hosted-downloads/ud651/DataWranglingWithR.pdf) to get a sense of how these packages allow you to manipulate data.

There are some useful cheat sheets on [RStudio's webpage](https://s3.amazonaws.com/udacity-hosted-downloads/ud651/DataWranglingWithR.pdf). The Data Import and Data Transformation sheets will be good references for working with tidyr and dplyr, respectively.

##Exploring Your Friends' Birthdays##
[Download Your Friends' Birthdays from Facebook](https://www.facebook.com/help/152652248136178/)

[Date Formats in R](https://www.r-bloggers.com/date-formats-in-r/)

[Export a GOogle Calendar](https://support.google.com/calendar/answer/37111?hl=en)

[Google Calendar to Excel: Free Trial](https://www.gcal2excel.com/)


#Explore Two Variables#
##Scatterplots##

You can also read in the data using the following code:
```R
read.delim('pseudo_facebook.tsv')
```
The equivalent ggplot syntax for the scatterplot:
```R
ggplot(aes(x = age, y = friend_count), data = pf) +
  geom_point()
```
```R
library(ggplot2)
pf <- read.csv('C:/Files/Udacity/Data-Analysis/Notes/Exploratory Data Analysis (R)/R Basics/eda-course-materials/lesson3/pseudo_facebook.tsv', sep = '\t')
#sep="\t" tells R that the file is tab-delimited (use " " for space delimited and "," for comma delimited; use "," for a .csv file)

qplot(x = age, y = friend_count, data = pf)
#qplot(age, friend_count, data = pf)
```

[ggplot2 tutorial by Ramon Saccilotto](https://classroom.udacity.com/nanodegrees/nd002/parts/0021345407/modules/316518875375460/lessons/755298985/concepts/8651687310923)
[ggplot2 geoms](http://ggplot2.tidyverse.org/reference/)

##Overplotting##
alpha and jitter
```R
ggplot(aes(x = age, y = friend_count), data = pf)  + 
  geom_jitter(alpha = 1/20) + 
  xlim(13, 90)

summary(pf$age)
```

##Coord_trans()##
[coord_trans()](http://docs.ggplot2.org/current/coord_trans.html)

##Alpha and Jitter##
 jitter使某每一个点在x轴的方向上产生随机的偏移, 从而减少了图形重叠的问题, 另一种介绍重叠的方式是改变点的透明度alpha, 将在实战中的地图讨论
```R
#Explore the relationship between friends initiated(y) vs age(x).
ggplot(aes(x = age, y = friendships_initiated), data = pf)  + 
  geom_jitter(alpha = 1/10, position = position_jitter(h = 0)) + 
  coord_trans(y = 'sqrt')
```
##Conditional Means##
**Important Notice**: Please note that in newer versions of dplyr (0.3.x+), the syntax %.% has been deprecated and replaced with %>%.

Another warning: Version 0.4.0 of dplyr has a bug when using the median function on the summarize layer, depending on the nature of the data being summarized. You may need to cast the data as a numeric (float) type when using it on your local machine, e.g. ```median(as.numeric(var))```.

[dplyr package](https://blog.rstudio.com/2014/01/17/introducing-dplyr/)
[Introduction to dplyr (knitted html file)](http://rstudio-pubs-static.s3.amazonaws.com/11068_8bc42d6df61341b2bed45e9a9a3bf9f4.html)

There are other ways to work with data and create new data frames without using the dplyr package. Learn about the R functions lapply, tapply, and split in a [blog post](https://rollingyours.wordpress.com/2014/10/20/the-lapply-command-101/).

For more on geom_line(), you can check the documentation [here](http://ggplot2.tidyverse.org/reference/geom_path.html).

##Cnditional Means##
```R
install.packages('dplyr')
library(dplyr)
```
```R
age_groups <- group_by(pf, age)
summarise(age_groups,
          friend_count_mean = mean(friend_count),
          friend_count_median = median(friend_count),
          n = n())
pf.fc_by_age <- arrange(pf.fc_by_age, age)
head(pf.fc_by_age)
```
Function chain ```%>%```
```R
pf.fc_by_age <- pf %>%
  group_by(age) %>%
  summarise(friend_count_mean = mean(friend_count),
          friend_count_median = median(friend_count),
          n = n()) %>%
  arrange(age)

head(pf.fc_by_age)
```
```R
# Plot mean friend count vs. age using a line graph.
# Be sure you use the correct variable names
# and the correct data frame. You should be working
# with the new data frame created from the dplyr
# functions. The data frame is called 'pf.fc_by_age'.

# Use geom_line() rather than geom_point to create
# the plot. You can look up the documentation for
# geom_line() to see what it does.

ggplot(aes(x = age, y = friend_count_mean), data = pf.fc_by_age)  + 
  geom_line()
```

##Overlaying Summaries with Raw Data##
**Note**:ggplot 2.0.0 changes the syntax for parameter arguments to functions when using stat = 'summary'. To denote parameters that are being set on the function specified by fun.y, use the fun.args argument, e.g.:
```R
ggplot( ... ) +
  geom_line(stat = 'summary', fun.y = quantile,
            fun.args = list(probs = .9), ... )
#stat参数表示统计的类型，而fun.y则表示应用于统计的函数
```

To zoom in, the code should use the```coord_cartesian(xlim = c(13, 90))``` layer rather than ```xlim(13, 90)``` layer.

Look up documentation for coord_cartesian() and quantile() if you're unfamiliar with them.

Try an example and practice problem for calculating [quantiles (percentiles)](http://www.r-tutor.com/elementary-statistics/numerical-measures/percentile).

```R
ggplot(aes(x = age, y = friend_count), data = pf) +
  #xlim(13, 90) +    replace by coord_cartesian
  coord_cartesian(xlim = c(13, 70), ylim = c(0, 1000)) +
  geom_point(alpha = 0.05,
             position = position_jitter(h = 0),
             color = 'orange') +
  #coord_trans(y = 'sqrt') +  replace by coord_cartesian
  geom_line(stat = 'summary', fun.y = mean) +
  geom_line(stat = 'summary', fun.y = quantile, 
            fun.args = list(probs = .1), 
            linetype = 2, color = 'blue') +
  geom_line(stat = 'summary', fun.y = quantile, 
            fun.args = list(probs = .5), 
            color = 'blue') +
  geom_line(stat = 'summary', fun.y = quantile, 
            fun.args = list(probs = .9), 
            linetype = 2, color = 'blue')
```
##Correlation##
[Correlation Coefficient](http://www.r-tutor.com/elementary-statistics/numerical-measures/correlation-coefficient)
[A Visual Guide to Correlation](https://s3.amazonaws.com/udacity-hosted-downloads/ud651/correlation_images.jpeg)
[Intro to Inferential Statistics - Correlation](https://classroom.udacity.com/courses/ud201/lessons/1345848540/concepts/1715827370923)
Correlation coefficients are often denoted with the greek letter ρ (rho), in addition to the letter r.

The default method for computing the correlation coefficient is Pearson, and this is true for most statistical software. You do not need to pass the method parameter when calculating the Pearson Product Moment Correlation.
```R
cor.test(pf$age, pf$friend_count, method = 'pearson')
```
```R
with(pf, cor.test(age, friend_count, method = 'pearson'))
```

**ostensibly** - apparently or purportedly, but perhaps not actually.

##Correlation on Subsets##
```R
with(subset(pf, age <= 70), cor.test(age, friend_count), method = 'pearson')
#method = 'pearson' can be removed since cor.test default method is 'pearson'
```

##Create Scatterplots##
```R
ggplot(aes(x = www_likes_received, y = likes_received), data = pf) +
  geom_point()
```

##Strong Correlations##
The correlation coefficient is invariant under a linear transformation of either X or Y, and the slope of the regression line when both X and Y have been transformed to z-scores is the correlation coefficient.

It's important to note that we may not always be interested in the bulk of the data. Sometimes, the outliers ARE of interest, and it's important that we understand their values and why they appear in the data set.

##More Caution With Correlation##
Argument matching (when not providing them by name) in R is a bit complex.

First, arguments (or parameters) can be matched by name. If a parameter matches exactly, it is "removed" from the argument list and the remaining unnamed arguments are matched in the order that they are listed in the function definition.

R does the following to match arguments... 

+ checks for exact match of named argument
+ checks for a partial match of the argument
+ checks for a positional match

If R does not find a match for a parameter, it typically throws an "unused" parameter error.

Type ```str(functionName)``` to find the order of the parameters and learn more about the parameters of an R function. 

**install alr3**
```R
install.packages('alr3')
library(alr3)
data(Mitchell)
```

##Noisy Scatterplots##
```R
cor.test(Mitchell$Month, Mitchell$Temp)
```

##Making Sense of Data##
As of ggplot 2.0, you will need to use a ```scale_x_continuous()``` layer instead of ```scale_x_discrete()```, since the Month is considered a numeric variable.

To see the range of Mitchell$Month:
```R
>range(Mitchell$Month)
[1] 0 203
```
```R
ggplot(data = Mitchell, aes(x = Month, y = Temp)) +
  geom_point() +
  scale_x_discrete(breaks = seq(0, 203, 12))
```

##A New Perspective##
You could also get perspective on this data by overlaying each year's data on top of each other, giving a clear, generally sinusoidal graph. You can do this by using the R's [modulus](https://en.wikipedia.org/wiki/Modular_arithmetic) operator %% in your code. Try running the code below!

```R
ggplot(aes(x=(Month%%12),y=Temp), data=Mitchell)+
  geom_point()
```

There are other measures of associations that can detect this. The ```dcor.ttest()``` function in the **energy** package implements a non-parametric test of the independence of two variables. While the Mitchell soil dataset is too coarse to identify a significant dependency between "Month" and "Temp", we can see the difference between ```dcor.ttest``` and ```cor.test``` through other examples, like the following:
```R
x <- seq(0, 4*pi, pi/20)
y <- cos(x)
qplot(x = x, y = y)
dcor.ttest(x, y)
```

The ```cor``` and ```cor.test``` functions determine the strength of a linear relationship, but they may miss other relationships in the data.
The Instructor Notes of the solution video includes a statistical test that would pick up this pattern. It also contains comments about data visualizations you don't want to miss!
```R
ggplot(aes(x=(Month%%12),y=Temp), data=Mitchell)+
  geom_point()
```
```R
dcor.ttest
```
##Understanding Noise: Age to Age Months##
```R
# Create a new variable, 'age_with_months', in the 'pf' data frame.
# Be sure to save the variable in the data frame rather than creating
# a separate, stand-alone variable. You will need to use the variables
# 'age' and 'dob_month' to create the variable 'age_with_months'.

# Assume the reference date for calculating age is December 31, 2013.
pf$age_with_months <- pf$age + (12 - pf$dob_month)/12
```

##Age with Months Means##
**Important Notice!** Please note that in newer versions of dplyr (0.3.x+), the syntax ```%.%``` has been deprecated and replaced with ```%>%```. Videos in the course use %.%, which will produce warning messages. If you answer using the chain operator, you should use ```%>%``` instead. Another warning: Version 0.4.0 of dplyr has a bug when using the median function on the summarize layer, depending on the nature of the data being summarized. You may need to cast the data as a numeric (float) type to get the expected results, e.g. ```median(as.numeric(var))```. 

A few additional hints follow below: 
**Hint 1**: Use the ```group_by()```, ```summarise()```, and ```arrange()``` functions in the dplyr package to split the data frame by ```age_with_month```. Make sure you arrange by the correct variable (it's not ```age``` anymore). 
**Hint 2**: The code should look similar to the code when we split the data frame by age and found summaries:
```R
age_groups <- group_by(pf, age)
pf.fc_by_age <- summarise(age_groups,
                          friend_count_mean = mean(friend_count),
                          friend_count_median = median(friend_count),
                          n = n())
pf.fc_by_age <- arrange(pf.fc_by_age, age)
head(pf.fc_by_age)
```

```R
# Create a new data frame called
# pf.fc_by_age_months that contains
# the mean friend count, the median friend
# count, and the number of users in each
# group of age_with_months. The rows of the
# data framed should be arranged in increasing
# order by the age_with_months variable.

# For example, the first two rows of the resulting
# data frame would look something like...

# age_with_months  friend_count_mean	friend_count_median	n
#              13            275.0000                   275 2
#        13.25000            133.2000                   101 11

pf.fc_by_age_months <- pf %>%
  group_by(age_with_months) %>%
  summarise(friend_count_mean = mean(friend_count),
           friend_count_median = median(friend_count),
           n = n()) %>%
  arrange(age_with_months)

head(pf.fc_by_age_months)
```
```R
#Alternate Solution
age_with_months_groups <- group_by(pf, age_with_months)
pf.fc_by_age_months2 <- summarise(age_with_months_groups,
                                  friend_count_mean = mean(friend_count),
                                  friend_count_median = median(friend_count),
                                  n = n())

pf.fc_by_age_months2 <- arrange(pf.fc_by_age_months2, age_with_months)

head(pf.fc_by_age_months2)
```

##Noise in Conditional Means##
```R
# This programming assignment will not be graded, but when you submit your code,
# the assignment will be marked as correct. By submitting your code, we can add
# to the feedback messages and address common mistakes in the Instructor Notes.

ggplot(aes(x = age_with_months, y = friend_count_mean),
       data = subset(pf.fc_by_age_months, age_with_months < 71)) +
  geom_line()
```

##Smoothing Conditional Means##
```R
p1 <- ggplot(aes(x = age, y = friend_count_mean),
             data = subset(pf.fc_by_age, age < 71)) +
  geom_line() +
  geom_smooth()

p2 <- ggplot(aes(x = age_with_months, y = friend_count_mean),
             data = subset(pf.fc_by_age_months, age_with_months < 71)) +
  geom_line() +
  geom_smooth()

p3 <- ggplot(aes(x = round(age / 5) * 5, y = friend_count),
             data = subset(pf, age < 71)) +
  geom_line(stat = 'summary', fun.y = mean)

library(gridExtra)
grid.arrange(p2, p1, p3, ncol = 1)
```

Scatterplot, and also augmented the scatter plot, with conditional summaries, like means. Benefits and the limitations of using correlation, to understand the relationship between two variables. How correlation may effect your decisions, over which variables to include in your final models. 
How to make sense of data through adjusting our visualizations. Not neccessarily trust our interpretation of initial scatter plots like with the seasonal temperature data. How to use jitter and transparency to reduce over plotting. 

##Quiz Summary##
**Omit the top 1% of Price and carat##
```R
# Create a scatterplot of price vs carat
# and omit the top 1% of price and carat
# values.

ggplot(aes(x = carat, y = price), data = diamonds) +
  geom_point(colour = "orange") +
  scale_x_continuous(limits = c(0, quantile(diamonds$carat, 0.99))) +
  scale_y_continuous(limits = c(0, quantile(diamonds$price, 0.99))) +
  labs(title = "Diamond Price vs. Mass", x = "Mass (carats)", y = "Price (USD")
```

[ggplot2 smooth](http://ggplot2.tidyverse.org/reference/geom_smooth.html)

```R
# Subset the data to exclude diamonds with a volume
# greater than or equal to 800. Also, exclude diamonds
# with a volume of 0. Adjust the transparency of the
# points and add a linear model to the plot. (See the
# Instructor Notes or look up the documentation of
# geom_smooth() for more details about smoothers.)

ggplot(diamonds[diamonds$volume > 0 & diamonds$volume < 800,], aes(x = volume, y = price)) +
  geom_point(alpha = 1/100, colour = "orange") +
  geom_smooth(method = "lm", colour = "blue") +
  labs(title = "Price vs. Volume", x = "volume", y = "price(USD)")
```

###Mean Price By Clarity###
**Note**: If you used the ```count()``` function from the plyr package before this exercise, you need to run this command to **unload the plyr package**: ```detach("package:plyr", unload=TRUE)```

The ```plyr``` package will conflict with the ```dplyr``` package when doing this exercise. You will want to complete this exercise in RStudio with **ONLY** the dplyr package loaded.

The [dplyr](https://blog.rstudio.com/2014/01/17/introducing-dplyr/) package.

**Important Notice!** Please note that in newer versions of dplyr (0.3.x+), the syntax ```%.%``` has been deprecated and replaced with ```%>%```. Videos in the course use ```%.%```, which will produce warning messages. If you answer using the chain operator, you should use ```%>%``` instead.

Another warning: Version 0.4.0 of dplyr has a bug when using the median function on the summarize layer, depending on the nature of the data being summarized. You may need to cast the data as a numeric (float) type to get the expected results, e.g. ```median(as.numeric(var))```.

```R
# Use the function dplyr package
# to create a new data frame containing
# info on diamonds by clarity.

# Name the data frame diamondsByClarity

# The data frame should contain the following
# variables in this order.

#       (1) mean_price
#       (2) median_price
#       (3) min_price
#       (4) max_price
#       (5) n

# where n is the number of diamonds in each
# level of clarity.

library(dplyr)

diamondsByClarity <- diamonds %>%
  group_by(clarity) %>%
  summarise(mean_price = mean(price),
            median_price = median(price),
            min_price = min(price),
            max_price = max(price),
           n = n()) %>%
  arrange(clarity)

diamondsByClarity
```
```R
diamondsByClarity <- summarise(group_by(diamonds, clarity),
                               mean_price = mean(price),
                               median_price = median(price),
                               min_price = min(price),
                               max_price = max(price),
                               n = n()
                              )

diamondsByClarity
```

[Save plots](http://ggplot2.tidyverse.org/reference/ggsave.html) using ```ggsave()```.

### inner_join ###
```R
library(dplyr)
# Join GNI data with oil consumption data
black_gold <- inner_join(ocpc, gnipc)
```
###as.factor###
[Convert a column into a factor column.](https://www.rdocumentation.org/packages/h2o/versions/3.10.5.3/topics/as.factor)
```R
black_gold$Year <- as.factor(black_gold$Year)
```

#Explore Many Variables#
**Third Qualitative Variable**
You can include multiple variables to split the data frame when using ```group_by()``` function in the dplyr package.

```new_groupings <- group_by(data, variable1, variable2)```

**OR**
using chained commands...
```R
new_data_frame <- data_frame %>%
  group_by(variable1, variable2) %>%
```
[Repeated use of ```summarise()``` and ```group_by()```:](https://classroom.udacity.com/nanodegrees/nd002/parts/0021345407/modules/316518875375460/lessons/701610057/concepts/8737286370923) The summarize function will automatically remove one level of grouping (the last group it collapsed).

```R
# Write code to create a new data frame,
# called 'pf.fc_by_age_gender', that contains
# information on each age AND gender group.

# The data frame should contain the following variables:

#    mean_friend_count,
#    median_friend_count,
#    n (the number of users in each age and gender grouping)

# Here is an example of the structure of your data frame. Your
# data values will be different. Note that if you are grouping by
# more than one variable, you will probably need to call the
# ungroup() function. 

#   age gender mean_friend_count median_friend_count    n
# 1  13 female          247.2953                 150  207
# 2  13   male          184.2342                  61  265
# 3  14 female          329.1938                 245  834
# 4  14   male          157.1204                  88 1201


library(dplyr)

#chain functions together %>%

pf.fc_by_age_gender <- pf %>%
  filter(!is.na(gender)) %>%
  group_by(age, gender) %>%
  summarise(mean_friend_count = mean(friend_count),
            median_friend_count = median(friend_count),
            n = n()) %>%
  ungroup() %>%
  arrange(age)
  
head(pf.fc_by_age_gender)
```

##Wide and Long Format##
You can restructure the data using the ```tidyr``` package. 
[data Wrangling with R pdf](https://s3.amazonaws.com/udacity-hosted-downloads/ud651/DataWranglingWithR.pdf)

The code to change the data frame from long format to wide (or tidy format) is shown below. I encourage you to read the Data Wrangling pdf and write code using the tidyr package before looking at the solution below. 


```R
install.packages("tidyr")
library(tidyr)

spread(subset(pf.fc_by_age_gender, 
       select = c('gender', 'age', 'median_friend_count')), 
       gender, median_friend_count)
```

I think you will find the tidyr package easier to use than the reshape2 package. Both packages can get the job done.

[An Introduction to reshape2 by Sean Anderson](http://seananderson.ca/2013/10/19/reshape.html)
[Converting Between Long and Wide Format](http://www.cookbook-r.com/Manipulating_data/Converting_data_between_wide_and_long_format/)
[Melt Data Frames](https://www.r-bloggers.com/melt/)

##Reshaping Data##
```R
install.packages('reshape2')
library(reshape2)
```
```R
#dcast is used since we want the result to be a data frame
#if we wanted an array or a matrix we could use a cast
pf.fc_by_age_gender.wide <- dcast(pf.fc_by_age_gender,
                                  age ~ gender,
                                  value.var = 'median_friend_count')
head(pf.fc_by_age_gender.wide)
```
##Ratio Plot##
```R
# Plot the ratio of the female to male median
# friend counts using the data frame
# pf.fc_by_age_gender.wide.

# Think about what geom you should use.
# Add a horizontal line to the plot with
# a y intercept of 1, which will be the
# base line. Look up the documentation
# for geom_hline to do that. Use the parameter
# linetype in geom_hline to make the
# line dashed.

# The linetype parameter can take the values 0-6:
# 0 = blank, 1 = solid, 2 = dashed
# 3 = dotted, 4 = dotdash, 5 = longdash
# 6 = twodash

ggplot(aes(x = age, y = female / male),
       data = pf.fc_by_age_gender.wide) + 
  geom_line() +
  geom_hline(yintercept = 1, alpha = 0.3, linetype = 2)
```
##Third Quantitative Variable##
You can use the ```floor()``` function to **round down** to the nearest integer. You can use the ```ceiling()``` function to **round up** to the nearest integer.

##Cut a Variable##
[The Cut Function](https://www.r-bloggers.com/r-function-of-the-day-cut-2/)
A common mistake is to use ```year_joined``` rather than ```pf$year_joined``` or ```with(pf, year_joined...)```. Remember that you need to access the variable in the data frame.

http://blog.wolfram.com/data/uploads/2012/10/xkcd.png

##Plotting It All Together##
```R
ggplot(aes(x = age, y = friend_count),
       data = subset(pf, !is.na(gender))) +
  geom_line(aes(color = gender), stat = 'summary', fun.y = median)
```
```R
ggplot(aes(x = age, y = friend_count),
       data = subset(pf, !is.na(gender))) +
  geom_line(aes(color = year_joined.bucket), stat = 'summary', fun.y = median)
```

##Plot the Grand Mean##
```R
# Write code to do the following:

# (1) Add another geom_line to code below
# to plot the grand mean of the friend count vs age.

# (2) Exclude any users whose year_joined.bucket is NA.

# (3) Use a different line type for the grand mean.

# As a reminder, the parameter linetype can take the values 0-6:

# 0 = blank, 1 = solid, 2 = dashed
# 3 = dotted, 4 = dotdash, 5 = longdash
# 6 = twodash

ggplot(aes(x = age, y = friend_count),
       data = subset(pf, !is.na(gender))) +
  geom_line(aes(color = year_joined.bucket), stat = 'summary', fun.y = mean) +
#Grand mean:
  geom_line(stat = 'summary', fun.y = mean, linetype = 2)
```

##Friending Rate##
```R
with(subset(pf, tenure >= 1), summary(friend_count / tenure))
```

##Friendships Initiated##
```R
ggplot(aes(x = tenure, y = friendships_initiated / tenure),
       data = subset(pf, pf$tenure >= 1)) +
  geom_line(aes(color = year_joined.bucket), stat = 'summary', fun.y = mean)
```

##Bias Variance Trade off Revisited##
[Understanding the Bias-Variance Tradeoff](http://scott.fortmann-roe.com/docs/BiasVariance.html)
**Note**: The code changing the binning is substituting ```x = tenure``` in the plotting expressions with ```x = 7 * round(tenure / 7)```, etc., binning values by the denominator in the ```round``` function and then transforming back to the natural scale with the constant in front.

```R
ggplot(aes(x = tenure, y = friendships_initiated / tenure),
       data = subset(pf, tenure >= 1)) +
  geom_line(aes(color = year_joined.bucket),
            stat = 'summary',
            fun.y = mean)

ggplot(aes(x = 7 * round(tenure / 7), y = friendships_initiated / tenure),
       data = subset(pf, tenure > 0)) +
  geom_line(aes(color = year_joined.bucket),
            stat = "summary",
            fun.y = mean)

ggplot(aes(x = 30 * round(tenure / 30), y = friendships_initiated / tenure),
       data = subset(pf, tenure > 0)) +
  geom_line(aes(color = year_joined.bucket),
            stat = "summary",
            fun.y = mean)

ggplot(aes(x = 90 * round(tenure / 90), y = friendships_initiated / tenure),
       data = subset(pf, tenure > 0)) +
  geom_line(aes(color = year_joined.bucket),
            stat = "summary",
            fun.y = mean)
```
```R
# Instead of geom_line(), use geom_smooth() to add a smoother to the plot.
# You can use the defaults for geom_smooth() but do color the line
# by year_joined.bucket

ggplot(aes(x =tenure, y = friendships_initiated / tenure),
       data = subset(pf, tenure >= 1)) +
  geom_smooth(aes(color = year_joined.bucket))
```

[The Emotional Highs and Lows of the NFL season](https://www.facebook.com/notes/facebook-data-science/the-emotional-highs-and-lows-of-the-nfl-season/10152033221418859)

##Introducing the Yogurt Dataset##
[Bayesian Statistics and Marketing](http://www.perossi.org/home/bsm-1)

##Number of Purchases##
The transform function takes in a data frame and allows us to add different variables to it by recombining variables that are alreayd within the dara frame.
```R
# Create a new variable called all.purchases,
# which gives the total counts of yogurt for
# each observation or household.

# One way to do this is using the transform
# function. You can look up the function transform
# and run the examples of code at the bottom of the
# documentation to figure out what it does.

# The transform function produces a data frame
# so if you use it then save the result to 'yo'!

# OR you can figure out another way to create the
# variable.

#the transform function takes in a data frame and allows us to add different variables to it by recombining variables that are alreayd within the dara frame.
yo <- transform(yo, all.purchases = strawberry + blueberry + pina.colada + plain + mixed.berry)

summary(yo$all.purchases)

#OR
#yo$all.purchases <- yo$strawberry + yo$blueberry + yo$pina.colada + #yo$plain + yo$mixed.berry
```

##Prices Over Time##
```R
# Create a scatterplot of price vs time.

# This will be an example of a time series plot.

ggplot(aes(x = time, y = price), data = yo) +
  geom_jitter(alpha = 1/4, shape = 21, fill = I('#F79420'))

#the most common prices, seems to be increasing over time, we also see some lower price points scattered about the graph.
```

##Looking at Samples of Households##
**Note**: ```x %in% y``` returns a logical (boolean) vector the same length as x that says whether each entry in x appears in y. That is, for each entry in x, it checks to see whether it is in y. This allows us to subset the data so we get all the purchases occasions for the households in the sample. Then, we create scatterplots of price vs. time and facet by the sample id. 


Use the ```pch``` or ```shape``` parameter to specify the symbol when plotting points. Scroll down to 'Plotting Points' on[ QuickR's Graphical Parameters](http://www.statmethods.net/advgraphs/parameters.html).

```R
#Set the seed for reproducible results
set.seed(4230)
#sampling from levels because those are all of the different households that we have
sample.ids <- sample(levels(yo$id), 16)

sample.ids
```
```
[1] "2107953" "2123463" "2167320" "2127605" "2124750" "2133066"
 [7] "2134676" "2141341" "2107706" "2151829" "2119693" "2122705"
[13] "2115006" "2143271" "2101980" "2101758"
```
```R
ggplot(aes(x = time, y = price),
       data = subset(yo, id %in% sample.ids)) +
  facet_wrap( ~ id) +
  geom_line() +
  geom_point(aes(size = all.purchases), pch = 1)
```
##Many Variables##
Auxiliary variables

##Scatterplot Matrices##
You'll need to run the code ```install.packages('GGally')``` to install the package for creating this particular scatterplot matrix.

If the plot takes a long time to render or if you want to see some of the scatterplot matrix, then only examine a smaller number of variables. You can use the following code or select fewer variables. We recommend including gender (the 6th variable)!

```pf_subset = pf[, c('age', 'dob_year', 'dob_month', 'gender', 'tenure')]```

You can also select a subset using the ```subset()``` function and the "select" argument:

```pf_subset <- subset(pf, select = -c(userid, year_joined, year_joined_bucket))```

The ```-``` sign in the "select" value indicates all but the listed columns.

You may find in your matrix that variable labels are on the outer edges of the scatterplot matrix, rather than on the diagonal. If you want labels in the diagonal, you can set the ```axisLabels = 'internal'``` argument in your ggpairs command.

##Heat Maps##
[Melt data frames in R](https://www.r-bloggers.com/melt/)

##Sumary##
We started with simple extensions to the scatterplot,
and plots of conditional summaries that you worked with in lesson four, such as adding summaries for multiple groups.
Then, we tried some techniques for examining a large number of variables at once, such as scatter-plot matrices and heat maps.
We also learned how to reshape data, moving from broad data with one row per case, to aggregate data with one row per combination of variables, and we moved back and forth between long and wide formats for our data. 

##[Mutate](https://www.rdocumentation.org/packages/dplyr/versions/0.5.0/topics/mutate)##
Add New Variables.
Mutate adds new variables and preserves existing; transmute drops existing variables.
```R
diamonds <- diamonds %>% 
  mutate(volume = x * y *z)
```

#Diamonds & Price Predictions#
##Scatterplot Review##
Use the ```quantile()``` function inside of ```xlim``` and ```ylim``` to omit the top 1% of values for each variable.
```R
# Let's start by examining two variables in the data set.
# The scatterplot is a powerful tool to help you understand
# the relationship between two continuous variables.

# We can quickly see if the relationship is linear or not.
# In this case, we can use a variety of diamond
# characteristics to help us figure out whether
# the price advertised for any given diamond is 
# reasonable or a rip-off.

# Let's consider the price of a diamond and it's carat weight.
# Create a scatterplot of price (y) vs carat weight (x).

# Limit the x-axis and y-axis to omit the top 1% of values.

qplot(data = diamonds, x = carat, y = price,
      xlim = c(0, quantile(diamonds$carat, 0.99)),
      ylim = c(0, quantile(diamonds$price, 0.99))) +
  geom_point(fill = I('#F79420'), color = I('black'), shape = 21)
```
Add a linear trim line to the plot by using the stat smooth function with method equals lm.
```R
ggplot(data = diamonds, aes(x = carat, y = price)) +
  geom_point(color = '#F79420', alpha = 1/4) +
  stat_smooth(method = 'lm') +
  scale_x_continuous(lim = c(0, quantile(diamonds$carat, 0.99))) +
  scale_y_continuous(lim = c(0, quantile(diamonds$price, 0.99)))
```
##ggpairs Function##
The "params" argument to the ```ggpairs``` function are there to change the shape of the plotted points in the plot matrix, to make them easier to see. GGally 1.0 changes the syntax of these plotting parameters to no longer be part of a params argument, and instead can be specified as follows:
```R
ggpairs(diamond_samp,
  lower = list(continuous = wrap("points", shape = I('.'))),
  upper = list(combo = wrap("box", outlier.shape = I('.'))))
```
You can click on the packages tab in RStudio to determine which packages have been installed.

You may receive a message when installing the new packages. If so, click cancel, clear your workspace, and try installing the packages again.

In this video, Solomon works with the ```plyr``` package. We worked with the ```dplyr``` package to manipulate data frames and to create new ones throughout the course. ```dplyr``` is the latest version of ```plyr``` that is specifically for working with data frames.

Similarly, we worked with the ```reshape2``` package, which is the newest version of the ```reshape``` package.

[ggpairs output](https://s3.amazonaws.com/udacity-hosted-downloads/ud651/ggpairs_landscape.pdf) When you duplicate the plot matrix on your local machine, you may want to add a axisLabels = 'internal' argument to your ggpairs function call to have the variable names on the diagonal of the matrix rather than on the outside.

**ggpairs plots each variable against each other variable, pairwise.**

```R
# install these if necessary
install.packages('GGally')  #particular plot 
install.packages('scales')  #for a variety of things
install.packages('memisc')  #summarize the regression
install.packages('lattice') #few other things
install.packages('MASS')    #various functions
install.packages('car')     #recode variables
install.packages('reshape') #reshape and wrangle data
install.packages('dplyr')   #create summaries and transmissions

# load the ggplot graphics package and the others
library(ggplot2)
library(GGally)
library(scales)
library(memisc)

# sample 10,000 diamonds from the data set
set.seed(20022012)
diamond_samp <- diamonds[sample(1:length(diamonds$price), 10000), ]
ggpairs(diamond_samp, params = c(shape = I('.'), outlier.shape = I('.')))
```

##The Demand of Diamonds##
[Log Transformations](https://www.r-statistics.com/2013/05/log-transformations-for-skewed-and-wide-distributions-from-practical-data-science-with-r/)

Often the distribution of any monetary variable like dollars will be highly skewed and vary over orders of magnitude.

```R
# Create two histograms of the price variable
# and place them side by side on one output image.

# We’ve put some code below to get you started.

# The first plot should be a histogram of price
# and the second plot should transform
# the price variable using log10.

# Set appropriate bin widths for each plot.
# ggtitle() will add a title to each histogram.
plot1 <- qplot(data = diamonds, x = price, binwidth = 100, fill = I('#0990D9')) + 
  ggtitle('Price')

plot2 <- qplot(data = diamonds, x = price, binwidth = 0.01, fill = I('#F79420')) +
  ggtitle('Price (log10)') +
  scale_x_log10()

library(gridExtra)
library(grid)
grid.arrange(plot1, plot2, ncol = 2)
```

##Scatterplot Transformation##
[Basic Structure of a Function](https://www.youtube.com/watch?v=Z1wB1rHAYzQ&list=PLOU2XLYxmsIK9qQfztXeybpHvru-TrqAP)

```R
qplot(carat, price, data = diamonds) +
  scale_y_continuous(trans = log10_trans()) +
  ggtitle('Price (log10) by Carat')
```
Create a new function to transform the carat variable.
```R
#Create a new function to transform the carat variable
cuberoot_trans = function() trans_new('cuberoot', transform = function(x) x^(1/3),
                                      inverse = function(x) x^3)
```
```R
#Use the cuberoot_trans function
ggplot(aes(carat, price), data = diamonds) + 
  geom_point() + 
  scale_x_continuous(trans = cuberoot_trans(), limits = c(0.2, 3),
                     breaks = c(0.2, 0.5, 1, 2, 3)) + 
  scale_y_continuous(trans = log10_trans(), limits = c(350, 15000),
                     breaks = c(350, 1000, 5000, 10000, 15000)) +
  ggtitle('Price (log10) by Cube-Root of Carat')
```

##Overplotting Revisited##

```{r Sort and Head Tables}
head(sort(table(diamonds$carat), decreasing = T))
head(sort(table(diamonds$price), decreasing = T))
```
```{r Overplotting Revisited}
# Add a layer to adjust the features of the
# scatterplot. Set the transparency to one half,
# the size to three-fourths, and jitter the points.

ggplot(aes(carat, price), data = diamonds) + 
  geom_point(alpha = 0.5, size = 0.75, position = 'jitter') + 
  scale_x_continuous(trans = cuberoot_trans(), limits = c(0.2, 3),
                     breaks = c(0.2, 0.5, 1, 2, 3)) + 
  scale_y_continuous(trans = log10_trans(), limits = c(350, 15000),
                     breaks = c(350, 1000, 5000, 10000, 15000)) +
  ggtitle('Price (log10) by Cube-Root of Carat')
```

##Price vs. Carat and Clarity##
ggplot2: [scale_colour_brewer](http://ggplot2.tidyverse.org/reference/scale_brewer.html)
ggplot2: [Color Brewer Palettes and Safe Colors](http://www.cookbook-r.com/Graphs/Colors_(ggplot2/#palettes-color-brewer)

Run the following code in RStudio to install and load the RColorBrewer package.
```R
install.packages('RColorBrewer', dependencies = TRUE)
library(RColorBrewer)
```
```{r Price vs. Carat and Clarity}
# Adjust the code below to color the points by clarity.

# A layer called scale_color_brewer() has 
# been added to adjust the legend and
# provide custom colors.
library(scales)

ggplot(aes(x = carat, y = price, colour = clarity), data = diamonds) + 
  geom_point(alpha = 0.5, size = 1, position = 'jitter') +
  scale_color_brewer(type = 'div',
    guide = guide_legend(title = 'Clarity', reverse = T,
    override.aes = list(alpha = 1, size = 2))) +  
  scale_x_continuous(trans = cuberoot_trans(), limits = c(0.2, 3),
    breaks = c(0.2, 0.5, 1, 2, 3)) + 
  scale_y_continuous(trans = log10_trans(), limits = c(350, 15000),
    breaks = c(350, 1000, 5000, 10000, 15000)) +
  ggtitle('Price (log10) by Cube-Root of Carat and Clarity')
```
##Price vs. Carat and Cut##
```{r Price vs. Carat and Cut}
library(scales)

ggplot(aes(x = carat, y = price, color = cut), data = diamonds) + 
  geom_point(alpha = 0.5, size = 1, position = 'jitter') +
  scale_color_brewer(type = 'div',
                     guide = guide_legend(title = 'cut', reverse = T,
                                          override.aes = list(alpha = 1, size = 2))) +  
  scale_x_continuous(trans = cuberoot_trans(), limits = c(0.2, 3),
                     breaks = c(0.2, 0.5, 1, 2, 3)) + 
  scale_y_continuous(trans = log10_trans(), limits = c(350, 15000),
                     breaks = c(350, 1000, 5000, 10000, 15000)) +
  ggtitle('Price (log10) by Cube-Root of Carat and Cut')
```

##Price vs. Carat and Color##
```{r Price vs. Carat and Color}
ggplot(aes(x = carat, y = price, color = color), data = diamonds) + 
  geom_point(alpha = 0.5, size = 1, position = 'jitter') +
  scale_color_brewer(type = 'div',
                     guide = guide_legend(title = 'Color', reverse = FALSE,
                                          override.aes = list(alpha = 1, size = 2))) +  
  scale_x_continuous(trans = cuberoot_trans(), limits = c(0.2, 3),
                     breaks = c(0.2, 0.5, 1, 2, 3)) + 
  scale_y_continuous(trans = log10_trans(), limits = c(350, 15000),
                     breaks = c(350, 1000, 5000, 10000, 15000)) +
  ggtitle('Price (log10) by Cube-Root of Carat and Color')
```

##Linear Models in R##
Predict! Use the lm() function.
**lm(y ~ x)**
y: outcome variable
x:explanatory variable

##Building the Linear Model##
[Linear Models and Operatior in R](http://data.princeton.edu/R/linearModels.html)

If you are running this code on your local computer, you may need to modify the last line to state:
```R
mtable(m1, m2, m3, m4, m5, sdigits = 3)
```
This will ensure that the output at the end of the table shows three significant digits like shown in the video.

```{r Building the Linear Model}
library(memisc)

m1 <- lm(I(log(price)) ~ I(carat^(1/3)), data = diamonds)
#I stands for as is
#This is instead of instrucing R to interpret these symbols as part of the formula to construct the design matrix for the regression.
m2 <- update(m1, ~ . + carat)
m3 <- update(m2, ~ . + cut)
m4 <- update(m3, ~ . + color)
m5 <- update(m4, ~ . + clarity)
mtable(m1, m2, m3, m4, m5, sdigits = 3)
```
##Model Problems##
[Interpreting Regression Coefficients in R on R Bloggers](https://www.r-bloggers.com/interpreting-regression-coefficient-in-r/?utm_source=feedburner&utm_medium=email&utm_campaign=Feed%3A+RBloggers+%28R+bloggers%29)
[Interpreting Regression Coefficients on the Analysis Factor blog](http://www.theanalysisfactor.com/interpreting-regression-coefficients/)
[Fitting and Interpreting Linear Models by ŷhat](http://blog.yhat.com/posts/r-lm-summary.html)
[Another Explanation of Factor Coefficients in Linear Models on Stats StackExchange](https://stats.stackexchange.com/questions/24242/how-to-apply-coefficient-term-for-factors-and-interactive-terms-in-a-linear-equa/24256#24256)

##A Bigger, Better Data Set##
```{r}
#install bitops and RCurl
install.packages('bitops')
install.packages('RCurl')
library('bitops')
library('RCurl')
```
```{r A Bigger, Better Data Set}
#diamondsurl = getBinaryURL("https://raw.github.com/solomonm/diamonds-data/master/BigDiamonds.Rda")
#load(rawConnection(diamondsurl))

load("C:/Files/Udacity/Data-Analysis/Notes/Exploratory Data Analysis (R)/R Basics/eda-course-materials/lesson6/BigDiamonds.rda")
```
```{r Building a Model Using the Big Diamonds Data Set}
#We will only use GIA certified diamonds in this modle, and only look at diamonds under $10,000 because these are the type of diamonds sold at most retailers and hence the kind we care most about.
#By trimming the most expensive diamonds from the data set, our model will also be less likely to be thrown off by outliers and the higher variants at the high-end of price and carat.

# Your task is to build five linear models like Solomon
# did for the diamonds data set only this
# time you'll use a sample of diamonds from the
# diamondsbig data set.

# Be sure to make use of the same variables
# (logprice, carat, etc.) and model
# names (m1, m2, m3, m4, m5).

# To get the diamondsbig data into RStudio
# on your machine, copy, paste, and run the
# code in the Instructor Notes. There's
# 598,024 diamonds in this data set!

# Since the data set is so large,
# you are going to use a sample of the
# data set to compute the models. You can use
# the entire data set on your machine which
# will produce slightly different coefficients
# and statistics for the models.

# sample 10,000 diamonds from the data set
set.seed(20022012)
diamondbig_samp <- diamondsbig[sample(1:length(diamonds$price), 10000), ]
```
```{r}
#diamondbig_samp$logprice = log(diamondbig_samp$price)
m1 <- lm(I(log(price)) ~ I(carat^(1/3)),
         data = diamondbig_samp[diamondbig_samp$price < 10000 &
                                  diamondbig_samp$cert == "GIA",])
m2 <- update(m1, ~ . + carat)
m3 <- update(m2, ~ . + cut)
m4 <- update(m3, ~ . + color)
m5 <- update(m4, ~ . + clarity)
mtable(m1, m2, m3, m4, m5, sdigits = 3)
```

##Predictions##
[Confidence Intervals](https://en.wikipedia.org/wiki/Confidence_interval)
The prediction interval here may be slightly conservative, as the model errors are heteroskedastic over carat (and hence price) even after our log and cube-root transformations.

See the output of the following code.
```R
dat = data.frame(m4$model, m4$residuals)

with(dat, sd(m4.residuals))

with(subset(dat, carat > .9 & carat < 1.1), sd(m4.residuals))

dat$resid <- as.numeric(dat$m4.residuals)
ggplot(aes(y = resid, x = round(carat, 2)), data = dat) +
  geom_line(stat = "summary", fun.y = sd)
```
RUN Console
```
> exp(modelEstimate)
```
 fit      lwr      upr
1 430.2906 307.6785 601.7645

The results yield an expected value for price given the characteristics of our diamond, and the upper and lower bounds of a 95% confidence level. 

[How to analyze your Facebook friends network with R](http://blog.revolutionanalytics.com/2013/11/how-to-analyze-you-facebook-friends-network-with-r.html)