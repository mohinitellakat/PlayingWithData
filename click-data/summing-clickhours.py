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

df1 = make_sum_dataframe('Click Hour 0.0')
df2 = make_sum_dataframe('Click Hour 1.0')
df3 = make_sum_dataframe('Click Hour 2.0')
df4 = make_sum_dataframe('Click Hour 3.0')
df5 = make_sum_dataframe('Click Hour 4.0')
df6 = make_sum_dataframe('Click Hour 5.0')
df7 = make_sum_dataframe('Click Hour 6.0')
df8 = make_sum_dataframe('Click Hour 7.0')
df9 = make_sum_dataframe('Click Hour 8.0')
df10 = make_sum_dataframe('Click Hour 9.0')
df11 = make_sum_dataframe('Click Hour 10.0')
df12 = make_sum_dataframe('Click Hour 11.0')
df13 = make_sum_dataframe('Click Hour 12.0')
df14 = make_sum_dataframe('Click Hour 13.0')
df15 = make_sum_dataframe('Click Hour 14.0')
df16 = make_sum_dataframe('Click Hour 15.0')
df17 = make_sum_dataframe('Click Hour 16.0')
df18 = make_sum_dataframe('Click Hour 17.0')
df19 = make_sum_dataframe('Click Hour 18.0')
df20 = make_sum_dataframe('Click Hour 19.0')
df21 = make_sum_dataframe('Click Hour 20.0')
df22= make_sum_dataframe('Click Hour 21.0')
df23 = make_sum_dataframe('Click Hour 22.0')
df24 = make_sum_dataframe('Click Hour 23.0')


df_sum_list = [df1,df2, df3, df4, df5, df6, df7, df8, df9, df10, df11, df12, df13, df14, df15, df16, df17, df18, df19, df20, df21, df22, df23, df24]
df25 = continuous_merge(df_sum_list, list_1)

df25.to_csv('summed-click-data-Spring2016.csv', index=False)

