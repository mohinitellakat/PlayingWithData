# -*- coding: utf-8 -*-
"""
Created on Mon Mar 19 16:54:11 2018

@author: mt34546
"""

import os
import random
import shutil

folder_length = 0
subreddit_files = []
mynewfolderpath = 'D:\\Games\\Games_Comments_Subset'
n=7
folder_path = raw_input('Enter your folder path here:')
all_folders = os.listdir(folder_path)

while n > 0: 
    for subreddit in all_folders: 
        mypath = folder_path + '\\' + subreddit
        mynewpath = mynewfolderpath + '_' + n + '_20\\' + subreddit
        print mynewpath
        subreddit_length = sum([len(files) for r, d, files in os.walk(mypath)])
        if subreddit_length > 20: 
            for path, subdirs, files in os.walk(mypath):
                for name in files:
                    subreddit_files.append(os.path.join(path, name))
            rand_20 = random.sample(subreddit_files, 20)
            if not os.path.exists (mynewpath):
                os.makedirs(mynewpath)
            for file_name in rand_20:
                if (os.path.isfile(file_name)):
                    shutil.copy(file_name, mynewpath)
        del subreddit_files[:]
        n = n - 1
        
    
    
    
#subdirs = listdir(mypath)
#for subdir in subdirs:
#    mypath_subdir = mypath + '\\' + subdir
#    subdir_length = len(os.walk(mypath_subdir).next()[2])
#    print subdir_length
#folder_length = folder_length + subdir_length
#print mypath + ':' + str(folder_length)


