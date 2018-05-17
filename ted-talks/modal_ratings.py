# -*- coding: utf-8 -*-
"""
Created on Tue Mar 07 10:00:21 2017

@author: mt34546
"""

from bs4 import BeautifulSoup
import pandas as pd
import requests
from lxml import html


file_path = raw_input('Enter your filepath here:')

df = pd.read_csv(file_path)

for link in df['VideoURL']:

    resp = requests.get(link)
#    content = resp.content
    tree = html.fromstring(resp.content)
    cool_text = tree.xpath('//span[@class="talk-rating__result__name"]/text()')
    
    print cool_text
    
#    soup = BeautifulSoup(content.decode('utf-8', 'ignore'))
#    bsid = soup.find('a', { 'class' : 'player-hero__tools__tool rate-button hide-on-fallback' })
#    if bsid:
#        rating_link = bsid.find('a href')
#        print rating_link