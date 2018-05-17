# -*- coding: utf-8 -*-
"""
Created on Wed Aug 10 14:51:31 2016

Script to download PDFs from a page

#basics borrowed from an awesome person on stackoverflow

@author: Mohini
"""

import urllib2
from bs4 import BeautifulSoup
import os

resp = urllib2.urlopen('https://www.justice.gov/ag/speeches-7')
soup = BeautifulSoup(resp.read())
links = soup.find_all('a')  #p is an array of all hyperlink tags


for link in links: # Processing each link and getting the url value
    url = link.get('href')
    print url
    print type(url)
    if (type(url) is str) == True:
        if "http://" in url:
            if ".pdf" in url:
                filename = os.path.basename(url)
                print filename
                data = urllib2.urlopen(url).read()
                with open( "janet-reno-speeches/" + filename , "wb") as code :
                    code.write(data)
            else:
                print "not the type of link we want"
        else:
            print "broken link"
    else:
        print "Type won't work"

#            
       