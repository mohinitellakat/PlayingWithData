# -*- coding: utf-8 -*-
"""
Created on Mon Jul 17 12:44:06 2017

@author: mt34546
"""

# -*- coding: utf-8 -*-
"""
Created on Thu Jun 29 11:57:18 2017

@author: mt34546
"""

# -*- coding: utf-8 -*-
"""
Created on Wed Mar 01 12:26:27 2017

@author: mt34546
"""

#import urllib2
import requests
from bs4 import BeautifulSoup
import pandas as pd
import re

page_urls = []
post_urls = []
blog_post_full = []

main_link = 'https://creakyjoints.org/author/jonathan-h/'
pagenum = 2

page_urls.append(main_link)

while (pagenum < 14):
    new_link = str(main_link) + 'page/' + str(pagenum)
    page_urls.append(new_link)
    pagenum = pagenum + 1
    print new_link
pagenum = 2


#get the month urls from the homepage
for page in page_urls:
    try:       
        resp = requests.get(page, headers = {'User-agent': 'your bot 0.1'})
        resp.raise_for_status()
        content = resp.content
        soup = BeautifulSoup(content.decode('utf-8', 'ignore'))
        big_container = soup.find_all('div', {'class' : 'home-posts categories-posts-container'})
        for pt in big_container:
            article_links = pt.find_all('a', href=True)
            for lnk in article_links:
                post_urls.append(lnk.get('href'))
    
        
    except requests.exceptions.HTTPError as err:
        if err.response.status_code == 404:
            print "Page not found"
            link = ''
        else:
            raise
            

print len(post_urls)

#write posts to text files
           
for post in post_urls:
    url = post.rsplit('/', 1)[0]
    file_name_pt1 = url[24:]
    file_name = file_name_pt1.replace('/', '-')
    
    with open('C:\\Users\\mt34546\\Dropbox\\GradSchoolStuff(UT)\\rheumatoid-arthritis-blogs\\creakyjoints-jonathanh-blogposts\\' + file_name + '.txt', 'w') as text_file:
        if 'https://' in post: 
            try:
                resp3 = requests.get(post, headers = {'User-agent': 'your bot 0.1'})
                resp3.raise_for_status()
                content = resp3.content
                soup3 = BeautifulSoup(content.decode('utf-8', 'ignore'))
    
                temp1 = soup3.find_all('div', { 'class' : 'entry-content' })
                for temp in temp1:
                    temp2 = temp.find_all('p')
                    for tmp in temp2:
                        post_text = tmp.text
                        encoded_post_text = u''.join(post_text).encode('utf-8').strip()
                        
                        blog_post_full.append(' ' + encoded_post_text)
                        
                    full_post = ' '.join(blog_post_full)
                    del blog_post_full[:]
                    
            except requests.exceptions.HTTPError as err:
                if err.response.status_code >= 400:
                    print "Page not found"
                    #link = ''
                else:
                    raise
        else: 
            continue
                
        text_file.write(full_post)
    text_file.close()


