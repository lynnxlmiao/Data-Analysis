
# Create a Tableau Story : Titanic Data Visualization #
## Summary ##
This project is an explanatory data visualization story from Titanic Data, which contains demographics and passenger information from a subset of the passengers and crew on board the Titanic. It shows the information between those passengers who survived and those who died based on age in years, classed, and gender. It reveals that female in first class had higher chance of survival and male in third class had lowest chance of survival. In general, females, children and the first class passangers has higher chance of survival.

## Design ##
The data is downloaded from [Data Set Options](https://docs.google.com/document/d/1w7KhqotVi5eoKE3I_AZHbsxdr-NmcWsLTIiZrpxWx4w/pub?embedded=true). And here I applied techniques from Exploratory Data Analysis with Tableau to make the visualization. Multiple chart types are used in this Tableau story, such as bar chart, bubble chart, etc. And markers, color and filters are used to visualie the data.

I chose bar chart to represent the passengers accross gender because bar chart provides great comparison view between entities. Here the bars are filtered by passengers survival status by color so that it's clear to see whether female passengers had higher survival chance compared with male passengers out of the total passengers on board. From this chart we can see that female passengers has higher survival rate. And age are set as filter here to see from different age groups.

For the survival by age chart, here we want to see the different survival chance by age. Since the number of age is ranging from 0 to 74, so a histogram is good to show this. I plot the histogram using bars in order to represent my visualization in a more appealing manner. Here the bars are filtered by survival status by color also so it's easier to see the different behavior among different age group of survival rate. And the class is set as filter here to see whether the survival chance by age behaves differently for different age group. 

Since there are four types of class for passengers, it's better to visualize from bar chart for survival rate by class. This chart shows that the first class passengers has higher chance of survival. And I set age as filter here to see in different age groups.

And I chose bubble chart to show which gender has the most number and which has highest chances of survival, belong to which class as well. Because bubble chart can bubble up the most prominent group with the largest size. I also set class and gender as filters so viwers are able to see from different and special groups.

** The first version: ** https://public.tableau.com/profile/lynn.miao#!/vizhome/Titanic_Story/Story?publish=yes

## Feedback ##
I have shared my visualization with one person, and here are the feedbacks.
- What do you notice in the visualization?

  **A:** The first dashboard is a bit confusing for me. I think adding a table of relative numbers will be a useful aid giving better first impression of the data. Besides, indicating the accurate numbers for bar charts seems better for me.
  
  
- What questions do you have about the data?

  **A:** I believe you have done necessary data preprocessing, nice work.
  
  
- What relationships do you notice?

  **A:** Females of first class would have the highest chance to survive.


- What do you think is the main takeaway from this visualization?

  **A:** Neat style.


- Is there something you don’t understand in the graphic?

  **A:** Although you did a decent job for the visualization, providing some necessary descriptions of each dashboard will make it much easier for readers to get what you have revealed.

## Post  Feedback Design ##
Thanks for the feedback and base on these, I have improved my visualization as below:

Following his feedback "The first dashboard is a bit confusing for me..." I have added a table shows the number of survival by class and gender, and also indicated the number of the bar charts so it is more accurate to compare the differences.

And also "...providing some necessary descriptions of each dashboard...", I added the decriptions for each dashboard so that to make a story instead of making charts only. 

** Final version: **https://public.tableau.com/profile/lynn.miao#!/vizhome/Titanic_Story/Story?publish=yes
