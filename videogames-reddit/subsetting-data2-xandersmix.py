# -*- coding: utf-8 -*-
"""
Created on Mon Jan 28 12:10:56 2019

@author: mt34546
"""

import glob
import os
from shutil import copyfile

#get list of authors if you only want to run this on a subset of people
author_list = 'G:/My Drive/GradSchoolStuff-UT/Research-Data/Gaming Data/centrality analysis/in-depth-DotA2/MEM_hml_2000/rand2000-author-list-DotA2.csv'
author_set = set()
with open(author_list, 'r', encoding = 'utf8') as f:
    for row in f:
        row = row.strip()
        author_set.add(row)
    
print ('done with dota authors list: ', len(author_set))
#copy author's files to new location

count = 0
for filename in glob.iglob('D:\\Games\\20180423_Game_Comments\\EZPZTXT\\DotA2\\**\\*.txt', recursive=True):
    if count % 5000 == 0:
        print(count)
    count += 1
    username = os.path.basename(filename)
    if username in author_set:
        new_filename = 'D:\\Games\\20180423_Game_Comments\\DotA2_hml_rand2000_subset\\{username}'.format(username=username)
        copyfile(filename, new_filename)
        print(new_filename)
