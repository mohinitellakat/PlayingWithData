# -*- coding: utf-8 -*-
"""
Created on Fri Sep 28 15:30:21 2018

@author: mt34546

I want this script to output a list of unique authors in my games subreddit data
"""

import pandas as pd

df = pd.read_csv("G:/My Drive/GradSchoolStuff-UT/Code/videogames-reddit/splitcsv-test/fornite-ExtractedRedditData-Comments-TextData.csv")

df2 = df['author']

df2 = df2.drop_duplicates()

df2.to_csv("D:/Games/fortnite-unique-authors.csv", index = False)

