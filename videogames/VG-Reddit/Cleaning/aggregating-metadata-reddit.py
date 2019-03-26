# -*- coding: utf-8 -*-
"""
Created on Fri Sep 21 12:07:53 2018

@author: mt34546

##Things I want this program to do:
#1. Just look at the author, subreddit, ups, downs, and controversy
#2. Groupby author and subreddit, and sum the other 3 values. 
#3. Don't look at or output the other values from the original dataset into the final one. 

"""

import pandas as pd
import csv

def parse_int(s):
	"""
	Attempts to parse an integer from the incoming string.
	If the cast to an int fails, will return 0.
	"""
	try:
		i = int(s)
	except ValueError:
		i = 0
	return i

filename = "D:/Games/2018-04-20 - Extracted Reddit Data - Comments - MetaData.csv"

minified_rows = []

with open(filename, encoding="utf-8") as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:

        author = row['author']
        subreddit = row['subreddit']
        ups = parse_int(row['ups'])
        downs = parse_int(row['downs'])
        controversiality = parse_int(row['controversiality'])
        
        minified_rows.append((author, subreddit, ups, downs, controversiality))
      
df = pd.DataFrame(minified_rows)
column_names = ['author', 'subreddit', 'ups', 'downs', 'controversiality']
df = df.rename(lambda x: column_names[x], axis='columns')

df2 = df.groupby(['author','subreddit']).sum()

df2.to_csv("D:/Games/reddit-comments-metadata-aggregated.csv")
