# Final Report Group 22

## Introduction

Our project has been a data analysis on the top scoring players of the 2017 and 2018 NHL seasons. We looked at all the statistics of the top 250 players in points from the 2017 NHL season, and the top 300 players in points from the 2018 NHL season. We kept those players who were in the top 250 from 2017 as well as the top 300 from 2018 and that left us with 225 players to work with for our data set. Due to some of us having a background in hockey, this was an amusing data set for us to have formed and analyzing it made it feel like a lot less work when we had some sort of interest in the topic. The project was simply to see whether there were correlations between certain statistics and others or between succesive NHL seasons for the league's best players.

---

## Exploratory Data Analysis

![EDA](images/EDA_of_stats.png)

From our exploratory data analysis, it can be seen that between both years for the top 225 NHL players that remained in the data set, the average points a player had was 53 in 76 games played. That is not even a point per game. What is very interesting about that is how far spread the points are from the minimum to the maximum of those 225 players in the two seasons played. The lowest amount of points any player had that made that top 225 between the two years was 23 points, less than half of the average. However, the highest anybody had was 128 points! Almost 2.5 times the mean! This speaks to the large skill gap even amongst the top players in the most talented hockey league in the world.

We also wanted to explore the relationship between the goals scored in each season and time on ice. We created a facet plot that showed the relationship in both the 2017 season and 2018 season shown below. From this figure we can conclude that there is a negative or no correlation between the number of goals a player scores, and the time their given/spend on the ice.

![EDA Goals vs TOI](images/EDA_Goals_Scored_vs_TOI.png)

---

## **Ricky Doucette**

### Does an increase in time on ice per game for a succesive season significantly increase an NHL player's overall statistics in that following season?

![All Stats vs TOI](images/all_stats_vs_toi.png)

For all the players who had more TOI in 2018 compared to 2017, this first image shows the difference in some of their most important offensive and defensive statistics between seasons compared to the increase in TOI they received in 2018. From the looks of it, the increase in TOI had no impact on their defensive performance statistically. An increase in TOI does seem to have somewhat of a positively linear trend however with their offensive statistics. Most noticebly, players tend to produce more P/GP as the change in their TOI increases between seasons.

![Points Per Game Played vs TOI](images/P_GP_vs_TOI.png)

As shown below, overall more players had an increase in P/GP rather than a decrease when their TOI was increased in a successive season

![Points Per Game Played vs TOI](images/P_GP_With_More_TOI.png)

From this analysis, we can conclude that an increase in a players average time on ice per game in a following season does not effect their defensive statistics, but it does effect their offensive statistics. Primarily their points per game played sees an increase when they receive more TOI.

---

## **Renat Rezyapov**

### **RQ: What performance statistics show significant correlations? What is the correlation between TOI & shots and goals, assists, and points? **

In order to, a structured data analysis approach was adopted as followed:

Firstly, I constructed a merged dataframe, which contained relevant parameters for both seasons. Next, I investigrated the relationships between different parameters through EDA and by using statistical .corr() and .describe() functions. I also tried to establish whether there are possible significant correlations between the parameters. After completing the EDA, it was clear that the most intersting parameters to look at would be the relationshps between Time on Ice in 2017 and goals, points, and assists in 2018.

![Time on Ice 2017 vs. Goals, Points, and Assists 2018](images/renat_plot1.png)

I thought it would also be intersting to investigate whether any correlation can be established between shots taken in 2017 and points, goals, and assists in the consecutive season. In order to answer those questions, I plotted said parameters against each other with a trend line and investigated the graphs for possible correlations between them.

![Shots 2017 vs. Goals, Points, and Assists 2018](images/renat_plot2.png)



---

## **Ryan Tschritter**

**RQ3: Does a players positive offensive performance in the previous season lead to more penalty time / body checks in the next season? Do they develop a ego?**

In this question I set out to explore if a player develops a ego or becomes more aggressive when they perform better. Taking the offensive data from 2017 and comparing it to the penalty minutes and the number of body checks in the next year, we can determine if players become more aggressive when they get more experience. This analysis used the same normalized offensive data that was used in question 2.

![Regression vs Time on Ice](images/Ryan_RQ3_Regression.png)

From the two charts above we can determine that there is little to no correlation between players aggression in the next year. This even goes to show that a player may become less aggressive the better they perform on the ice. However the spread on the linear regression is significant and I did not calculate the p-values for the regression lines.

---

## Summary

From our research questions and data analyses we have been able to show the correlation between various parameters of NHL statistics. The key findings include the fact that the average points scored by a player in our dataset was 53 in 76 games, highlighting a significant skill gap between the highest and lowest performing players. The skill gap was also evident in the difference between the maximum (128 points) and minimum (23 points) scores among the top 225 players. 
Surprisingly, the research showed no significant correlation between the number of goals a player scored and their time on ice, as evident in the compound plot analysis. Moreover, an increase in time on ice per game for a successive season did not significantly impact a player's defensive performance, but had a positive effect on their offensive statistics, particularly points per game played.
Lastly, we found out that a player's positive offensive performance in the previous season did not lead to more penalty time or body checks in the next season, indicating that there is no strong relationship between a player's performance and their level of aggression.
Overall, the research provided valuable insights into the correlations between various performance statistics in the NHL and their impact on players' overall performance.

