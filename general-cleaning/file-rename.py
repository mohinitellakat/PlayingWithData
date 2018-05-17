# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.

Script to rename files in a folder
"""


import os

folder_path = raw_input("Enter the path of your folder: ")

data_files = [data_file for data_file in os.listdir(folder_path) if data_file.endswith('.pdf')]

for data_file in data_files:
    df_year = data_file[-8:-4]
    df_head = data_file[:-9]    
    data_file2 = df_year + "-" + df_head + ".pdf"
    d_file1 = os.path.join(folder_path, data_file)
    d_file2 = os.path.join(folder_path, data_file2)
    os.rename(d_file1, d_file2)
    