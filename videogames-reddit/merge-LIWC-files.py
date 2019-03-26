# -*- coding: utf-8 -*-
"""
Created on Sun Nov 25 09:08:02 2018

@author: mt34546
"""

import os
import pandas as pd

os.chdir('D:/Games/20180423_Game_Comments/LIWC')

dfs = []
for f in os.listdir(os.getcwd()):
    if f.endswith('csv'):
        df = pd.read_csv(f)
        print(f)
        df['subreddit'] = f
        dfs.append(df)
        


#dfs = [pd.read_csv(f)
#        for f in os.listdir(os.getcwd()) if f.endswith('csv')]
#
#dfs = [print(df.name)
#        for df in dfs]

finaldf = pd.concat(dfs)

finaldf.to_csv("C:/Users/mt34546/Documents/UTStuff/merged-LIWCiePy-64Games.csv")
