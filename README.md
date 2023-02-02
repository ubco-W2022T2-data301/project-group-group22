# Group 22 - {How performance changes for the top NHL players}


## Milestones

Details for Milestone are available on Canvas (left sidebar, Course Project).

## Describe your topic/interest in about 150-200 words

Ricky: I am interested in this dataset because I am a fan of hockey and like to see the statistical aspects of players' performances. I would like to find if there is a corelation between drops and increases in certain statistics for consecutive years for the top NHL players in points. Specific examples of research questions I would like to discover answers to are: Does an increase/decrease in time on ice per game relate to an increase in certain stats like overall points in the season? Do the top players that have a decrease in their offensive stats in a succesive season make up for it with an increase in their defensive stats? How many of the top 250 players in points from the 2017-2018 season managed to make the top 350 players in points for the 2018-2019 season? How many of those players didn't make the top 350 just because they retired?

Renat: I find the topic of analysing NHL player performance of personal interest, as I am a big fan of hockey. I used to play thee sport as a kid, and watch NHL games. The analysis of players' statistical data in one year and evaluation the correlation between their performance of the following year seems like it would bring further understanding of hockey, and I am excited to see what the results will show. For the data set, we used a website that provides royalty-free NHL statistics under Open License. After performing some edits on the data by using a Python code which removes colums in the statistics which are not of interest, as well as players' data entries which are not in both the 2017 and 2018 data sets, we got usable data of player's performance in 2017, and the following season. I am interested to see how each performance statstic of 2017 affects the player's goals scored and the ranking in 2018, and whether one has a larger effect than the others. 

Ryan:


## Describe your dataset in about 150-200 words

The project is based on a data set containing the statistics for top 225 NHL players in 2017-18 season and their statistics for the following 2018-19 season. The project aims to look at the relationship between the data such as time on ice, assists, etc. of the 17-18 season, and correlate them to the number of goals scored in the following season (or their ranking in the following season).
The data for the project was obtained from https://www.quanthockey.com/. Data is under Open License, royalty-free. 

The methodology for obtaining the data was to:
1. Firstly, retrieve the statistics for top 250 players of the 2017-18 players based on the number of points. This data set is called ‘NHL2017’. 
2. Obtain the statistics for the top 350 players in the following season, as the majority of the top 250 players will still be in the top 350 next year. This data set is called ‘NHL2018’. 
3. Remove the player entries that are not in both data sets and form two new data sets ‘Top250_2017’ and ‘Top250_2018’. This way we obtain two data sets with statistics of players’ performance for two consecutive years. 
4. Drop the columns in both datasets that are not of interest.


## Team Members

- Ricky: I grew up playing high level hockey and was always interested in the numbers aspect of the game to really paint a picture of players in my head so this data analysis seems very exciting to me!
- Renat: I am interessted to learn the correlation between players' stats and their perofrmance in following year. 
- Ryan: one sentence about you!

## Images

{You should use this area to add a screenshot of an interesting plot, or of your dashboard}

*Ryan*

<img src ="images/test.png" width="100px">

## References

https://www.quanthockey.com



