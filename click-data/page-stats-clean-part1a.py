# -*- coding: utf-8 -*-
"""
Created on Mon Nov 28 11:23:06 2016

@author: mt34546
"""

import pandas as pd
import pytz


##TIME BUCKETS
hours_of_day=( 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23)

no_dst_hours=(12, 1, 2)


##DATES FOR CLASS - Comment out everything except the dates for the semester you need

#Fall 2015 Dates for Class
#classdates = ("2015-12-03","2015-12-01","2015-11-24","2015-11-19","2015-11-17","2015-11-12","2015-11-10","2015-11-05","2015-11-03","2015-10-29","2015-10-27","2015-10-22","2015-10-20", 
#	"2015-10-15", "2015-10-13", "2015-10-08", "2015-10-06", "2015-10-01", "2015-09-29", "2015-09-24", "2015-09-22", "2015-09-17", "2015-09-15", "2015-09-10", "2015-09-08", 
#	"2015-09-03", "2015-09-01", "2015-08-27")
#semesterdates = ("2015-08-27","2015-08-28","2015-08-29","2015-08-30","2015-08-31","2015-09-01","2015-09-02","2015-09-03","2015-09-04","2015-09-05","2015-09-06","2015-09-07","2015-09-08",
#	"2015-09-09","2015-09-10","2015-09-11","2015-09-12","2015-09-13","2015-09-14","2015-09-15","2015-09-16","2015-09-17","2015-09-18","2015-09-19","2015-09-20","2015-09-21","2015-09-22",
#	"2015-09-23","2015-09-24","2015-09-25","2015-09-26","2015-09-27","2015-09-28","2015-09-29","2015-09-30","2015-10-01","2015-10-02","2015-10-03","2015-10-04","2015-10-05","2015-10-06",
#	"2015-10-07","2015-10-08","2015-10-09","2015-10-10","2015-10-11","2015-10-12","2015-10-13","2015-10-14","2015-10-15","2015-10-16","2015-10-17","2015-10-18","2015-10-19","2015-10-20",
#	"2015-10-21","2015-10-22","2015-10-23","2015-10-24","2015-10-25","2015-10-26","2015-10-27","2015-10-28","2015-10-29","2015-10-30","2015-10-31","2015-11-01","2015-11-02",
#	"2015-11-03","2015-11-04","2015-11-05","2015-11-06","2015-11-07","2015-11-08","2015-11-09","2015-11-10","2015-11-11","2015-11-12","2015-11-13","2015-11-14","2015-11-15","2015-11-16",
#	"2015-11-17","2015-11-18","2015-11-19","2015-11-20","2015-11-21","2015-11-22","2015-11-23","2015-11-24","2015-11-25","2015-11-26","2015-11-27","2015-11-28","2015-11-29",
#	"2015-11-30","2015-12-01","2015-12-02","2015-12-03","2015-12-04","2015-12-05","2015-12-06","2015-12-07","2015-12-08")

#Spring 2016 Dates for class
classdates = ("2016-1-19", "2016-01-21","2016-01-26","2016-01-28","2016-02-02","2016-02-04",
    "2016-02-09","2016-02-11","2016-02-16","2016-02-18","2016-02-23","2016-02-25", "2016-03-01",
    "2016-03-03", "2016-03-08", "2016-03-10", "2016-03-22", "2016-03-24", "2016-03-29",
    "2016-03-31", "2016-04-05", "2016-04-07", "2016-04-12", "2016-04-14", "2016-04-19",
    "2016-04-21", "2016-04-26", "2016-04-28", "2016-05-03")

