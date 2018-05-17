# -*- coding: utf-8 -*-
"""
Created on Tue Sep 12 20:10:40 2017

@author: mt34546
"""

import pandas as pd

media_type_list = []

coded_file_file_path = raw_input('Enter your coded file filepath here:') #C:\Users\mt34546\Documents\UTStuff\PennebakerLabStuff\Click Data\Fall2015-LinkMappings.csv
raw_data_file_path = raw_input('Enter your raw file filepath here:') #C:\Users\mt34546\Documents\UTStuff\PennebakerLabStuff\Click Data\Starting Data\page_stats_Fall2015.csv


df = pd.read_csv(coded_file_file_path) 
df2 = pd.read_csv(raw_data_file_path)

df3 = pd.merge(left=df2,right=df, how='outer', on='url')

df3['media_type'] = df3.media_type.fillna(value="missing")

df3.to_csv("click-data-starting-Fall2015-addedmediatype.csv")
