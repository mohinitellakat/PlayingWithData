# -*- coding: utf-8 -*-
"""
Created on Thu Nov 03 12:20:35 2016

@author: mt34546
"""

import pandas as pd

#Fall 2015 Dates for Class
classdates = ("2015-12-03","2015-12-01","2015-11-24","2015-11-19","2015-11-17","2015-11-12","2015-11-10","2015-11-05","2015-11-03","2015-10-29","2015-10-27","2015-10-22","2015-10-20", 
	"2015-10-15", "2015-10-13", "2015-10-08", "2015-10-06", "2015-10-01", "2015-09-29", "2015-09-24", "2015-09-22", "2015-09-17", "2015-09-15", "2015-09-10", "2015-09-08", 
	"2015-09-03")

#Spring 2016 Dates for class
#classdates = ("2016-1-19", "2016-01-21","2016-01-26","2016-01-28","2016-02-02","2016-02-04",
#    "2016-02-09","2016-02-11","2016-02-16","2016-02-18","2016-02-23","2016-02-25", "2016-03-01",
#    "2016-03-03", "2016-03-08", "2016-03-10", "2016-03-22", "2016-03-24", "2016-03-29",
#    "2016-03-31", "2016-04-05", "2016-04-07", "2016-04-12", "2016-04-14", "2016-04-19",
#    "2016-04-21", "2016-04-26", "2016-04-28", "2016-05-03")

date_list = []

file_path = raw_input('Enter your filepath here:')

df = pd.read_csv(file_path)   

#FALL 2015 DATA ** COMMENT OUT WHEN DOING SPRING 2016 DATA
for bm_num in df['Benchmark Number']:
    if bm_num == 2:
        date_list.append("2015-09-03")
    elif bm_num == 3:
        date_list.append("2015-09-08")
    elif bm_num == 4:
        date_list.append("2015-09-10")
    elif bm_num == 5:
        date_list.append("2015-09-15")
    elif bm_num == 6:
        date_list.append("2015-09-17")
    elif bm_num == 7:
        date_list.append("2015-09-22")
    elif bm_num == 8:
        date_list.append("2015-09-24")
    elif bm_num == 9:
        date_list.append("2015-09-29")
    elif bm_num == 10:
        date_list.append("2015-10-01")
    elif bm_num == 11:
        date_list.append("2015-10-06")
    elif bm_num == 12:
        date_list.append("2015-10-08")
    elif bm_num == 13:
        date_list.append("2015-10-13")
    elif bm_num == 14:
        date_list.append("2015-10-15")
    elif bm_num == 15:
        date_list.append("2015-10-20")
    elif bm_num == 16:
        date_list.append("2015-10-22")
    elif bm_num == 17:
        date_list.append("2015-10-27")
    elif bm_num == 18:
        date_list.append("2015-10-29")
    elif bm_num == 19:
        date_list.append("2015-11-03")
    elif bm_num == 20:
        date_list.append("2015-11-05")
    elif bm_num == 21:
        date_list.append("2015-11-10")
    elif bm_num == 22:
        date_list.append("2015-11-12")
    elif bm_num == 23:
        date_list.append("2015-11-17")
    elif bm_num == 24:
        date_list.append("2015-11-19")
    elif bm_num == 25:
        date_list.append("2015-11-24")
    elif bm_num == 26:
        date_list.append("2015-12-01")
    elif bm_num == 27:
        date_list.append("2015-12-03")
    else:
        date_list.append("0")
        

#SPRING 2016 DATA ** COMMENT OUT WHEN DOING FALL 2015 DATA
#for bm_num in df['Benchmark Number']:
#    if bm_num == 2:
#        date_list.append("2016-01-28")
#    elif bm_num == 3:
#        date_list.append("2016-02-02")
#    elif bm_num == 4:
#        date_list.append("2016-02-04")
#    elif bm_num == 5:
#        date_list.append("2016-02-09")
#    elif bm_num == 6:
#        date_list.append("2016-02-11")
#    elif bm_num == 7:
#        date_list.append("2016-02-16")
#    elif bm_num == 8:
#        date_list.append("2016-02-18")
#    elif bm_num == 9:
#        date_list.append("2016-02-23")
#    elif bm_num == 10:
#        date_list.append("2016-02-25")
#    elif bm_num == 11:
#        date_list.append("2016-03-01")
#    elif bm_num == 12:
#        date_list.append("2016-03-03")
#    elif bm_num == 13:
#        date_list.append("2016-03-08")
#    elif bm_num == 14:
#        date_list.append("2016-03-10")
#    elif bm_num == 15:
#        date_list.append("2016-03-22")
#    elif bm_num == 16:
#        date_list.append("2016-03-24")
#    elif bm_num == 17:
#        date_list.append("2016-03-29")
#    elif bm_num == 18:
#        date_list.append("2016-03-31")
#    elif bm_num == 19:
#        date_list.append("2016-04-05")
#    elif bm_num == 20:
#        date_list.append("2016-04-07")
#    elif bm_num == 21:
#        date_list.append("2016-04-12")
#    elif bm_num == 22:
#        date_list.append("2016-04-14")
#    elif bm_num == 23:
#        date_list.append("2016-04-19")
#    elif bm_num == 24:
#        date_list.append("2016-04-21")
#    elif bm_num == 25:
#        date_list.append("2016-04-26")
#    elif bm_num == 26:
#        date_list.append("2016-04-28")
#    elif bm_num == 27:
#        date_list.append("2016-05-03")
#    else:
#        date_list.append("0")

df['Date Benchmark'] = date_list

df.to_csv('click-data-for-MLM-Fall2015.csv', index=False)
   