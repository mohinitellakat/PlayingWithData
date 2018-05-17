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


file_path = raw_input('Enter your filepath here:')

df = pd.read_csv(file_path)


transcript = []

for link in df['transcript_url']:
    
    file_name = link[26:-23]
    with open('C:\\Users\\mt34546\\Documents\\UTStuff\\PennebakerLabStuff\\TEDTalks\\transcripts\\' + file_name + '_transcript.txt', 'w') as text_file:
        try:
            
            resp = requests.get(link, headers = {'User-agent': 'your bot 0.1'})
            resp.raise_for_status()
            content = resp.content
            #resp = urllib2.urlopen(link)
            soup = BeautifulSoup(content.decode('utf-8', 'ignore'))
            temp1 = soup.find_all('span', { 'class' : 'talk-transcript__fragment' })
            for temp in temp1:
                text_byte = temp.text
                encoded_text_byte = u''.join(text_byte).encode('utf-8').strip()
                encoded_text_byte = encoded_text_byte.replace('\n', ' ').replace('\\' , '').replace('\xe2\x80\x94', '').replace(',', '').replace('"', '')

                regex_encoded_tb = re.sub(r'\([^)]*\)', '', encoded_text_byte)
                
                transcript.append(' ' + regex_encoded_tb)
                
            full_transcript = ' '.join(transcript)
            del transcript[:]
            
        except requests.exceptions.HTTPError as err:
            if err.response.status_code == 404:
                print "Page not found"
                full_transcript = ''
            else:
                raise
                
        text_file.write(full_transcript)
    text_file.close()

