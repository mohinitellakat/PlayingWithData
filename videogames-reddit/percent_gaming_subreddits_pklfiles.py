# -*- coding: utf-8 -*-
"""
Created on Tue Nov  6 15:38:24 2018

This file should take a .pkl file and output the "percent gaming" for each person in the dataset

@author: mt34546
"""

import pickle
import csv

##convert subreddit list to a set
Subreddits_To_Keep = set()
Subreddit_List_Filename = 'D:/Games/Reddit-Comments-GameNetwork/list_of_gaming_subreddits.txt'

with open(Subreddit_List_Filename, 'r', encoding='utf8') as SubredditFileIncoming:
    for line in SubredditFileIncoming:
        if line.strip() not in Subreddits_To_Keep:
            Subreddits_To_Keep.add(line.strip())


retain_values = list(Subreddits_To_Keep)


#convert all to lowercase, convert to set for faster lookups
#retain_values = set([x.lower() for x in retain_values])

#get list of authors if you only want to run this on a subset of people
#author_list = 'G:/My Drive/GradSchoolStuff(UT)/Research-Data/Gaming Data/centrality analysis/dota_author_list.csv'
#with open(author_list, 'rb', encoding = 'utf8') as f:
#    reader = csv.reader(f)
#    dota_author_list = list(reader)


##open pkl file and create the percent gaming for each person
#initialize variables
gaming_posts = 0
non_gaming_posts = 0
percent_gaming = 0
DotA2_posts = 0
final_dict = dict()
pickle_file = 'D:/Games/Reddit-Comments-GameNetwork/Centrality_Dictionary.pkl'


with open(pickle_file, 'rb') as p_f:
    data = pickle.load(p_f)
    
    for user, subreddit_info in data.items(): 
        print ("username: " + user)     
        for key in subreddit_info:
#            if key == 'DotA2':
#                print('im in dota2')
#                DotA2_posts += subreddit_info[key]
            
            if key in retain_values:
                gaming_posts += subreddit_info[key]
            else:
                non_gaming_posts += subreddit_info[key]
#            
            percent_gaming = gaming_posts / (gaming_posts + non_gaming_posts)
            
#            DotA2_centrality = DotA2_posts / (gaming_posts + non_gaming_posts)
        
        final_dict[user] = [gaming_posts, non_gaming_posts, percent_gaming]
#        final_dict[user] = [DotA2_posts, DotA2_centrality]
        print(user + ":" + str(final_dict[user]))
        gaming_posts = 0
        non_gaming_posts = 0
        percent_gaming = 0
#        DotA2_posts = 0
        
    
with open('G:/My Drive/GradSchoolStuff(UT)/Research-Data/Gaming Data/centrality analysis/post_stats_centrality.csv', 'w', newline='') as csv_file:
    writer = csv.writer(csv_file)
    for key, value in final_dict.items():
       writer.writerow([key, value[0], value[1], value[2]])   
#       writer.writerow([key, value[0], value[1]])