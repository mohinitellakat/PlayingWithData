# -*- coding: utf-8 -*-
"""
Created on Sun Jun 11 21:26:11 2017

@author: mt34546
"""

#!/usr/bin/python

import requests
#from PIL import Image
#from resizeimage import resizeimage
#from StringIO import StringIO
import os
import urllib2
import csv
import httplib

from fnmatch import fnmatch

images = set()

root = "C:\\Users\\mt34546\\Documents\\UTStuff\\PennebakerLabStuff\\UMich-Summer2017\\test-images-overall"
pattern = "*.jpg"

for path, subdirs, files in os.walk(root):
    for name in files:
        if fnmatch(name, pattern):
            image_file = name
            images.add(image_file)


#C:\Users\mt34546\Documents\UTStuff\PennebakerLabStuff\UMich-Summer2017\img_gender_state.csv


#image_dir = os.listdir("C:\\Users\\mt34546\\Documents\\UTStuff\\PennebakerLabStuff\\UMich-Summer2017\\test-images")
#for image_file in image_dir:
#    images.add(image_file)
    
folder_num = 54

file_path = raw_input("Enter the path of your file: ")

print "got filepath"

with open(file_path, 'rb') as csvfile:

#df = pd.read_csv(file_path)
    csvreader = csv.reader(csvfile, delimiter=',')

    print "got file"
    
    
    
    
#    try:
    for index, row in enumerate(csvreader):
        folder_path = "C:\\Users\\mt34546\\Documents\\UTStuff\\PennebakerLabStuff\\UMich-Summer2017\\test-images-overall\\test-images-" + str(folder_num) + "\\"
    
        if len(os.listdir(folder_path)) > 20000:
            folder_num = folder_num + 1
            folder_path = "C:\\Users\\mt34546\\Documents\\UTStuff\\PennebakerLabStuff\\UMich-Summer2017\\test-images-overall\\test-images-" + str(folder_num) + "\\"
            os.mkdir(folder_path)
        else: 
            folder_path = folder_path
            
        img_lnk = row[5] # image url            
        blog_name = row[3].rsplit('//', 1)[-1][:-1] #blogname
        
        file_name = blog_name + "__image" + str(index) + ".jpg"
      
        try:
            if img_lnk and blog_name != None:
                if file_name not in images:
                    with open(folder_path + file_name,'wb') as f:
                        f.write(urllib2.urlopen(img_lnk).read())
                        f.close()
                    images.add(file_name)
                else:
                    continue

            else: 
                continue            
            
        except requests.exceptions.HTTPError as err:
            if err.response.status_code > 400:
                print "Page not found"
            else:
                raise
                
        except requests.exceptions.ConnectionError as err:
            print "connection refused"
        
        except IOError:
            print "caught this stupid IOError"
        
        except urllib2.HTTPError, x:
            print 'Ignoring', x.code
        
        except ValueError as err:
            if err == "I/O operation on closed file":
                continue
            else:
                print "got a value error"
                
        except (IOError, httplib.HTTPException):
            print "bad status"
        
       

    
#    except requests.exceptions.RequestException: 
#        print "Something's wrong" 
#        print img_lnk
    
#    except IOError as e:
#        pass
    
    #### MISC SHIT
      #            image_request_result = requests.get(img_lnk)
    #            image_request_result.raise_for_status()
    #            content = image_request_result.content
    #            image = Image.open(img_lnk)
    #            if image.height > 700 or image.width > 700: #resize image to be 700px x 700px if it's bigger than that
    #                image = resizeimage.resize_contain(image, [700, 700])
    #            image.save(folder_path + blog_name + "__image" + str(dataset.index(row[:])) + ".jpg", image.format)
    #            file_size = sum(os.path.getsize(folder_path) for folder_path in os.listdir('.') if os.path.isfile(folder_path))
    #            print file_size
    #  and requests.get(img_lnk).status_code != "connection refused"
    
    #                else:
#                    with open(folder_path + blog_name + "__image" + str(index) + ".jpg",'wb') as f:
#                        f.write(urllib2.urlopen(img_lnk).read())
#                        f.close()
#                        continue
#                    urllib.urlretrieve(img_lnk, folder_path + blog_name + "__image" + str(index) + ".jpg")
