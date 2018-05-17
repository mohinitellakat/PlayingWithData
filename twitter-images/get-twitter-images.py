# -*- coding: utf-8 -*-
"""
Created on Wed May 24 12:10:28 2017

@author: mt34546
"""

import requests
import urllib
from bs4 import BeautifulSoup
import pandas as pd
import os
from shutil import copyfileobj

def return_url_list(txtf):
    urllist = []
    for txtln in txtf:
        if "https" in txtln:
            txtln=txtln.rstrip()
            words = txtln.split(' ')
            #print words
            for word in words:
                if  "https://" in word:
                    urllist.append(word)
                else:
                    continue
    return urllist
    

imageurls = []

folder_path = raw_input("Enter the path of your folder: ")

twitter_user_files = [twitter_user_file for twitter_user_file in os.listdir(folder_path) if twitter_user_file.endswith('.txt')]

for twitter_user_file in twitter_user_files:

    txtfile = open(os.path.join(folder_path, twitter_user_file), 'r')
    username = twitter_user_file[:-4]
    
    mediaurls = return_url_list(txtfile)
    
 
    for lnk in mediaurls:
        try:  
            resp = requests.get(lnk, headers = {'User-agent': 'your bot 0.1'})
            resp.raise_for_status()
            content = resp.content
            soup = BeautifulSoup(content.decode('utf-8', 'ignore'))
            temp1 = soup.find_all('div', { 'data-image-url' : True })
            for temp in temp1:
                imageurls.append(temp['data-image-url'])    
    
            for img in imageurls:
                if not os.path.exists("C:\\Users\\mt34546\\Documents\\UTStuff\\PennebakerLabStuff\\Twitter\\2016-07-01 - Old Data with Associated Info\\imgs\\" + username):
                    os.makedirs("C:\\Users\\mt34546\\Documents\\UTStuff\\PennebakerLabStuff\\Twitter\\2016-07-01 - Old Data with Associated Info\\imgs\\" + username)
                urllib.urlretrieve(img, "C:\\Users\\mt34546\\Documents\\UTStuff\\PennebakerLabStuff\\Twitter\\2016-07-01 - Old Data with Associated Info\\imgs\\" + username + "\\image_" + username + "_" + str(imageurls.index(img)) +  ".jpg")

            del imageurls[:]
                    
        except requests.exceptions.HTTPError as err:
            if err.response.status_code > 400:
                print "Page not found"
            else:
                raise
        except requests.exceptions.ConnectionError:
            resp.status_code = "Connection refused"

    del mediaurls[:]

                    