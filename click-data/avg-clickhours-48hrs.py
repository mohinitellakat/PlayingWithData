# -*- coding: utf-8 -*-
"""
Created on Tue Dec 13 14:19:45 2016

@author: mt34546
"""

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
avg_24_list = []
avg_25_list = []
avg_26_list = []
avg_27_list = []
avg_28_list = []
avg_29_list = []
avg_30_list = []
avg_31_list = []
avg_32_list = []
avg_33_list = []
avg_34_list = []
avg_35_list = []
avg_36_list = []
avg_37_list = []
avg_38_list = []
avg_39_list = []

file_path = raw_input('Enter your filepath here:')

df = pd.read_csv(file_path)   

col_list = list(df)
col_list.remove('eid')
col_list.remove('Benchmark Number')
col_list.remove('Grade')

df['Sum_Col_List'] = df[col_list].sum(axis=1)
for idx, sum_col in enumerate(df['Sum_Col_List']):
    numerator_0 = df['ClickHour0'][idx]
    numerator_1 = df['ClickHour1'][idx]
    numerator_2 = df['ClickHour2'][idx]
    numerator_3 = df['ClickHour3'][idx]
    numerator_4 = df['ClickHour4'][idx]
    numerator_5 = df['ClickHour5'][idx]
    numerator_6 = df['ClickHour6'][idx]
    numerator_7 = df['ClickHour7'][idx]
    numerator_8 = df['ClickHour8'][idx]
    numerator_9 = df['ClickHour9'][idx]
    numerator_10 = df['ClickHour10'][idx]
    numerator_11 = df['ClickHour11'][idx]
    numerator_12 = df['ClickHour12'][idx]
    numerator_13 = df['ClickHour13'][idx]
    numerator_14 = df['ClickHour14'][idx]
    numerator_15 = df['ClickHour15'][idx]
    numerator_16 = df['ClickHour16'][idx]
    numerator_17 = df['ClickHour17'][idx]
    numerator_18 = df['ClickHour18'][idx]
    numerator_19 = df['ClickHour19'][idx]
    numerator_20 = df['ClickHour20'][idx]
    numerator_21 = df['ClickHour21'][idx]
    numerator_22 = df['ClickHour22'][idx]
    numerator_23 = df['ClickHour23'][idx]
    numerator_24 = df['ClickHour24'][idx]
    numerator_25 = df['ClickHour25'][idx]
    numerator_26 = df['ClickHour26'][idx]
    numerator_27 = df['ClickHour27'][idx]
    numerator_28 = df['ClickHour28'][idx]
    numerator_29 = df['ClickHour29'][idx]
    numerator_30 = df['ClickHour30'][idx]
    numerator_31 = df['ClickHour31'][idx]
    numerator_32 = df['ClickHour32'][idx]
    numerator_33 = df['ClickHour33'][idx]
    numerator_34 = df['ClickHour34'][idx]
    numerator_35 = df['ClickHour35'][idx]
    numerator_36 = df['ClickHour36'][idx]
    numerator_37 = df['ClickHour37'][idx]
    numerator_38 = df['ClickHour38'][idx]
    numerator_39 = df['ClickHour39'][idx]
    
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
        avg_24 = float(numerator_24)/sum_col
        avg_25 = float(numerator_25)/sum_col
        avg_26 = float(numerator_26)/sum_col
        avg_27 = float(numerator_27)/sum_col
        avg_28 = float(numerator_28)/sum_col
        avg_29 = float(numerator_29)/sum_col
        avg_30 = float(numerator_30)/sum_col
        avg_31 = float(numerator_31)/sum_col
        avg_32 = float(numerator_32)/sum_col
        avg_33 = float(numerator_33)/sum_col
        avg_34 = float(numerator_34)/sum_col
        avg_35 = float(numerator_35)/sum_col
        avg_36 = float(numerator_36)/sum_col
        avg_37 = float(numerator_37)/sum_col
        avg_38 = float(numerator_38)/sum_col
        avg_39 = float(numerator_39)/sum_col
        
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
        avg_24_list.append(avg_24)
        avg_25_list.append(avg_25)
        avg_26_list.append(avg_26)
        avg_27_list.append(avg_27)
        avg_28_list.append(avg_28)
        avg_29_list.append(avg_29)
        avg_30_list.append(avg_30)
        avg_31_list.append(avg_31)
        avg_32_list.append(avg_32)
        avg_33_list.append(avg_33)
        avg_34_list.append(avg_34)
        avg_35_list.append(avg_35)
        avg_36_list.append(avg_36)
        avg_37_list.append(avg_37)
        avg_38_list.append(avg_38)
        avg_39_list.append(avg_39)
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
        avg_24_list.append(0)
        avg_25_list.append(0)
        avg_26_list.append(0)
        avg_27_list.append(0)
        avg_28_list.append(0)
        avg_29_list.append(0)
        avg_30_list.append(0)
        avg_31_list.append(0)
        avg_32_list.append(0)
        avg_33_list.append(0)
        avg_34_list.append(0)
        avg_35_list.append(0)
        avg_36_list.append(0)
        avg_37_list.append(0)
        avg_38_list.append(0)
        avg_39_list.append(0)
  

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
df['Avg Click Hour 24'] = avg_24_list
df['Avg Click Hour 25'] = avg_25_list 
df['Avg Click Hour 26'] = avg_26_list 
df['Avg Click Hour 27'] = avg_27_list 
df['Avg Click Hour 28'] = avg_28_list 
df['Avg Click Hour 29'] = avg_29_list 
df['Avg Click Hour 30'] = avg_30_list 
df['Avg Click Hour 31'] = avg_31_list 
df['Avg Click Hour 32'] = avg_32_list 
df['Avg Click Hour 33'] = avg_33_list 
df['Avg Click Hour 34'] = avg_34_list 
df['Avg Click Hour 35'] = avg_35_list 
df['Avg Click Hour 36'] = avg_36_list 
df['Avg Click Hour 37'] = avg_37_list 
df['Avg Click Hour 38'] = avg_38_list 
df['Avg Click Hour 39'] = avg_39_list  

df.to_csv('48-hr-data/summed-and-averaged-click-data-48hr-Spring2016.csv', index=False)

  