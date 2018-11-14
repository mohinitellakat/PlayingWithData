# -*- coding: utf-8 -*-
"""
Mohini Tellakat
2018_06_05

Running LIWCiePy on a ton of data
"""
#import the lib
import LIWCiePy
import os
import json
from multiprocessing.dummy import Pool as ThreadPool 

import time
start_time = time.time()

#instantiate a new "LIWCer" object
#the first parameter is the location/filename of the dictionary file
#the directory is not needed if the dictionary file is in the same directory as this script
#the second parameter is the encoding of your dictionary file
LIWC = LIWCiePy.LIWCer('D:/LIWCiePy-OG-code/2017-04-15-LIWC2015 Dictionary.dic', file_encoding='utf-8')

#analyze some text:
#file_text should be the string that you want to analyze
#the "SummaryMeasures" parameter is for if you are using the LIWC2015 dictionary and
#want to calculate Analytic, Tone, Clout, and Authentic. This will break if set to "True"
#and using any dictionary other than the official LIWC2015 English dictionary

#test file path: D:\Games\TestLIWCiePyFolder
#This is the path to where your file that has all of the sub files is located
folder_path = input('Enter your filepath here:')

#creates a list of all the folders inside your main folder
all_folders = os.listdir(folder_path)

def make_json(name):
    #gets the path for the text you want to analyze and sticks it into the variable, results
    file_text_path = (os.path.join(path, name))

    #need to read in the file text:
    with open(file_text_path, 'r', encoding='utf-8') as file_text_incoming:

        results = LIWC.analyze(file_text_incoming.read(), SummaryMeasures=True)
        
        #This is the main folder where you want your output to go
        home_folder = 'D:\Games\Multi-TestLIWCiePy-JSON'
        #this will name sub-folders based on your original subfolder names, but will contain 
        #JSON outputs instead
        sub_folder = os.path.join(home_folder, folder) 
        
        #Creates a directory for this sub_folder if it doesn't already exist
        try:
            if not os.path.exists(sub_folder):
                os.makedirs(sub_folder)
        except:
            pass

            
        #writes files to JSON and puts them in your folder 
        with open(os.path.join(sub_folder, name + '.json'), 'w') as fp:
            json.dump(results, fp)

filepaths = []

def get_path(folder):
    os.path.join(folder_path, folder)
    
filepaths = 

pool = ThreadPool(2)

pool2 = ThreadPool(4)
           
for folder in all_folders:
    root = os.path.join(folder_path, folder)
    for path, subdirs, files in os.walk(root):
        pool.map(make_json, files)
        

print ("My program took", time.time() - start_time, "to run")