semesterdates = ("2016-01-19","2016-01-20","2016-01-21","2016-01-22","2016-01-23","2016-01-24","2016-01-25","2016-01-26","2016-01-27","2016-01-28","2016-01-29","2016-01-30","2016-01-31",
    "2016-02-01","2016-02-02","2016-02-03","2016-02-04","2016-02-05","2016-02-06","2016-02-07","2016-02-08","2016-02-09","2016-02-10","2016-02-11","2016-02-12","2016-02-13",
    "2016-02-14","2016-02-15","2016-02-16","2016-02-17","2016-02-18","2016-02-19","2016-02-20","2016-02-21","2016-02-22","2016-02-23","2016-02-24","2016-02-25","2016-02-26",
    "2016-02-27","2016-02-28","2016-02-29","2016-03-01","2016-03-02","2016-03-03","2016-03-04","2016-03-05","2016-03-06","2016-03-07",
    "2016-03-08","2016-03-09","2016-03-10","2016-03-11","2016-03-12","2016-03-13","2016-03-14",
    "2016-03-15","2016-03-16","2016-03-17","2016-03-18","2016-03-19","2016-03-20","2016-03-21",
    "2016-03-22","2016-03-23","2016-03-24","2016-03-25","2016-03-26","2016-03-27","2016-03-28",
    "2016-03-29","2016-03-30","2016-03-31","2016-04-01","2016-04-02","2016-04-03","2016-04-04",
    "2016-04-05","2016-04-06","2016-04-07","2016-04-08","2016-04-09","2016-04-10","2016-04-11",
    "2016-04-12","2016-04-13","2016-04-14","2016-04-15","2016-04-16","2016-04-17","2016-04-18",
    "2016-04-19","2016-04-20","2016-04-21","2016-04-22","2016-04-23","2016-04-24","2016-04-25",
    "2016-04-26","2016-04-27","2016-04-28","2016-04-29","2016-04-30","2016-05-01","2016-05-02",
    "2016-05-03")


benchmark_num_list = []

file_path = raw_input('Enter your filepath here:')

df = pd.read_csv(file_path)

#FALL 2015 BENCHMARK NUMBER ASSIGNMENT : COMMENT OUT IF DOING SPRING 2016 DATA

