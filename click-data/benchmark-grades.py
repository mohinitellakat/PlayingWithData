# -*- coding: utf-8 -*-
"""
Created on Fri Sep 09 15:34:10 2016

Short script to get the benchmark grade data into BM#, EID, GRADE column format

@author: Mohini
"""
import pandas as pd

file_path = raw_input('Enter your filepath here:')

df = pd.read_csv(file_path)

new_file = df.stack().to_frame()


new_file.to_csv('benchmark-grades-clean.csv')