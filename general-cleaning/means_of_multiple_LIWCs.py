# -*- coding: utf-8 -*-
"""
Created on Mon Sep 10 13:32:22 2018

@author: mt34546
"""

from os import listdir
import pandas as pd

def find_csv_filenames( path_to_dir, suffix=".csv" ):
    filenames = listdir(path_to_dir)
    return [ filename for filename in filenames if filename.endswith( suffix ) ]

def filename_to_series(filename):
    df = pd.read_csv(filepath + filename)
    s = df.mean()
    s['filename'] = filename
    return s

filepath = "G:/My Drive/GradSchoolStuff(UT)/Research-Data/Gaming Data/Reddit/201800910-LIWC-100WC/"

filenames = find_csv_filenames(filepath)


#for name in filenames: 
#    df = pd.read_csv(filepath + name)
#    df_means = df.mean()
print("working on means")
means = [filename_to_series(filename) for filename in filenames]
print (means)
df1 = pd.DataFrame(means)

df1.to_csv("G:/My Drive/GradSchoolStuff(UT)/Research-Data/Gaming Data/Reddit/LIWC_100WC_means.csv")