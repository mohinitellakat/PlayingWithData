# -*- coding: utf-8 -*-
"""
Mohini Tellakat
2018_06_05

Running LIWCiePy on a ton of data
"""
#import the lib
import LIWCiePy27
import os
import json

#instantiate a new "LIWCer" object
#the first parameter is the location/filename of the dictionary file
#the directory is not needed if the dictionary file is in the same directory as this script
#the second parameter is the encoding of your dictionary file
LIWC = LIWCiePy27.LIWCer('D:/LIWCiePy-OG-code/2017-04-15-LIWC2015 Dictionary.dic')

#analyze some text:
#file_text should be the string that you want to analyze
#the "SummaryMeasures" parameter is for if you are using the LIWC2015 dictionary and
#want to calculate Analytic, Tone, Clout, and Authentic. This will break if set to "True"
#and using any dictionary other than the official LIWC2015 English dictionary

#test file path: D:\Games\TestLIWCiePyFolder
#This is the path to where your file that has all of the sub files is located
folder_path = raw_input('Enter your filepath here:')

#creates a list of all the folders inside your main folder
all_folders = os.listdir(folder_path)


for folder in all_folders:
    root = os.path.join(folder_path, folder)
    for path, subdirs, files in os.walk(root):
        for name in files:
            #gets the path for the text you want to analyze and sticks it into the variable, results
            file_text = (os.path.join(path, name))
            results = LIWC.analyze(file_text, SummaryMeasures=True)
            #This is the main folder where you want your output to go
            home_folder = 'D:/Games/TestLIWCiePy_JSON'
            #this will name sub-folders based on your original subfolder names, but will contain 
            #JSON outputs instead
            sub_folder = os.path.join(home_folder, folder) 
            
            #Creates a directory for this sub_folder if it doesn't already exist
            if not os.path.exists(sub_folder):
                os.makedirs(sub_folder)
            #writes files to JSON and puts them in your folder 
            with open(os.path.join(sub_folder, name + '.json'), 'w') as fp:
                json.dump(results, fp)

