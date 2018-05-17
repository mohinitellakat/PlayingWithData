# -*- coding: utf-8 -*-
"""
Created on Wed Jun 14 12:08:14 2017

@author: mt34546
"""

# -*- coding: utf-8 -*-
"""
Created on Wed May 31 14:19:29 2017

@author: mt34546
"""
#!/usr/bin/python
import MySQLdb
import csv


db = MySQLdb.connect(host="lit06.eecs.umich.edu",    # your host, usually localhost
                     user="blogreader",         # your username
                     passwd="",  # your password
                     db="NAblogs")        # name of the data base
                     
                     

# you must create a Cursor object. It will let
#  you execute all the queries you need
cur = db.cursor()

if cur != None:
    print "connected!"
else:
    print "there's a problem"

# Get cases that have a gender, and state and all the corresponding info

cur.execute("""SELECT a.gender, a.state, b.profile_url, c.blog_url, d.url, d.content
                FROM profiles AS a 
                LEFT OUTER JOIN profiles_blogs AS b ON a.url = b.profile_url
                LEFT OUTER JOIN blogs_posts AS c ON b.blog_url = c.blog_url
                LEFT OUTER JOIN posts AS d ON c.post_url = d.url
                WHERE a.gender IS NOT NULL
                AND a.state IS NOT NULL""")
                

                

dataset = cur.fetchall()
c = csv.writer(open("C:\\Users\\mt34546\\Documents\\UTStuff\\PennebakerLabStuff\\UMich-Summer2017\\text_gender_state.csv","wb"))
for row in dataset:
    c.writerow(row)

print "data acquired"
  
        
db.close()