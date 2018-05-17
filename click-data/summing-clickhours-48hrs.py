# -*- coding: utf-8 -*-
"""
Created on Tue Dec 13 11:42:19 2016

@author: mt34546
"""

# -*- coding: utf-8 -*-
"""
Created on Sun Oct 16 13:17:05 2016

@author: Mohini


"""
import pandas as pd


#Sums column data with respect to a given key
def make_sum_dataframe(colname):
    dfx = df.groupby(by=['eid','Benchmark Number','Grade'])[colname].sum().to_frame()
    dfx = dfx.reset_index()
    return dfx

    


    
#getting rid of excess or duplicate data in the dataframe    
def continuous_merge (df_list,key):
    for i in range(len(df_list)):
        if i < len(df_list):
            if (i+1) < len(df_list):
                this_item = df_list[i]
                next_item = df_list[i+1]
                merged_item = pd.merge(this_item, next_item, on=key)
                df_list[i+1] = merged_item
            elif (i+1) == len(df_list):
                df_list[i] = merged_item
            else:
                print "This is out of range1"
        else:
            print "This is out of range2"                     
    return merged_item


file_path = raw_input('Enter your filepath here:')

df = pd.read_csv(file_path)    
    
list_1 = ['eid', 'Benchmark Number','Grade']

df1 = make_sum_dataframe('ClickHour0')
df2 = make_sum_dataframe('ClickHour1')
df3 = make_sum_dataframe('ClickHour2')
df4 = make_sum_dataframe('ClickHour3')
df5 = make_sum_dataframe('ClickHour4')
df6 = make_sum_dataframe('ClickHour5')
df7 = make_sum_dataframe('ClickHour6')
df8 = make_sum_dataframe('ClickHour7')
df9 = make_sum_dataframe('ClickHour8')
df10 = make_sum_dataframe('ClickHour9')
df11 = make_sum_dataframe('ClickHour10')
df12 = make_sum_dataframe('ClickHour11')
df13 = make_sum_dataframe('ClickHour12')
df14 = make_sum_dataframe('ClickHour13')
df15 = make_sum_dataframe('ClickHour14')
df16 = make_sum_dataframe('ClickHour15')
df17 = make_sum_dataframe('ClickHour16')
df18 = make_sum_dataframe('ClickHour17')
df19 = make_sum_dataframe('ClickHour18')
df20 = make_sum_dataframe('ClickHour19')
df21 = make_sum_dataframe('ClickHour20')
df22= make_sum_dataframe('ClickHour21')
df23 = make_sum_dataframe('ClickHour22')
df24 = make_sum_dataframe('ClickHour23')
df25 = make_sum_dataframe('ClickHour24')
df26 = make_sum_dataframe('ClickHour25')
df27 = make_sum_dataframe('ClickHour26')
df28 = make_sum_dataframe('ClickHour27')
df29 = make_sum_dataframe('ClickHour28')
df30 = make_sum_dataframe('ClickHour29')
df31 = make_sum_dataframe('ClickHour30')
df32 = make_sum_dataframe('ClickHour31')
df33 = make_sum_dataframe('ClickHour32')
df34 = make_sum_dataframe('ClickHour33')
df35 = make_sum_dataframe('ClickHour34')
df36 = make_sum_dataframe('ClickHour35')
df37 = make_sum_dataframe('ClickHour36')
df38 = make_sum_dataframe('ClickHour37')
df39 = make_sum_dataframe('ClickHour38')
df40 = make_sum_dataframe('ClickHour39')



df_sum_list = [df1,df2, df3, df4, df5, df6, df7, df8, df9, df10, df11, df12, df13, df14, df15, df16, df17, df18, df19, df20, df21, df22, df23, df24, df25 ,df26, df27, df28, df29, df30, df31, df32, df33, df34, df35, df36, df37, df38, df39, df40]
df41 = continuous_merge(df_sum_list, list_1)

df41.to_csv('48-hr-data/summed-click-data-48Hour-Spring2016.csv', index=False)
