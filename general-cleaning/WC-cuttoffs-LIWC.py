# -*- coding: utf-8 -*-
"""
Created on Wed Sep  5 13:56:15 2018

@author: mt34546
"""

from os import listdir
import pandas as pd

def find_csv_filenames( path_to_dir, suffix=".csv" ):
    filenames = listdir(path_to_dir)
    return [ filename for filename in filenames if filename.endswith( suffix ) ]


filepath = "G:/My Drive/GradSchoolStuff(UT)/Research-Data/Gaming Data/Reddit/20180910-LIWC-OG/"

filenames = find_csv_filenames(filepath)

for name in filenames: 
    df1 = pd.read_csv(filepath + name)
    
    df1 = df1[df1.WC >= 100]
    
    df1.to_csv("G:/My Drive/GradSchoolStuff(UT)/Research-Data/Gaming Data/Reddit/201800910-LIWC-100WC/100WC-" + name)
    
    
    
