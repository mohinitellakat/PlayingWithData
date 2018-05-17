# -*- coding: utf-8 -*-
"""
Created on Mon Sep 12 14:58:11 2016

@author: Mohini
"""

import pandas as pd

file_path1 = raw_input('Enter filepath1 here:')
file_path2 = raw_input('Enter filepath2 here:')

df1 = pd.read_csv(file_path1)
df2 = pd.read_csv(file_path2)

merged_left = pd.merge(left=df1,right=df2, how='left', left_on=['eid','Benchmark Number'], right_on=['eid','Benchmark Number'])

merged_left.to_csv('click-data-full-Fall2015.csv')