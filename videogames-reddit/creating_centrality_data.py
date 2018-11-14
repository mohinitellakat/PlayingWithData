# -*- coding: utf-8 -*-
"""
Created on Tue Oct 23 15:58:58 2018

@author: mt34546
"""

import pandas as pd
import csv

#df = pd.read_csv("D:/Games/Reddit-Comments-GameNetwork/2018-10-02 - Extracted Reddit Data - Comments - MetaData.csv")
#Put the filepath to the data here
filename = "D:/Games/Reddit-Comments-GameNetwork/2018-10-02 - Extracted Reddit Data - Comments - MetaData.csv"

#initialize an empty dictionary
centrality_dict = dict()

print ("Created empty dictionary")

#Create a dictionary from the original file with key = (author, subreddit) and value = # of posts the author has for a specific subreddit
with open(filename, encoding="utf-8") as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        author = row['author']
        subreddit = row['subreddit']
        
        key_val = (author, subreddit)
        
        if key_val in centrality_dict:
            centrality_dict[key_val] += 1
        else:
            centrality_dict[key_val] = 1

print ("Finished Creating Dictionary!")

#formatting the output into a dataframe
df = pd.DataFrame.from_dict(centrality_dict, orient='index')
df=df.reset_index()

print("Finished resetting index")

df.columns = ['index','value']
df[['author', 'subreddit']] = df['index'].apply(pd.Series)

df2 = df[['author','subreddit','value']]

#Reorienting the data so that the columns are the subreddit names and each row is a different author
df2 = pd.pivot_table(df2, index = 'author', columns=['subreddit'])
df2.columns = df2.columns.droplevel(0)
df2.columns.name = None
df2.rename_axis(None, axis=1).reset_index()

#Gets the total number of posts per author and puts it into the "sum_posts" variable
df2["sum_posts"] = df2.sum(axis=1)

#Divides each subreddit count by the sum posts to get the percentage of posts a person has for a particular subreddit
df3 = df2.loc[:,].div(df2["sum_posts"], axis=0)

#Write to a csv
df3.to_csv("D:/Games/reddit-games-numposts-table.csv")
