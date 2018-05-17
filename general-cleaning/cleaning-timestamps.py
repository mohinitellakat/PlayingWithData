# -*- coding: utf-8 -*-
"""
Created on Mon Mar 12 16:00:34 2018

@author: mt34546
"""

# -*- coding: utf-8 -*-
"""
Created on Wed Jan 03 11:57:42 2018

@author: mt34546
"""

import pandas as pd
import os
from os import listdir
from os.path import isfile, join
#from HTMLParser import HTMLParser
import re

allfiles = []

def scanfolder(folderpath):
    for path, dirs, files in os.walk(folderpath):
        for f in files:
            if f.endswith('.txt') or f.endswith('.docx'):
                allfiles.append(os.path.join(path, f))
    return allfiles

folder_path = raw_input('Enter your folder path here:')
all_files = scanfolder(folder_path)
print all_files

for singlefile in all_files:
    
    #file_path = folder_path + '\\' + singlefile
    
#    if ".txt" in singlefile:
#        with open(singlefile) as oldfile, open (singlefile + "_clean.txt", 'w') as newfile:
#            for line in oldfile:
#                if ":" not in line:
#                    newfile.write(line)
    
#    if "_clean.txt" in singlefile:
#        with open(singlefile) as oldfile, open (singlefile + "_clean2.txt", 'w') as newfile:
#            for num, line in enumerate(oldfile, 1):
#                if num != 1:
#                    newfile.write(line)
                    
    if "_clean2.txt" not in singlefile:
        os.remove(singlefile)
#    try:
#        df.to_csv('D:\\Games\\Games_Comments_Clean\\' + str(filename2) + '-clean.csv', index=False)  
#    except UnicodeEncodeError:
#        pass
    

    