#for idx, date in enumerate(df['Date']):
#    if date in semesterdates:
#        if date < '2015-09-03':
#            benchmark_num_list.append(2)
#        elif date == '2015-09-03':
#            if df['Time'][idx] < '15:30:00-00:00':
#                benchmark_num_list.append(2)
#            elif  df['Time'][idx] > '17:00:00-00:00':
#                benchmark_num_list.append(3)
#            else:
#                benchmark_num_list.append(0)
#        elif date < '2015-09-08' and date > '2015-09-03':
#            benchmark_num_list.append(3)
#        elif date == '2015-09-08':
#            if df['Time'][idx] < '15:30:00-00:00':
#                benchmark_num_list.append(3)
#            elif  df['Time'][idx] > '17:00:00-00:00':
#                benchmark_num_list.append(4)
#            else:
#                benchmark_num_list.append(0)
#        elif date < '2015-09-10' and date > '2015-09-08':
#            benchmark_num_list.append(4)
#        elif date == '2015-09-10':
#            if df['Time'][idx] < '15:30:00-00:00':
#                benchmark_num_list.append(4)
#            elif  df['Time'][idx] > '17:00:00-00:00':
#                benchmark_num_list.append(5)
#            else:
#                benchmark_num_list.append(0)
#        elif date < '2015-09-15' and date > '2015-09-10':
#            benchmark_num_list.append(5)
#        elif date == '2015-09-15':
#            if df['Time'][idx] < '15:30:00-00:00':
#                benchmark_num_list.append(5)
#            elif  df['Time'][idx] > '17:00:00-00:00':
#                benchmark_num_list.append(6)
#            else:
#                benchmark_num_list.append(0)
#        elif date < '2015-09-17' and date > '2015-09-15':
#            benchmark_num_list.append(6)
#        elif date == '2015-09-17':
#            if df['Time'][idx] < '15:30:00-00:00':
#                benchmark_num_list.append(6)
#            elif  df['Time'][idx] > '17:00:00-00:00':
#                benchmark_num_list.append(7)
#            else:
#                benchmark_num_list.append(0)
#        elif date < '2015-09-22' and date > '2015-09-17':
#            benchmark_num_list.append(7)
#        elif date == '2015-09-22':
#            if df['Time'][idx] < '15:30:00-00:00':
#                benchmark_num_list.append(7)
#            elif  df['Time'][idx] > '17:00:00-00:00':
#                benchmark_num_list.append(8)
#            else:
#                benchmark_num_list.append(0)
#        elif date < '2015-09-24' and date > '2015-09-22':
#            benchmark_num_list.append(8)
#        elif date == '2015-09-24':
#            if df['Time'][idx] < '15:30:00-00:00':
#                benchmark_num_list.append(8)
#            elif  df['Time'][idx] > '17:00:00-00:00':
#                benchmark_num_list.append(9)
#            else:
#                benchmark_num_list.append(0)
#        elif date < '2015-09-29' and date > '2015-09-24':
#            benchmark_num_list.append(9)
#        elif date == '2015-09-29':
#            if df['Time'][idx] < '15:30:00-00:00':
#                benchmark_num_list.append(9)
#            elif  df['Time'][idx] > '17:00:00-00:00':
#                benchmark_num_list.append(10)
#            else:
#                benchmark_num_list.append(0)
#        elif date < '2015-10-01' and date > '2015-09-29':
#            benchmark_num_list.append(10)
#        elif date == '2015-10-01':
#            if df['Time'][idx] < '15:30:00-00:00':
#                benchmark_num_list.append(10)
#            elif  df['Time'][idx] > '17:00:00-00:00':
#                benchmark_num_list.append(11)
#            else:
#                benchmark_num_list.append(0)
#        elif date < '2015-10-06' and date > '2015-10-01':
#            benchmark_num_list.append(11)
#        elif date == '2015-10-06':
#            if df['Time'][idx] < '15:30:00-00:00':
#                benchmark_num_list.append(11)
#            elif  df['Time'][idx] > '17:00:00-00:00':
#                benchmark_num_list.append(12)
#            else:
#                benchmark_num_list.append(0)
#        elif date < '2015-10-08' and date > '2015-10-06':
#            benchmark_num_list.append(11)
#        elif date == '2015-10-08':
#            if df['Time'][idx] < '15:30:00-00:00':
#                benchmark_num_list.append(12)
#            elif  df['Time'][idx] > '17:00:00-00:00':
#                benchmark_num_list.append(13)
#            else:
#                benchmark_num_list.append(0)
#        elif date < '2015-10-13' and date > '2015-10-08':
#            benchmark_num_list.append(13)
#        elif date == '2015-10-13':
#            if df['Time'][idx] < '15:30:00-00:00':
#                benchmark_num_list.append(13)
#            elif  df['Time'][idx] > '17:00:00-00:00':
#                benchmark_num_list.append(14)
#            else:
#                benchmark_num_list.append(0)
#        elif date < '2015-10-15' and date > '2015-10-13':
#            benchmark_num_list.append(14)
#        elif date == '2015-10-15':
#            if df['Time'][idx] < '15:30:00-00:00':
#                benchmark_num_list.append(14)
#            elif  df['Time'][idx] > '17:00:00-00:00':
#                benchmark_num_list.append(15)
#            else:
#                benchmark_num_list.append(0)
#        elif date < '2015-10-20' and date > '2015-10-15':
#            benchmark_num_list.append(15)
#        elif date == '2015-10-20':
#            if df['Time'][idx] < '15:30:00-00:00':
#                benchmark_num_list.append(15)
#            elif  df['Time'][idx] > '17:00:00-00:00':
#                benchmark_num_list.append(16)
#            else:
#                benchmark_num_list.append(0)
#        elif date < '2015-10-22' and date > '2015-10-20':
#            benchmark_num_list.append(16)
#        elif date == '2015-10-22':
#            if df['Time'][idx] < '15:30:00-00:00':
#                benchmark_num_list.append(16)
#            elif  df['Time'][idx] > '17:00:00-00:00':
#                benchmark_num_list.append(17)
#            else:
#                benchmark_num_list.append(0)
#        elif date < '2015-10-27' and date > '2015-10-22':
#            benchmark_num_list.append(17)
#        elif date == '2015-10-27':
#            if df['Time'][idx] < '15:30:00-00:00':
#                benchmark_num_list.append(17)
#            elif  df['Time'][idx] > '17:00:00-00:00':
#                benchmark_num_list.append(18)
#            else:
#                benchmark_num_list.append(0)
#        elif date < '2015-10-29' and date > '2015-10-27':
#            benchmark_num_list.append(18)
#        elif date == '2015-10-29':
#            if df['Time'][idx] < '15:30:00-00:00':
#                benchmark_num_list.append(18)
#            elif  df['Time'][idx] > '17:00:00-00:00':
#                benchmark_num_list.append(19)
#            else:
#                benchmark_num_list.append(0)
#        elif date < '2015-11-03' and date > '2015-10-29':
#            benchmark_num_list.append(19)
#        elif date == '2015-11-03':
#            if df['Time'][idx] < '15:30:00-00:00':
#                benchmark_num_list.append(19)
#            elif  df['Time'][idx] > '17:00:00-00:00':
#                benchmark_num_list.append(20)
#            else:
#                benchmark_num_list.append(0)
#        elif date < '2015-11-05' and date > '2015-11-03':
#            benchmark_num_list.append(20)
#        elif date == '2015-11-05':
#            if df['Time'][idx] < '15:30:00-00:00':
#                benchmark_num_list.append(20)
#            elif  df['Time'][idx] > '17:00:00-00:00':
#                benchmark_num_list.append(21)
#            else:
#                benchmark_num_list.append(0)
#        elif date < '2015-11-10' and date > '2015-11-05':
#            benchmark_num_list.append(21)
#        elif date == '2015-11-10':
#            if df['Time'][idx] < '15:30:00-00:00':
#                benchmark_num_list.append(21)
#            elif  df['Time'][idx] > '17:00:00-00:00':
#                benchmark_num_list.append(22)
#            else:
#                benchmark_num_list.append(0)
#        elif date < '2015-11-12' and date > '2015-11-10':
#            benchmark_num_list.append(22)
#        elif date == '2015-11-12':
#            if df['Time'][idx] < '15:30:00-00:00':
#                benchmark_num_list.append(22)
#            elif  df['Time'][idx] > '17:00:00-00:00':
#                benchmark_num_list.append(23)
#            else:
#                benchmark_num_list.append(0)
#        elif date < '2015-11-17' and date > '2015-11-12':
#            benchmark_num_list.append(23)
#        elif date == '2015-11-17':
#            if df['Time'][idx] < '15:30:00-00:00':
#                benchmark_num_list.append(23)
#            elif  df['Time'][idx] > '17:00:00-00:00':
#                benchmark_num_list.append(24)
#            else:
#                benchmark_num_list.append(0)
#        elif date < '2015-11-19' and date > '2015-11-17':
#            benchmark_num_list.append(24)
#        elif date == '2015-11-19':
#            if df['Time'][idx] < '15:30:00-00:00':
#                benchmark_num_list.append(24)
#            elif  df['Time'][idx] > '17:00:00-00:00':
#                benchmark_num_list.append(25)
#            else:
#                benchmark_num_list.append(0)
#        elif date < '2015-11-24' and date > '2015-11-19':
#            benchmark_num_list.append(25)
#        elif date == '2015-11-24':
#            if df['Time'][idx] < '15:30:00-00:00':
#                benchmark_num_list.append(25)
#            elif  df['Time'][idx] > '17:00:00-00:00':
#                benchmark_num_list.append(26)
#            else:
#                benchmark_num_list.append(0)
#        elif date < '2015-12-01' and date > '2015-11-24':
#            benchmark_num_list.append(26)
#        elif date == '2015-12-01':
#            if df['Time'][idx] < '15:30:00-00:00':
#                benchmark_num_list.append(26)
#            elif  df['Time'][idx] > '17:00:00-00:00':
#                benchmark_num_list.append(27)
#            else:
#                benchmark_num_list.append(0)
#        elif date < '2015-12-03' and date > '2015-12-01':
#            benchmark_num_list.append(27)
#        elif date == '2015-12-03':
#            if df['Time'][idx] < '15:30:00-00:00':
#                benchmark_num_list.append(27)
#            elif  df['Time'][idx] > '17:00:00-00:00':
#                benchmark_num_list.append(0)
#            else:
#                benchmark_num_list.append(0)
#        elif date > '2015-12-03':
#            benchmark_num_list.append(0)
#        else:
#            benchmark_num_list.append(0)
#    else:
#        benchmark_num_list.append(0)
        
