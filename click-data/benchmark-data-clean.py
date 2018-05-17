# -*- coding: utf-8 -*-
"""
Cleaning up and modifying benchmark data from the 2015 Intro Psych Click Dataset

Created on Tue Jul 26 20:32:54 2016

@author: Mohini
"""
import os
import pandas as pd
import pytz
from pytz import UTC
from pytz import timezone
import csv
import ntpath

folder_path = raw_input("Enter the path of your folder: ")

benchmark_data_files = [benchmark_data_file for benchmark_data_file in os.listdir(folder_path) if benchmark_data_file.endswith('.csv')]

for bm_file in benchmark_data_files:
    
    answer_choice_count = []
    answer_delete_count = []
    clipboard_copy_count = []
    data_save_count = []
    page_load_count = []
    tab_click_count = []
    tab_save_and_next_count= []
    
    answer_choice_sum = []
    answer_delete_sum = []
    clipboard_copy_sum = []
    data_save_sum = []
    page_load_sum = []
    tab_click_sum = []
    tab_save_and_next_sum= []
    
    date_list =[]
    time_list =[]
    
    df = pd.read_csv(os.path.join(folder_path, bm_file))
    
    df1 = df.dropna(axis='rows', how='all')

    df1 = df1[['Login ID','Date/Time','Event Type']]
    
    #Seperate out date and time
    for row in df1['Date/Time']:
        ts = pd.Timestamp(row)
        try:
            ts.replace(tzinfo=None)
            time_UTC = ts.tz_localize(UTC)
            central = pytz.timezone('US/Central')
            central_normal = central.normalize(time_UTC)
        
            date_list.append(str(central_normal).rsplit(' ', 1)[0])
            time_list.append(str(central_normal).rsplit(' ', 1)[1])
        except:
            date_list.append("nan")
            time_list.append("nan")
            
    df1['Date'] = date_list
    df1['Time'] = time_list

       
    #Different types of click counts per EID
    for row in df1['Event Type']:

        if row == 'answer_choice':
            answer_choice_count.append(1)
            answer_delete_count.append(0) 
            clipboard_copy_count.append(0)
            data_save_count.append(0)
            page_load_count.append(0)
            tab_click_count.append(0)
            tab_save_and_next_count.append(0)
        elif row == 'answer_delete':
            answer_choice_count.append(0)
            answer_delete_count.append(1) 
            clipboard_copy_count.append(0)
            data_save_count.append(0)
            page_load_count.append(0)
            tab_click_count.append(0)
            tab_save_and_next_count.append(0)
        elif row == 'clipboard_copy':
            answer_choice_count.append(0)
            answer_delete_count.append(0) 
            clipboard_copy_count.append(1)
            data_save_count.append(0)
            page_load_count.append(0)
            tab_click_count.append(0)
            tab_save_and_next_count.append(0) 
        elif row == 'data_save':
            answer_choice_count.append(0)
            answer_delete_count.append(0) 
            clipboard_copy_count.append(0)
            data_save_count.append(1)
            page_load_count.append(0)
            tab_click_count.append(0)
            tab_save_and_next_count.append(0) 
        elif row == 'page_load':
            answer_choice_count.append(0)
            answer_delete_count.append(0) 
            clipboard_copy_count.append(0)
            data_save_count.append(0)
            page_load_count.append(1)
            tab_click_count.append(0)
            tab_save_and_next_count.append(0) 
        elif row == 'tab_click':
            answer_choice_count.append(0)
            answer_delete_count.append(0) 
            clipboard_copy_count.append(0)
            data_save_count.append(0)
            page_load_count.append(0)
            tab_click_count.append(1)
            tab_save_and_next_count.append(0) 
        elif row == 'tab_save_and_next':
            answer_choice_count.append(0)
            answer_delete_count.append(0) 
            clipboard_copy_count.append(0)
            data_save_count.append(0)
            page_load_count.append(0)
            tab_click_count.append(0)
            tab_save_and_next_count.append(1)
        else:
            answer_choice_count.append(0)
            answer_delete_count.append(0) 
            clipboard_copy_count.append(0)
            data_save_count.append(0)
            page_load_count.append(0)
            tab_click_count.append(0)
            tab_save_and_next_count.append(0)
            
            
    df1['answer_choice counts'] = answer_choice_count
    df1['answer_delete counts'] = answer_delete_count 
    df1['clipboard_copy counts'] = clipboard_copy_count 
    df1['data_save counts'] = data_save_count
    df1['page_load counts'] = page_load_count 
    df1['tab_click counts'] = tab_click_count 
    df1['tab_save_and_next counts'] = tab_save_and_next_count
    
    for eid in df1['Login ID']:
        answer_choice_sum.append(df1.loc[df1['Login ID']== eid, 'answer_choice counts'].sum())
        answer_delete_sum.append(df1.loc[df1['Login ID']== eid, 'answer_delete counts'].sum())
        clipboard_copy_sum.append(df1.loc[df1['Login ID']== eid, 'clipboard_copy counts'].sum())
        data_save_sum.append(df1.loc[df1['Login ID']== eid, 'data_save counts'].sum())
        page_load_sum.append(df1.loc[df1['Login ID']== eid, 'page_load counts'].sum())
        tab_click_sum.append(df1.loc[df1['Login ID']== eid, 'tab_click counts'].sum())
        tab_save_and_next_sum.append(df1.loc[df1['Login ID']== eid, 'tab_save_and_next counts'].sum())

    df1['answer_choice sums'] = answer_choice_sum
    df1['answer_delete sums'] = answer_delete_sum 
    df1['clipboard_copy sums'] = clipboard_copy_sum 
    df1['data_save sums'] = data_save_sum
    df1['page_load sums'] = page_load_sum 
    df1['tab_click sums'] = tab_click_sum 
    df1['tab_save_and_next sums'] = tab_save_and_next_sum
    
    newdf1 = df1[['Login ID', 'Date', 'Time', 'Event Type', 'answer_choice counts', 'answer_delete counts', 'clipboard_copy counts', 'data_save counts', 'page_load counts', 'tab_click counts', 'tab_save_and_next counts' ]].copy()
    newdf2 = df1[['Login ID', 'answer_choice sums', 'answer_delete sums', 'clipboard_copy sums', 'data_save sums', 'page_load sums', 'tab_click sums', 'tab_save_and_next sums' ]].copy()

    newdf2 = newdf2.groupby(['Login ID']).max()
    
    newdf1.to_csv('bm-data-clean/bm_data_clean_expanded_' + bm_file , index=False)
    newdf2.to_csv('bm-data-clean/bm_data_clean_sums_' + bm_file)
    
    
    

    
