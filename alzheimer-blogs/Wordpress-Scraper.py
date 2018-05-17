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

#import time
#
#from selenium import webdriver
#from selenium.webdriver.common.keys import Keys
#
#browser = webdriver.Chrome()
#
#browser.get("https://kateswaffer.com/daily-blog/")
#time.sleep(1)
#
#elem = browser.find_element_by_tag_name("a")
#
#no_of_pagedowns = 1200
#
#while no_of_pagedowns:
#    elem.send_keys(Keys.PAGE_DOWN)
#    time.sleep(0.2)
#    no_of_pagedowns-=1
#
#post_elems = browser.find_elements_by_class_name("post-item-title")
#
#for post in post_elems:
#    print post.get_attribute("href")




post_urls = []
month_urls = []
new_month_urls = []
blog_post_full = []

ks_link = "https://livingwithra.wordpress.com/"

#get the month urls from the homepage
try:
            
    resp = requests.get(ks_link, headers = {'User-agent': 'your bot 0.1'})
    resp.raise_for_status()
    content = resp.content
    soup = BeautifulSoup(content.decode('utf-8', 'ignore'))
    dropdown = soup.find_all('select', {'name' : 'archive-dropdown'})
    for dd in dropdown:
        dd_options = soup.find_all('option')
        for option in dd_options:
            month_urls.append(option.get('value'))

    
except requests.exceptions.HTTPError as err:
    if err.response.status_code == 404:
        print "Page not found"
        link = ''
    else:
        raise
        
print len(month_urls)
        
#testing pages urls for the months
pagenum = 2

for mu in month_urls: 
    if mu != '':
        while (pagenum < 10):
            new_mu = str(mu) + 'page/' + str(pagenum)
            new_month_urls.append(new_mu)
            pagenum = pagenum + 1
        pagenum = 2
    else:
        continue
    
print len(new_month_urls)   
    
month_urls_merged = month_urls + new_month_urls

print len (month_urls_merged)

# go through month urls to get the post urls
for month in month_urls_merged:
    if month != '':
        try:
            resp2 = requests.get(month, headers = {'User-agent': 'your bot 0.1'})
            resp2.raise_for_status()
            content = resp2.content
            soup2 = BeautifulSoup(content.decode('utf-8', 'ignore'))
    
            temp1 = soup2.find_all('div', { 'id' : 'content-main' })
            for temp in temp1:
#                temp2 = temp.find_all('article')
#                for tmp in temp2:
                temp3 = temp.find_all('h2')
                for supertmp in temp3:
                    links = supertmp.find_all('a', href=True)
                    for link in links:
                        post_urls.append(link.get('href'))
        except requests.exceptions.HTTPError as err:
            if err.response.status_code == 404:
                print "Page not found"
                link = ''
            else:
                raise
    else:
        continue

print len(post_urls)

#write posts to text files
           
for post in post_urls:
    url = post.rsplit('/', 1)[0]
    file_name_pt1 = url[33:]
    file_name = file_name_pt1.replace('/', '-')
    
    with open('C:\\Users\\mt34546\\Dropbox\\GradSchoolStuff(UT)\\rheumatoid-arthritis-blogs\\livingwithra-blogposts\\' + file_name + '.txt', 'w') as text_file:
        try:
            resp3 = requests.get(post, headers = {'User-agent': 'your bot 0.1'})
            resp3.raise_for_status()
            content = resp3.content
            soup3 = BeautifulSoup(content.decode('utf-8', 'ignore'))

            temp1 = soup3.find_all('div', { 'class' : 'entry' })
            for temp in temp1:
                temp2 = temp.find_all('p')
                for tmp in temp2:
                    post_text = tmp.text
                    encoded_post_text = u''.join(post_text).encode('utf-8').strip()
                    
                    blog_post_full.append(' ' + encoded_post_text)
                    
                full_post = ' '.join(blog_post_full)
                del blog_post_full[:]
                
        except requests.exceptions.HTTPError as err:
            if err.response.status_code == 404:
                print "Page not found"
                link = ''
            else:
                raise
                
        text_file.write(full_post)
    text_file.close()


