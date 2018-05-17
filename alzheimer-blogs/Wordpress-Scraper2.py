# -*- coding: utf-8 -*-
"""
Created on Mon Jul 17 15:15:57 2017

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

page_urls = []
post_urls = []
blog_post_full = []

main_link = 'http://rawarrior.com/'
pagenum = 2

page_urls.append(main_link)

while (pagenum < 68):
    new_link = str(main_link) + 'page/' + str(pagenum) + '/'
    page_urls.append(new_link)
    pagenum = pagenum + 1
    print new_link
pagenum = 2

for page in page_urls:
    try:       
        resp = requests.get(page, headers = {'User-agent': 'your bot 0.1'})
        resp.raise_for_status()
        content = resp.content
        soup = BeautifulSoup(content.decode('utf-8', 'ignore'))
        big_container = soup.find_all('div', {'id' : 'content'})
        for pt in big_container:
            headers = pt.find_all('h2', {'class': 'title'})
            for header in headers:
                article_links = header.find_all('a', href=True)
                for lnk in article_links:
                    post_urls.append(lnk.get('href'))
    
        
    except requests.exceptions.HTTPError as err:
        if err.response.status_code > 400:
            print "Page not found"
            link = ''
        else:
            raise
            
print len(post_urls)
print post_urls


#write posts to text files
           
for post in post_urls:
    #url = post
    file_name_pt1 = post[21:]
    #file_name_pt2 = post[28:]
    file_name = file_name_pt1.replace('/', '-')
#    file_name = file_name.replace('?', '-')
#    file_name = file_name.replace('=', '-')
    #file_name= file_name_pt1 + file_name_pt2
    #print post
    with open('C:\\Users\\mt34546\\Dropbox\\GradSchoolStuff(UT)\\rheumatoid-arthritis-blogs\\rawarrior-blogposts\\' + file_name + '.txt', 'w') as text_file:
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


