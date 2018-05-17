# -*- coding: utf-8 -*-
"""
Created on Thu Mar 02 15:50:52 2017

@author: mt34546
"""

# -*- coding: utf-8 -*-
"""
Created on Wed Mar 01 12:26:27 2017

@author: mt34546
"""


from bs4 import BeautifulSoup
import pandas as pd
import requests


file_path = raw_input('Enter your filepath here:')

df = pd.read_csv(file_path)

ratings = []
views = []

print len(df['transcript_url'])

for link in df['transcript_url']:

    try:
        resp = requests.get(link, headers = {'User-agent': 'your bot 0.1'})
        resp.raise_for_status()
        content = resp.content
        soup = BeautifulSoup(content.decode('utf-8', 'ignore'))
        bsclass = soup.find('span', { 'class' : 'meta__row' })
        if bsclass:
            temp1 = soup.find_all('span', { 'class' : 'meta__row' })
            for temp in temp1:
                rating_text = temp.text
                encoded_rating = u''.join(rating_text).encode('utf-8').strip()
                encoded_rating = encoded_rating.replace('\n', ' ').replace('\\' , '').replace('\xe2\x80\x94', '').replace('Rated ','')
                
                ratings.append(encoded_rating)
        else:
            ratings.append('N/A')
    except requests.exceptions.HTTPError as err:
            if err.response.status_code > 400:
                print "Page not found"
                ratings.append('N/A')
            else:
                raise
        
    
print len(ratings)
    
df['TopRatings'] = ratings
print 'Done with ratings!'

    
    
                
for link in df['public_url']:

    resp = requests.get(link, headers = {'User-agent': 'your bot 0.1'})
    content = resp.content
    soup = BeautifulSoup(content.decode('utf-8', 'ignore'))
    bsid = soup.find('div', { 'id' : 'sharing-count' })
    if bsid:
        temp1 = soup.find_all('div', { 'id' : 'sharing-count' })
        for temp in temp1:
            views_text = temp.text
            encoded_views = u''.join(views_text).encode('utf-8').strip()
            encoded_views = encoded_views.replace('\n', ' ').replace('\\' , '').replace('\xe2\x80\x94', '').replace(' \t   \t\t\tTotal \t\t  \t\t\tviews','')
    
            views.append(encoded_views)
    else:
        views.append('N/A')


            
df['Views'] = views
print 'Done with Views!'



df.to_csv('ted_talks_with_ratings_and_views.csv', index=False)
