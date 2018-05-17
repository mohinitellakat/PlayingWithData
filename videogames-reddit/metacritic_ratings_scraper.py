# -*- coding: utf-8 -*-
"""
Created on Mon Apr 23 11:52:27 2018

@author: mt34546
"""

#import urllib2
import requests
from bs4 import BeautifulSoup
import pandas as pd

rating_num_list = []
reviewer_list = []
rating_text_list = []

##CHANGE STUFF UNDER THIS COMMENT
#This is the link to either the general or critic reviews for a specific game
main_link = 'http://www.metacritic.com/game/pc/world-of-warcraft/critic-reviews'

try:       
    resp = requests.get(main_link, headers = {'User-agent': 'your bot 0.1'})
    resp.raise_for_status()
    content = resp.content
    soup = BeautifulSoup(content.decode('utf-8', 'ignore'), "html.parser")
    
    #website specific
    big_container = soup.find_all('div', {'class' : 'review critic'})
    for pt in big_container:
        rating_num = pt.find('div', {'class': 'indiv'}).text.strip() 
        reviewer = pt.find('div', {'class':'source'}).text.strip()
        rating_text = pt.find('div', {'class': 'clr summary'}).text.strip()

#        print (rating_num)
#        print (reviewer)
#        print (rating_text)
#        
        rating_num_list.append(rating_num)
        reviewer_list.append(reviewer)
        rating_text_list.append(rating_text)

except requests.exceptions.HTTPError as err:
    if err.response.status_code > 400:
        print ("Page not found")
        link = ''
    else:
        raise
        
        
dataset = pd.DataFrame({'Rating Num': rating_num_list, 'Critic': reviewer_list, 'Rating Text': rating_text_list})

##CHANGE STUFF UNDER THIS COMMENT
#game_critic/user_reviews.csv
dataset.to_csv("D:/Games/wow_critic_reviews.csv", encoding = "utf-8", index = False)

            