#SPRING 2016 BENCHMARK NUMBER ASSIGNMENT : COMMENT OUT IF DOING FALL 2015 DATA
for idx, date in enumerate(df['Date']):
    if date in semesterdates:
        if date < '2016-01-28':
            benchmark_num_list.append(2)
        elif date == '2016-01-28':
            if df['Time'][idx] < '15:30:00-00:00':
                benchmark_num_list.append(2)
            elif  df['Time'][idx] > '17:00:00-00:00':
                benchmark_num_list.append(3)
            else:
                benchmark_num_list.append(0)
        elif date < '2016-02-02' and date > '2016-01-28':
            benchmark_num_list.append(3)
        elif date == '2016-02-02':
            if df['Time'][idx] < '15:30:00-00:00':
                benchmark_num_list.append(3)
            elif  df['Time'][idx] > '17:00:00-00:00':
                benchmark_num_list.append(4)
            else:
                benchmark_num_list.append(0)
        elif date < '2016-02-04' and date > '2016-02-02':
            benchmark_num_list.append(4)
        elif date == '2016-02-04':
            if df['Time'][idx] < '15:30:00-00:00':
                benchmark_num_list.append(4)
            elif  df['Time'][idx] > '17:00:00-00:00':
                benchmark_num_list.append(5)
            else:
                benchmark_num_list.append(0)
        elif date < '2016-02-09' and date > '2016-02-04':
            benchmark_num_list.append(5)
        elif date == '2016-02-09':
            if df['Time'][idx] < '15:30:00-00:00':
                benchmark_num_list.append(5)
            elif  df['Time'][idx] > '17:00:00-00:00':
                benchmark_num_list.append(6)
            else:
                benchmark_num_list.append(0)
        elif date < '2016-02-11' and date > '2016-02-09':
            benchmark_num_list.append(6)
        elif date == '2016-02-11':
            if df['Time'][idx] < '15:30:00-00:00':
                benchmark_num_list.append(6)
            elif  df['Time'][idx] > '17:00:00-00:00':
                benchmark_num_list.append(7)
            else:
                benchmark_num_list.append(0)
        elif date < '2016-02-16' and date > '2016-02-11':
            benchmark_num_list.append(7)
        elif date == '2016-02-16':
            if df['Time'][idx] < '15:30:00-00:00':
                benchmark_num_list.append(7)
            elif  df['Time'][idx] > '17:00:00-00:00':
                benchmark_num_list.append(8)
            else:
                benchmark_num_list.append(0)
        elif date < '2016-02-18' and date > '2016-02-16':
            benchmark_num_list.append(8)
        elif date == '2016-02-18':
            if df['Time'][idx] < '15:30:00-00:00':
                benchmark_num_list.append(8)
            elif  df['Time'][idx] > '17:00:00-00:00':
                benchmark_num_list.append(9)
            else:
                benchmark_num_list.append(0)
        elif date < '2016-02-23' and date > '2016-02-18':
            benchmark_num_list.append(9)
        elif date == '2016-02-23':
            if df['Time'][idx] < '15:30:00-00:00':
                benchmark_num_list.append(9)
            elif  df['Time'][idx] > '17:00:00-00:00':
                benchmark_num_list.append(10)
            else:
                benchmark_num_list.append(0)
        elif date < '2016-02-25' and date > '2016-02-23':
            benchmark_num_list.append(10)
        elif date == '2016-02-25':
            if df['Time'][idx] < '15:30:00-00:00':
                benchmark_num_list.append(10)
            elif  df['Time'][idx] > '17:00:00-00:00':
                benchmark_num_list.append(11)
            else:
                benchmark_num_list.append(0)
        elif date < '2016-03-01' and date > '2016-02-25':
            benchmark_num_list.append(11)
        elif date == '2016-03-01':
            if df['Time'][idx] < '15:30:00-00:00':
                benchmark_num_list.append(11)
            elif  df['Time'][idx] > '17:00:00-00:00':
                benchmark_num_list.append(12)
            else:
                benchmark_num_list.append(0)
        elif date < '2016-03-03' and date > '2016-03-01':
            benchmark_num_list.append(12)
        elif date == '2016-03-03':
            if df['Time'][idx] < '15:30:00-00:00':
                benchmark_num_list.append(12)
            elif  df['Time'][idx] > '17:00:00-00:00':
                benchmark_num_list.append(13)
            else:
                benchmark_num_list.append(0)
        elif date < '2016-03-08' and date > '2016-03-03':
            benchmark_num_list.append(13)
        elif date == '2016-03-08':
            if df['Time'][idx] < '15:30:00-00:00':
                benchmark_num_list.append(13)
            elif  df['Time'][idx] > '17:00:00-00:00':
                benchmark_num_list.append(14)
            else:
                benchmark_num_list.append(0)
        elif date < '2016-03-10' and date > '2016-03-08':
            benchmark_num_list.append(14)
        elif date == '2016-03-10':
            if df['Time'][idx] < '15:30:00-00:00':
                benchmark_num_list.append(14)
            elif  df['Time'][idx] > '17:00:00-00:00':
                benchmark_num_list.append(15)
            else:
                benchmark_num_list.append(0)
        elif date < '2016-03-22' and date > '2016-03-10':
            benchmark_num_list.append(15)
        elif date == '2016-03-22':
            if df['Time'][idx] < '15:30:00-00:00':
                benchmark_num_list.append(15)
            elif  df['Time'][idx] > '17:00:00-00:00':
                benchmark_num_list.append(16)
            else:
                benchmark_num_list.append(0)
        elif date < '2016-03-24' and date > '2016-03-22':
            benchmark_num_list.append(16)
        elif date == '2016-03-24':
            if df['Time'][idx] < '15:30:00-00:00':
                benchmark_num_list.append(16)
            elif  df['Time'][idx] > '17:00:00-00:00':
                benchmark_num_list.append(17)
            else:
                benchmark_num_list.append(0)
        elif date < '2016-03-29' and date > '2016-03-24':
            benchmark_num_list.append(17)
        elif date == '2016-03-29':
            if df['Time'][idx] < '15:30:00-00:00':
                benchmark_num_list.append(17)
            elif  df['Time'][idx] > '17:00:00-00:00':
                benchmark_num_list.append(18)
            else:
                benchmark_num_list.append(0)
        elif date < '2016-03-31' and date > '2016-03-29':
            benchmark_num_list.append(18)
        elif date == '2016-03-31':
            if df['Time'][idx] < '15:30:00-00:00':
                benchmark_num_list.append(18)
            elif  df['Time'][idx] > '17:00:00-00:00':
                benchmark_num_list.append(19)
            else:
                benchmark_num_list.append(0)
        elif date < '2016-04-05' and date > '2016-03-31':
            benchmark_num_list.append(19)
        elif date == '2016-04-05':
            if df['Time'][idx] < '15:30:00-00:00':
                benchmark_num_list.append(19)
            elif  df['Time'][idx] > '17:00:00-00:00':
                benchmark_num_list.append(20)
            else:
                benchmark_num_list.append(0)
        elif date < '2016-04-07' and date > '2016-04-05':
            benchmark_num_list.append(20)
        elif date == '2016-04-07':
            if df['Time'][idx] < '15:30:00-00:00':
                benchmark_num_list.append(20)
            elif  df['Time'][idx] > '17:00:00-00:00':
                benchmark_num_list.append(21)
            else:
                benchmark_num_list.append(0)
        elif date < '2016-04-12' and date > '2016-04-07':
            benchmark_num_list.append(21)
        elif date == '2016-04-12':
            if df['Time'][idx] < '15:30:00-00:00':
                benchmark_num_list.append(21)
            elif  df['Time'][idx] > '17:00:00-00:00':
                benchmark_num_list.append(22)
            else:
                benchmark_num_list.append(0)
        elif date < '2016-04-14' and date > '2016-04-12':
            benchmark_num_list.append(22)
        elif date == '2016-04-14':
            if df['Time'][idx] < '15:30:00-00:00':
                benchmark_num_list.append(22)
            elif  df['Time'][idx] > '17:00:00-00:00':
                benchmark_num_list.append(23)
            else:
                benchmark_num_list.append(0)
        elif date < '2016-04-19' and date > '2016-04-14':
            benchmark_num_list.append(23)
        elif date == '2016-04-19':
            if df['Time'][idx] < '15:30:00-00:00':
                benchmark_num_list.append(23)
            elif  df['Time'][idx] > '17:00:00-00:00':
                benchmark_num_list.append(24)
            else:
                benchmark_num_list.append(0)
        elif date < '2016-04-21' and date > '2016-04-19':
            benchmark_num_list.append(24)
        elif date == '2016-04-21':
            if df['Time'][idx] < '15:30:00-00:00':
                benchmark_num_list.append(24)
            elif  df['Time'][idx] > '17:00:00-00:00':
                benchmark_num_list.append(25)
            else:
                benchmark_num_list.append(0)
        elif date < '2016-04-26' and date > '2016-04-21':
            benchmark_num_list.append(25)
        elif date == '2016-04-26':
            if df['Time'][idx] < '15:30:00-00:00':
                benchmark_num_list.append(25)
            elif  df['Time'][idx] > '17:00:00-00:00':
                benchmark_num_list.append(26)
            else:
                benchmark_num_list.append(0)
        elif date < '2016-04-28' and date > '2016-04-26':
            benchmark_num_list.append(26)
        elif date == '2016-04-28':
            if df['Time'][idx] < '15:30:00-00:00':
                benchmark_num_list.append(26)
            elif  df['Time'][idx] > '17:00:00-00:00':
                benchmark_num_list.append(27)
            else:
                benchmark_num_list.append(0)
        elif date < '2016-05-03' and date > '2016-04-28':
            benchmark_num_list.append(27)
        elif date == '2016-05-03':
            if df['Time'][idx] < '15:30:00-00:00':
                benchmark_num_list.append(27)
            elif  df['Time'][idx] > '17:00:00-00:00':
                benchmark_num_list.append(0)
            else:
                benchmark_num_list.append(0)
        elif date > '2016-05-03':
            benchmark_num_list.append(0)
        else:
            benchmark_num_list.append(0)
    else:
        benchmark_num_list.append(0)
            

df['Benchmark Number'] = benchmark_num_list

print "done with benchmark number assignment"

df.to_csv('ps-data-clean/page_stats_where_intermediate_Spring2016.csv', index=False)