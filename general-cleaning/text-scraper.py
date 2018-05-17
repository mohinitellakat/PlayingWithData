# -*- coding: utf-8 -*-
"""
Created on Tue Aug 23 15:32:14 2016

@author: Mohini
"""

# -*- coding: utf-8 -*-
"""
Created on Wed Aug 10 14:51:31 2016

Script to create text files from a page


@author: Mohini
"""

import urllib2
from bs4 import BeautifulSoup
import os


resp = urllib2.urlopen('http://w2.vatican.va/content/john-paul-ii/it/speeches.index.html')
soup = BeautifulSoup(resp.read())
uls = soup.find_all('ul', { 'path' : 'speeches' })
for ul in uls:
    links = soup.find_all('a')  #p is an array of all hyperlink tags


#for link in links: # Processing each link and getting the url value
#    if link.parent.name =='b':
#        url = link.get('href')
#        filename = link.contents[0]
#        print filename
#        exclude = set(string.punctuation)
#        filename2  = ''.join(ch for ch in filename if ch not in exclude)
#        print filename2
#        html = urllib2.urlopen(url)
#        soup2 = BeautifulSoup(html.read())
#        texts = soup2.find_all(text=True)
#        with open( "pope-jpii-speeches/" + filename2 + '.txt' , "wb") as code :
#            code.writelines(texts)
#    else:
#        print "bad link"

url_list = []
url_list2 = []
url_list3 = []

##POPE JP II STUFF
for link in links: # Processing each link and getting the url value
    url = link.get('href')
    if "www.vatican.va" in str(url):
        full_url = url
        url_list.append(full_url)
    elif "/contents" in str(url):
        full_url = 'http://w2.vatican.va' + str(url)
        url_list.append(full_url)
    else: 
        print "not a URL"
    
    for url in url_list:
        try:
            speeches_in_yr = urllib2.urlopen(url)
        except urllib2.URLError as e:
            speeches_in_yr = e
        if speeches_in_yr.code in (200, 401):
            print '[{}]: '.format(url), "Up!"
        elif speeches_in_yr.code == 404:
            print '[{}]: '.format(url), "Not Found!" 
    
        soup2 = BeautifulSoup(speeches_in_yr.read())
        links2 = soup2.find_all('a')
        for lnk in links2: 
            if lnk.contents == 'English':
                print "got english version!"
                url2 = lnk.get('href')
                if "www.vatican.va" in str(url2):
                    full_url2 = url2
                    url_list2.append(full_url2)
                elif "/contents" in str(url2):
                    full_url2 = 'http://w2.vatican.va' + str(url2)
                    url_list2.append(full_url2)
                else: 
                    print "not a URL"
                
                for url2 in url_list2:
                    try:
                        english_speeches = urllib2.urlopen(url2)
                    except urllib2.URLError as e:
                        english_speeches = e
                    if english_speeches.code in (200, 401):
                        print '[{}]: '.format(url2), "Up!"
                    elif english_speeches.code == 404:
                        print '[{}]: '.format(url2), "Not Found!" 
                    
                    soup3 = BeautifulSoup(english_speeches.read())
                    links3 = soup3.find_all('a')
                    for lnkk in links3: 
                        url3 = lnkk.get('href')
                        if "www.vatican.va" in str(url3):
                            full_url3 = url3
                            url_list3.append(full_url3)
                        elif "/contents" in str(url3):
                            full_url3 = 'http://w2.vatican.va' + str(url3)
                            url_list3.append(full_url3)
                        else: 
                            print "not a URL"
                        for url3 in url_list3:
                            if ".pdf" in url3:
                                print "we have a pdf!"
                                filename = os.path.basename(url3)
                                print filename
                                data = urllib2.urlopen(url3).read()
                                with open( "pope-jpii-speeches-vatican/" + filename + '.pdf' , "wb") as code :
                                    code.write(data)
                            else:
                                print "not the type of link we want"

    
                    
                                
                    
              