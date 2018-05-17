# -*- coding: utf-8 -*-
"""
Created on Tue Oct 25 13:07:07 2016

@author: mt34546
"""

import pandas as pd

avg_0_list = []
avg_1_list = []
avg_2_list = []
avg_3_list = []
avg_4_list = []
avg_5_list = []
avg_6_list = []
avg_7_list = []
avg_8_list = []
avg_9_list = []
avg_10_list = []
avg_11_list = []
avg_12_list = []
avg_13_list = []
avg_14_list = []
avg_15_list = []
avg_16_list = []
avg_17_list = []
avg_18_list = []
avg_19_list = []
avg_20_list = []
avg_21_list = []
avg_22_list = []
avg_23_list = []

file_path = raw_input('Enter your filepath here:')

df = pd.read_csv(file_path)   

col_list = list(df)
col_list.remove('eid')
col_list.remove('Benchmark Number')
col_list.remove('Grade')

df['Sum_Col_List'] = df[col_list].sum(axis=1)
for idx, sum_col in enumerate(df['Sum_Col_List']):
    numerator_0 = df['Click Hour 0.0'][idx]
    numerator_1 = df['Click Hour 1.0'][idx]
    numerator_2 = df['Click Hour 2.0'][idx]
    numerator_3 = df['Click Hour 3.0'][idx]
    numerator_4 = df['Click Hour 4.0'][idx]
    numerator_5 = df['Click Hour 5.0'][idx]
    numerator_6 = df['Click Hour 6.0'][idx]
    numerator_7 = df['Click Hour 7.0'][idx]
    numerator_8 = df['Click Hour 8.0'][idx]
    numerator_9 = df['Click Hour 9.0'][idx]
    numerator_10 = df['Click Hour 10.0'][idx]
    numerator_11 = df['Click Hour 11.0'][idx]
    numerator_12 = df['Click Hour 12.0'][idx]
    numerator_13 = df['Click Hour 13.0'][idx]
    numerator_14 = df['Click Hour 14.0'][idx]
    numerator_15 = df['Click Hour 15.0'][idx]
    numerator_16 = df['Click Hour 16.0'][idx]
    numerator_17 = df['Click Hour 17.0'][idx]
    numerator_18 = df['Click Hour 18.0'][idx]
    numerator_19 = df['Click Hour 19.0'][idx]
    numerator_20 = df['Click Hour 20.0'][idx]
    numerator_21 = df['Click Hour 21.0'][idx]
    numerator_22 = df['Click Hour 22.0'][idx]
    numerator_23 = df['Click Hour 23.0'][idx]
    
    if sum_col != 0:
        avg_0 = float(numerator_0)/sum_col
        avg_1 = float(numerator_1)/sum_col
        avg_2 = float(numerator_2)/sum_col
        avg_3 = float(numerator_3)/sum_col
        avg_4 = float(numerator_4)/sum_col
        avg_5 = float(numerator_5)/sum_col
        avg_6 = float(numerator_6)/sum_col
        avg_7 = float(numerator_7)/sum_col
        avg_8 = float(numerator_8)/sum_col
        avg_9 = float(numerator_9)/sum_col
        avg_10 = float(numerator_10)/sum_col
        avg_11 = float(numerator_11)/sum_col
        avg_12 = float(numerator_12)/sum_col
        avg_13 = float(numerator_13)/sum_col
        avg_14 = float(numerator_14)/sum_col
        avg_15 = float(numerator_15)/sum_col
        avg_16 = float(numerator_16)/sum_col
        avg_17 = float(numerator_17)/sum_col
        avg_18 = float(numerator_18)/sum_col
        avg_19 = float(numerator_19)/sum_col
        avg_20 = float(numerator_20)/sum_col
        avg_21 = float(numerator_21)/sum_col
        avg_22 = float(numerator_22)/sum_col
        avg_23 = float(numerator_23)/sum_col
        
        avg_0_list.append(avg_0)
        avg_1_list.append(avg_1)
        avg_2_list.append(avg_2)
        avg_3_list.append(avg_3)
        avg_4_list.append(avg_4)
        avg_5_list.append(avg_5)
        avg_6_list.append(avg_6)
        avg_7_list.append(avg_7)
        avg_8_list.append(avg_8)
        avg_9_list.append(avg_9)
        avg_10_list.append(avg_10)
        avg_11_list.append(avg_11)
        avg_12_list.append(avg_12)
        avg_13_list.append(avg_13)
        avg_14_list.append(avg_14)
        avg_15_list.append(avg_15)
        avg_16_list.append(avg_16)
        avg_17_list.append(avg_17)
        avg_18_list.append(avg_18)
        avg_19_list.append(avg_19)
        avg_20_list.append(avg_20)
        avg_21_list.append(avg_21)
        avg_22_list.append(avg_22)
        avg_23_list.append(avg_23)
    else:
        avg_0_list.append(0)
        avg_1_list.append(0)
        avg_2_list.append(0)
        avg_3_list.append(0)
        avg_4_list.append(0)
        avg_5_list.append(0)
        avg_6_list.append(0)
        avg_7_list.append(0)
        avg_8_list.append(0)
        avg_9_list.append(0)
        avg_10_list.append(0)
        avg_11_list.append(0)
        avg_12_list.append(0)
        avg_13_list.append(0)
        avg_14_list.append(0)
        avg_15_list.append(0)
        avg_16_list.append(0)
        avg_17_list.append(0)
        avg_18_list.append(0)
        avg_19_list.append(0)
        avg_20_list.append(0)
        avg_21_list.append(0)
        avg_22_list.append(0)
        avg_23_list.append(0)
  

df['Avg Click Hour 0'] = avg_0_list
df['Avg Click Hour 1'] = avg_1_list 
df['Avg Click Hour 2'] = avg_2_list 
df['Avg Click Hour 3'] = avg_3_list 
df['Avg Click Hour 4'] = avg_4_list 
df['Avg Click Hour 5'] = avg_5_list 
df['Avg Click Hour 6'] = avg_6_list 
df['Avg Click Hour 7'] = avg_7_list 
df['Avg Click Hour 8'] = avg_8_list 
df['Avg Click Hour 9'] = avg_9_list 
df['Avg Click Hour 10'] = avg_10_list 
df['Avg Click Hour 11'] = avg_11_list 
df['Avg Click Hour 12'] = avg_12_list 
df['Avg Click Hour 13'] = avg_13_list 
df['Avg Click Hour 14'] = avg_14_list 
df['Avg Click Hour 15'] = avg_15_list 
df['Avg Click Hour 16'] = avg_16_list 
df['Avg Click Hour 17'] = avg_17_list 
df['Avg Click Hour 18'] = avg_18_list 
df['Avg Click Hour 19'] = avg_19_list 
df['Avg Click Hour 20'] = avg_20_list 
df['Avg Click Hour 21'] = avg_21_list 
df['Avg Click Hour 22'] = avg_22_list 
df['Avg Click Hour 23'] = avg_23_list 

df.to_csv('summed-and-averaged-click-data-Spring2016.csv', index=False)

  