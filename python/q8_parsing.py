#The football.csv file contains the results from the English Premier League. 
# The columns labeled ‘Goals’ and ‘Goals Allowed’ contain the total number of 
# goals scored for and against each team in that season (so Arsenal scored 79 goals 
# against opponents, and had 36 goals scored against them). Write a program to read the file, 
# then print the name of the team with the smallest difference in ‘for’ and ‘against’ goals.

# The below skeleton is optional.  You can use it or you can write the script with an approach of your choice.


import pandas as pd

 def read_data(path):
  	f=pd.read_csv(path)
  	return f

 def parsed_data(self):
  	return abs(self['Goals']-self['Goals Allowed'])

 def get_min_score_difference(parsed_data):
    return min(parsed_data)

 def get_team(self, value, parsed_data):
    f=pd.DataFrame({'difference':abs(self['Goals']-self['Goals Allowed']),'Team':self['Team']})
    return f[f['difference']==value]['Team']

r=read_data('/Users/ruichang/ds/metis/prework/dsp/python/football.csv')
p=parsed_data(r)
m=get_min_score_difference(p)
get_team(r,m)
