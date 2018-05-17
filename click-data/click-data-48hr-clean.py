# -*- coding: utf-8 -*-
"""
Created on Fri Dec 02 15:57:23 2016

@author: mt34546
"""
import pandas as pd
import numpy as np

hours_of_day=( 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39)
#date_marker_list = []

#FALL2015 DATA

#bm_day_zero = ("2015-09-02","2015-09-07","2015-09-09","2015-09-14","2015-09-16","2015-09-21","2015-09-23","2015-09-28",
#               "2015-09-30","2015-10-05","2015-10-07","2015-10-12","2015-10-14","2015-10-19",
#               "2015-10-21","2015-10-26","2015-10-28","2015-11-02",
#               "2015-11-04","2015-11-09","2015-11-11","2015-11-16",
#               "2015-11-18","2015-11-23","2015-11-30","2015-12-02")
#      
#bm_day_one = ("2015-09-03","2015-09-08","2015-09-10","2015-09-15","2015-09-17","2015-09-22","2015-09-24","2015-09-29","2015-10-01","2015-10-06",
#	"2015-10-08","2015-10-13""2015-10-15","2015-10-20","2015-10-22","2015-10-27","2015-10-29","2015-11-03",
#      "2015-11-05","2015-11-10","2015-11-12","2015-11-17","2015-11-19","2015-11-24","2015-12-01","2015-12-03")

#SPRING2016 DATA

bm_day_zero = ("2016-01-27","2016-02-01","2016-02-03","2016-02-08","2016-02-10","2016-02-15","2016-02-17","2016-02-22","2016-02-24",
               "2016-02-29","2016-03-02","2016-03-07","2016-03-09","2016-03-21","2016-03-23","2016-03-28","2016-03-30","2016-04-04",
               "2016-04-06","2016-04-11","2016-04-13","2016-04-18","2016-04-20","2016-04-25","2016-04-27")
               
bm_day_one = ("2016-01-28",
    "2016-02-02","2016-02-04","2016-02-09","2016-02-11",
    "2016-02-16","2016-02-18","2016-02-23","2016-02-25",
    "2016-03-01","2016-03-03","2016-03-08","2016-03-10",
    "2016-03-22","2016-03-24","2016-03-29","2016-03-31",
    "2016-04-05","2016-04-07","2016-04-12","2016-04-14",
    "2016-04-19","2016-04-21","2016-04-26","2016-04-28",
    "2016-05-02","2016-05-03")

file_path = raw_input('Enter your filepath here:')

df = pd.read_csv(file_path)

df['Hour'] = df['Hour'].astype(int)

for i, date in enumerate (df["Date"]):
    if date in bm_day_one:
        df['Hour'][i] = df['Hour'][i] + 24
    else:
        print "moving on"
        
for each_hour in df['Hour'].unique():
    if each_hour in hours_of_day:
        df["ClickHour" + str(each_hour)] = (df['Hour'] == each_hour).astype(int)
    else:
        print "bad time"
        

print "done with date marking" 
print "done with hour assignment"

df1 = df[['eid', 'Hour', 'Benchmark Number', 'Grade', 'Date', 'ClickHour0','ClickHour1','ClickHour2','ClickHour3', 'ClickHour4', 'ClickHour5', 'ClickHour6', 'ClickHour7', 'ClickHour8', 'ClickHour9', 'ClickHour10', 'ClickHour11', 'ClickHour12', 'ClickHour13', 'ClickHour14', 'ClickHour15', 'ClickHour16', 'ClickHour17', 'ClickHour18', 'ClickHour19', 'ClickHour20', 'ClickHour21', 'ClickHour22', 'ClickHour23', 'ClickHour24','ClickHour25','ClickHour26','ClickHour27', 'ClickHour28', 'ClickHour29', 'ClickHour30', 'ClickHour31', 'ClickHour32', 'ClickHour33', 'ClickHour34', 'ClickHour35', 'ClickHour36', 'ClickHour37', 'ClickHour38', 'ClickHour39']]

df1.to_csv('Benchmark_48hr_Spring2016_Data.csv', index=False)