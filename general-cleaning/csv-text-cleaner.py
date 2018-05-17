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

def change_it(text):
    return re.sub(r'&(?!#\d{4};|amp;)', '&', text)

folder_path = raw_input('Enter your folder path here:')
all_files = [f for f in listdir(folder_path) if isfile(join(folder_path, f))]
print all_files

for singlefile in all_files:
    
    file_path = folder_path + '\\' + singlefile
    df = pd.read_csv(file_path)
    print ('file loaded')
    
    filename1 = os.path.basename(file_path)
    filename2 = filename1[:-4]
    print filename2
    
    
    df['body'] = df['body'].replace('', 'nan')
    print "blanks replaced"
    
    df = df.drop(df[(df.body == 'nan')|(df.body == '[deleted]')|(df.body == '[removed]')].index)
    print "cleaned empty cells"
    
    df['body'] = df['body'].str.decode('utf-8')
    print "formatted text"
    
    #df['body'] = df['body'].apply(HTMLParser().unescape)
    #df['body'] = df['body'].apply(change_it)

    df['body'] = [change_it(str(text)) for text in df['body']]
    print "corrected html translation"
#    htmldone = False
#    while htmldone == False:
#        try:
#            df['body'] = df['body'].apply(HTMLParser().unescape)
#            print "corrected html translation"
#            htmldone = True
#        except UnicodeDecodeError:
#            #print "got a unicode decode error"
#            continue
    
    
    try:
        df.to_csv('D:\\Games\\Games_Comments_Clean\\' + str(filename2) + '-clean.csv', index=False)  
    except UnicodeEncodeError:
        pass
    

    