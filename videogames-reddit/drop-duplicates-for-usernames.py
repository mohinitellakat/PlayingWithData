# -*- coding: utf-8 -*-
"""
Created on Fri Sep 28 15:30:21 2018

@author: mt34546

I want this script to output a list of unique authors in my games subreddit data
"""

import pandas as pd

df = pd.read_csv("D:/Games/reddit-comments-metadata-aggregated.csv")

df2 = df['author']

df2 = df2.drop_duplicates()

df2.to_csv("D:/Games/reddit-games-unique-authors.csv", index = False)

