# -*- coding: utf-8 -*-
"""
Created on Tue Jan 29 10:06:06 2019

@author: Mohini Tellakat
What this program does: 
1. Takes a reddit output file
2. Aggregates the text data (body) based on author and subreddit
3. Outputs the data into a CSV
"""

import pandas as pd

games_comments = pd.read_csv("G:\\My Drive\\GradSchoolStuff(UT)\\Research-Data\\Gaming Data\\game_test_data.csv")

df = games_comments[['author','subreddit', 'body']]

df = df.groupby(['author','subreddit'])['body'].apply(' '.join)

df.to_csv("G:\\My Drive\\GradSchoolStuff(UT)\\Research-Data\\Gaming Data\\game_test_outputagg_data.csv")