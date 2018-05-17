# -*- coding: utf-8 -*-
"""
Created on Thu Oct 13 10:15:10 2016

@author: mt34546

Get important data columns 
"""

import pandas as pd

file_path = raw_input('Enter your filepath here:')

df1 = pd.read_csv(file_path)

df2 = df1[['eid', 'Date', 'Benchmark Number', 'Grade', 'Click Hour 0.0', 'Click Hour 1.0', 'Click Hour 2.0', 'Click Hour 3.0', 'Click Hour 4.0', 'Click Hour 5.0', 'Click Hour 6.0', 'Click Hour 7.0', 'Click Hour 8.0', 'Click Hour 9.0', 'Click Hour 10.0', 'Click Hour 11.0',  'Click Hour 12.0', 'Click Hour 13.0', 'Click Hour 14.0', 'Click Hour 15.0', 'Click Hour 16.0', 'Click Hour 17.0', 'Click Hour 18.0', 'Click Hour 19.0', 'Click Hour 20.0', 'Click Hour 21.0', 'Click Hour 22.0', 'Click Hour 23.0' ]]

df2.to_csv('click_data_Spring2016_subset1.csv' , index=False)

