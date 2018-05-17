# -*- coding: utf-8 -*-
"""
Created on Mon Sep 04 10:41:10 2017

@author: mt34546
"""

import pandas as pd

file_path = raw_input('Enter your filepath here:')
print ('loading file')
df = pd.read_csv(file_path)
print ('file loaded')
#REDDIT SUBMISSIONS INTO FILES : C:\Users\mt34546\Dropbox\GradSchoolStuff(UT)\_REDDIT - UT Austin\2017-07-17 - UTAustin - Extracted Reddit Data - Submissions.csv
#for i, text in enumerate(df['selftext']):
#    if str(text) not in ['','nan','[deleted]','[removed]']:
#        with open('C:\\Users\\mt34546\\Documents\\UTStuff\\PennebakerLabStuff\\REDDIT_GAMES\\REDDIT-Games-Submissions\\' + str(df['id'][i]) + '.txt', 'ab+') as text_file:
#            text_file.write(str(text))



       

#REDDIT COMMENTS INTO FILES : C:\Users\mt34546\Dropbox\GradSchoolStuff(UT)\_REDDIT - UT Austin\2017-07-17 - UTAustin - Extracted Reddit Data - Comments.csv
for i, text in enumerate(df['body']):
    if str(text) not in ['','nan','[deleted]','[removed]']:
        with open('C:\\Users\\mt34546\\Documents\\UTStuff\\PennebakerLabStuff\\REDDIT_GAMES\\REDDIT-Games-Comments\\' + str(df['id'][i]) + '.txt', 'ab+') as text_file:
            text_file.write(str(text))
            print "wrote a file"
