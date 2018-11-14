# -*- coding: utf-8 -*-
"""
Created on Tue Nov  6 15:38:24 2018

This file should take a .pkl file and output the "percent gaming" for each person in the dataset

@author: mt34546
"""

import pickle
import csv

##convert subreddit list to a set
Users_To_Keep = set()
User_List_Filename = 'D:/Games/Reddit-Comments-GameNetwork/list_of_gaming_subreddits.txt'

with open(User_List_Filename, 'r', encoding='utf8') as UserFileIncoming:
    for line in UserFileIncoming:
        if line.strip() not in Users_To_Keep:
            Users_To_Keep.add(line.strip())


retain_values = list(Users_To_Keep)


#convert all to lowercase, convert to set for faster lookups
retain_values = set([x.lower() for x in retain_values])


##open pkl file and create the percent gaming for each person
#initialize variables
gaming_posts = 0
non_gaming_posts = 0
percent_gaming = 0
final_dict = dict()
pickle_file = 'D:/Games/Reddit-Comments-GameNetwork/Centrality_Dictionary.pkl'

with open(pickle_file, 'rb') as p_f:
    data = pickle.load(p_f)
    
    for user, subreddit_info in data.items(): 
        print ("username: " + user)     
        for key in subreddit_info: 
            
            if key in retain_values:
                gaming_posts += subreddit_info[key]
            else:
                non_gaming_posts += subreddit_info[key]
            
            percent_gaming = gaming_posts / (gaming_posts + non_gaming_posts)
        
        final_dict[user] = percent_gaming
        print(user + ":" + str(final_dict[user]))
        gaming_posts = 0
        non_gaming_posts = 0
        percent_gaming = 0
        
    
with open('C:/Users/mt34546/Documents/UTStuff/percent-gaming.csv', 'w', newline='') as csv_file:
    writer = csv.writer(csv_file)
    for key, value in final_dict.items():
       writer.writerow([key, value])        
    