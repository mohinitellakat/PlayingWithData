# -*- coding: utf-8 -*-
"""
Created on Sun Aug 21 22:00:54 2016

@author: Mohini

Gets rid of ChatIDs that only have 1 person
"""

import pandas as pd

file_path = raw_input('Enter your filepath here:')

df = pd.read_csv(file_path)

#Puts ChatIDs and Person into a dict where the ChatID is the key and the Person is appended to a unique chatID
chat_id_dict = {k: g['Person'].tolist() for k, g in df.groupby('ChatID')}
print chat_id_dict

# check length of Person list in dict. If not enough people, delete data for the ChatID
for key in chat_id_dict:
    if len(chat_id_dict[key]) < 2:
        df = df[df.ChatID != key]
        print 'deleting row'
    else:
        print 'ChatID is valid'
  
#Send to CSV file  
df.to_csv('LSM_data_2people_only.csv', index=False)

