# -*- coding: utf-8 -*-
"""
Created on Mon Jan 28 12:10:56 2019

@author: mt34546
"""

import csv
import glob
import os
from shutil import copyfile

def find(name, path):
    for root, dirs, files in os.walk(path):
        if name in files:
            return os.path.join(root, name)

#get list of authors if you only want to run this on a subset of people
author_list = 'G:/My Drive/GradSchoolStuff-UT/Research-Data/Gaming Data/centrality analysis/in-depth-DotA2/rand2000-author-list-DotA2.csv'
with open(author_list, 'r', encoding = 'utf8') as f:
    reader = csv.reader(f)
    dota_author_list = list(reader)
    
print ('done with dota authors list')
#get list of filenames
dota_filenames = []
for filename in glob.iglob('D:\\Games\\20180423_Game_Comments\\EZPZTXT\\DotA2\\**\\*.txt', recursive=True):
    dota_filenames.append(filename)

print ('done with filenames list')


#move appropriate files to a new folder   
for file in dota_filenames:
    for author in dota_author_list:
        username = os.path.basename(file)
        if (author[0] == username):
            copyfile(file, 'D:\\Games\\20180423_Game_Comments\\DotA2_hml_rand2000_subset\\' + username)
            print ('D:\\Games\\20180423_Game_Comments\\DotA2_hml_rand2000_subset\\' + username)
    
