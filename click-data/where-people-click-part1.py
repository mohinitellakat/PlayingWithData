# -*- coding: utf-8 -*-
"""
Created on Mon Jul 17 20:24:46 2017

@author: mt34546
"""

# -*- coding: utf-8 -*-
"""
Created on Fri Dec 02 15:57:23 2016

@author: mt34546
"""
import pandas as pd
import numpy as np
import datetime

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

bm_day_zero = ("1/27/2016","2/1/2016","2/3/2016","2/8/2016","2/10/2016","2/15/2016","2/17/2016","2/22/2016","2/24/2016",
               "2/29/2016","3/2/2016","3/7/2016","3/9/2016","3/21/2016","3/23/2016","3/28/2016","3/30/2016","4/4/2016",
               "4/6/2016","4/11/2016","4/13/2016","4/18/2016","4/20/2016","4/25/2016","4/27/2016")
               
bm_day_one = ("1/28/2016",
    "2/2/2016","2/4/2016","2/9/2016","2/11/2016",
    "2/16/2016","2/18/2016","2/23/2016","2/25/2016",
    "3/1/2016","3/3/2016","3/8/2016","3/10/2016",
    "3/22/2016","3/24/2016","3/29/2016","3/31/2016",
    "4/5/2016","4/7/2016","4/12/2016","4/14/2016",
    "4/19/2016","4/21/2016","4/26/2016","4/28/2016",
    "5/2/2016","5/3/2016")

file_path = raw_input('Enter your filepath here:') #C:\Users\mt34546\Documents\UTStuff\PennebakerLabStuff\Click Data\Final Base Data\click-data-full-Fall2015-lp.csv
#C:\Users\mt34546\Documents\UTStuff\PennebakerLabStuff\Click Data\Final Base Data\click-data-full-Spring2016-lp.csv

df = pd.read_csv(file_path)

df = df.rename(columns = {'\xef\xbb\xbfeid':'eid'})

#for date in df['Date']:
#    date = str(datetime.datetime.strptime(date, '%m/%d/%Y').strftime('%Y-%m-%d'))
#    
#
#df['Date'] = df['Date'].astype(str)        
df['Hour'] = df['Hour'].astype(int)

for hr in hours_of_day:
    df['OfficeHourClicks_' + str(hr)] = np.nan
    df['OtherAssignmentClicks_' + str(hr)]= np.nan
    df['GradeClicks_' + str(hr)] = np.nan
    df['ClassMaterialClicks_' + str(hr)] = np.nan
    df['BenchmarkClicks_' + str(hr)] = np.nan   
    df['OtherClicks_' + str(hr)] = np.nan
    df["ClickHour" + str(hr)] = np.nan

print "done making new columns for where"


for i, date in enumerate (df["Date"]):
    if date in bm_day_one:
        #df['Hour'][i] = df['Hour'][i] + 24
        df.set_value(i, 'Hour', (df['Hour'][i] + 24))
    else:
        continue
        
print "done changing hours"
        
for each_hour in df['Hour'].unique():
    if each_hour in hours_of_day:
        df["ClickHour" + str(each_hour)] = (df['Hour'] == each_hour).astype(int)
    else:
        print "bad time"
        
print "done with date marking" 
print "done with hour assignment"

print list(df.columns.values)
        
for i, each_hour in enumerate (df['Hour']):
    
    if each_hour in hours_of_day and df['URLOfficeHours'][i] == 1:
        df.set_value(i, ('OfficeHourClicks_' + str(each_hour)), 1)
        #df['OfficeHourClicks_' + str(each_hour)][df.URLOfficeHours == 1] = 1
    else:
        df.set_value(i, ('OfficeHourClicks_' + str(each_hour)), 0)
        #df.loc[i, ('OfficeHourClicks_' + str(each_hour))] = 0
        
    if each_hour in hours_of_day and df['URLOtherAssignments'][i] == 1:
        df.set_value(i, ('OtherAssignmentClicks_' + str(each_hour)), 1)
        #df.loc[i, ('OtherAssignmentClicks_' + str(each_hour))] = 1
    else:
        df.set_value(i, ('OtherAssignmentClicks_' + str(each_hour)), 0)
        #df.loc[i, ('OtherAssignmentClicks_' + str(each_hour))] = 0
        
    if each_hour in hours_of_day and df['URLGrades'][i] == 1:
        df.set_value(i, ('GradeClicks_' + str(each_hour)), 1)
        #df.loc[i, ('GradeClicks_' + str(each_hour))] = 1
    else:
        df.set_value(i, ('GradeClicks_' + str(each_hour)), 0)
        #df.loc[i, ('GradeClicks_' + str(each_hour))] = 0
        
    if each_hour in hours_of_day and df['URLClassMaterials'][i] == 1:
        df.set_value(i, ('ClassMaterialClicks_' + str(each_hour)), 1)
        #df.loc[i, ('ClassMaterialClicks_' + str(each_hour))] = 1
    else:
        df.set_value(i, ('ClassMaterialClicks_' + str(each_hour)), 0)
        #df.loc[i, ('ClassMaterialClicks_' + str(each_hour))] = 0
        
    if each_hour in hours_of_day and df['URLBenchmarks'][i] == 1:
        df.set_value(i, ('BenchmarkClicks_' + str(each_hour)), 1)
        #df.loc[i, ('BenchmarkClicks_' + str(each_hour))] = 1
    else:
        df.set_value(i, ('BenchmarkClicks_' + str(each_hour)), 0)
        #df.loc[i, ('BenchmarkClicks_' + str(each_hour))] = 0    
        
    if each_hour in hours_of_day and df['URLOther'][i] == 1:
        df.set_value(i, ('OtherClicks_' + str(each_hour)), 1)
        #df.loc[i, ('OtherClicks_' + str(each_hour))] = 1
    else:
        df.set_value(i, ('OtherClicks_' + str(each_hour)), 0)
        #df.loc[i, ('OtherClicks_' + str(each_hour))] = 0 


        
print 'done with where clicks per hour'


df1 = df[['eid', 'Hour', 'BenchmarkNumber', 'Grade', 'Date', 'ClickHour0','ClickHour1','ClickHour2','ClickHour3', 'ClickHour4', 'ClickHour5', 'ClickHour6', 'ClickHour7', 'ClickHour8', 'ClickHour9', 'ClickHour10', 'ClickHour11', 'ClickHour12', 'ClickHour13', 'ClickHour14', 'ClickHour15', 'ClickHour16', 'ClickHour17', 'ClickHour18', 'ClickHour19', 'ClickHour20', 'ClickHour21', 'ClickHour22', 'ClickHour23', 'ClickHour24','ClickHour25','ClickHour26','ClickHour27', 'ClickHour28', 'ClickHour29', 'ClickHour30', 'ClickHour31', 'ClickHour32', 'ClickHour33', 'ClickHour34', 'ClickHour35', 'ClickHour36', 'ClickHour37', 'ClickHour38', 'ClickHour39',
'OfficeHourClicks_0','OfficeHourClicks_1','OfficeHourClicks_2','OfficeHourClicks_3', 'OfficeHourClicks_4', 'OfficeHourClicks_5', 'OfficeHourClicks_6', 'OfficeHourClicks_7', 'OfficeHourClicks_8', 'OfficeHourClicks_9', 'OfficeHourClicks_10', 'OfficeHourClicks_11', 'OfficeHourClicks_12', 'OfficeHourClicks_13', 'OfficeHourClicks_14', 'OfficeHourClicks_15', 'OfficeHourClicks_16', 'OfficeHourClicks_17', 'OfficeHourClicks_18', 'OfficeHourClicks_19', 'OfficeHourClicks_20', 'OfficeHourClicks_21', 'OfficeHourClicks_22', 'OfficeHourClicks_23', 'OfficeHourClicks_24','OfficeHourClicks_25','OfficeHourClicks_26','OfficeHourClicks_27', 'OfficeHourClicks_28', 'OfficeHourClicks_29', 'OfficeHourClicks_30', 'OfficeHourClicks_31', 'OfficeHourClicks_32', 'OfficeHourClicks_33', 'OfficeHourClicks_34', 'OfficeHourClicks_35', 'OfficeHourClicks_36', 'OfficeHourClicks_37', 'OfficeHourClicks_38', 'OfficeHourClicks_39',
'OtherAssignmentClicks_0','OtherAssignmentClicks_1','OtherAssignmentClicks_2','OtherAssignmentClicks_3', 'OtherAssignmentClicks_4', 'OtherAssignmentClicks_5', 'OtherAssignmentClicks_6', 'OtherAssignmentClicks_7', 'OtherAssignmentClicks_8', 'OtherAssignmentClicks_9', 'OtherAssignmentClicks_10', 'OtherAssignmentClicks_11', 'OtherAssignmentClicks_12', 'OtherAssignmentClicks_13', 'OtherAssignmentClicks_14', 'OtherAssignmentClicks_15', 'OtherAssignmentClicks_16', 'OtherAssignmentClicks_17', 'OtherAssignmentClicks_18', 'OtherAssignmentClicks_19', 'OtherAssignmentClicks_20', 'OtherAssignmentClicks_21', 'OtherAssignmentClicks_22', 'OtherAssignmentClicks_23', 'OtherAssignmentClicks_24','OtherAssignmentClicks_25','OtherAssignmentClicks_26','OtherAssignmentClicks_27', 'OtherAssignmentClicks_28', 'OtherAssignmentClicks_29', 'OtherAssignmentClicks_30', 'OtherAssignmentClicks_31', 'OtherAssignmentClicks_32', 'OtherAssignmentClicks_33', 'OtherAssignmentClicks_34', 'OtherAssignmentClicks_35', 'OtherAssignmentClicks_36', 'OtherAssignmentClicks_37', 'OtherAssignmentClicks_38', 'OtherAssignmentClicks_39',
'GradeClicks_0','GradeClicks_1','GradeClicks_2','GradeClicks_3', 'GradeClicks_4', 'GradeClicks_5', 'GradeClicks_6', 'GradeClicks_7', 'GradeClicks_8', 'GradeClicks_9', 'GradeClicks_10', 'GradeClicks_11', 'GradeClicks_12', 'GradeClicks_13', 'GradeClicks_14', 'GradeClicks_15', 'GradeClicks_16', 'GradeClicks_17', 'GradeClicks_18', 'GradeClicks_19', 'GradeClicks_20', 'GradeClicks_21', 'GradeClicks_22', 'GradeClicks_23', 'GradeClicks_24','GradeClicks_25','GradeClicks_26','GradeClicks_27', 'GradeClicks_28', 'GradeClicks_29', 'GradeClicks_30', 'GradeClicks_31', 'GradeClicks_32', 'GradeClicks_33', 'GradeClicks_34', 'GradeClicks_35', 'GradeClicks_36', 'GradeClicks_37', 'GradeClicks_38', 'GradeClicks_39',
'ClassMaterialClicks_0','ClassMaterialClicks_1','ClassMaterialClicks_2','ClassMaterialClicks_3', 'ClassMaterialClicks_4', 'ClassMaterialClicks_5', 'ClassMaterialClicks_6', 'ClassMaterialClicks_7', 'ClassMaterialClicks_8', 'ClassMaterialClicks_9', 'ClassMaterialClicks_10', 'ClassMaterialClicks_11', 'ClassMaterialClicks_12', 'ClassMaterialClicks_13', 'ClassMaterialClicks_14', 'ClassMaterialClicks_15', 'ClassMaterialClicks_16', 'ClassMaterialClicks_17', 'ClassMaterialClicks_18', 'ClassMaterialClicks_19', 'ClassMaterialClicks_20', 'ClassMaterialClicks_21', 'ClassMaterialClicks_22', 'ClassMaterialClicks_23', 'ClassMaterialClicks_24','ClassMaterialClicks_25','ClassMaterialClicks_26','ClassMaterialClicks_27', 'ClassMaterialClicks_28', 'ClassMaterialClicks_29', 'ClassMaterialClicks_30', 'ClassMaterialClicks_31', 'ClassMaterialClicks_32', 'ClassMaterialClicks_33', 'ClassMaterialClicks_34', 'ClassMaterialClicks_35', 'ClassMaterialClicks_36', 'ClassMaterialClicks_37', 'ClassMaterialClicks_38', 'ClassMaterialClicks_39',
'BenchmarkClicks_0','BenchmarkClicks_1','BenchmarkClicks_2','BenchmarkClicks_3', 'BenchmarkClicks_4', 'BenchmarkClicks_5', 'BenchmarkClicks_6', 'BenchmarkClicks_7', 'BenchmarkClicks_8', 'BenchmarkClicks_9', 'BenchmarkClicks_10', 'BenchmarkClicks_11', 'BenchmarkClicks_12', 'BenchmarkClicks_13', 'BenchmarkClicks_14', 'BenchmarkClicks_15', 'BenchmarkClicks_16', 'BenchmarkClicks_17', 'BenchmarkClicks_18', 'BenchmarkClicks_19', 'BenchmarkClicks_20', 'BenchmarkClicks_21', 'BenchmarkClicks_22', 'BenchmarkClicks_23', 'BenchmarkClicks_24','BenchmarkClicks_25','BenchmarkClicks_26','BenchmarkClicks_27', 'BenchmarkClicks_28', 'BenchmarkClicks_29', 'BenchmarkClicks_30', 'BenchmarkClicks_31', 'BenchmarkClicks_32', 'BenchmarkClicks_33', 'BenchmarkClicks_34', 'BenchmarkClicks_35', 'BenchmarkClicks_36', 'BenchmarkClicks_37', 'BenchmarkClicks_38', 'BenchmarkClicks_39',
'OtherClicks_0','OtherClicks_1','OtherClicks_2','OtherClicks_3', 'OtherClicks_4', 'OtherClicks_5', 'OtherClicks_6', 'OtherClicks_7', 'OtherClicks_8', 'OtherClicks_9', 'OtherClicks_10', 'OtherClicks_11', 'OtherClicks_12', 'OtherClicks_13', 'OtherClicks_14', 'OtherClicks_15', 'OtherClicks_16', 'OtherClicks_17', 'OtherClicks_18', 'OtherClicks_19', 'OtherClicks_20', 'OtherClicks_21', 'OtherClicks_22', 'OtherClicks_23', 'OtherClicks_24','OtherClicks_25','OtherClicks_26','OtherClicks_27', 'OtherClicks_28', 'OtherClicks_29', 'OtherClicks_30', 'OtherClicks_31', 'OtherClicks_32', 'OtherClicks_33', 'OtherClicks_34', 'OtherClicks_35', 'OtherClicks_36', 'OtherClicks_37', 'OtherClicks_38', 'OtherClicks_39']]

df1.to_csv('C:\\Users\\mt34546\\Documents\\UTStuff\\PennebakerLabStuff\\Click Data\\WhereClicks_48hr_Spring2016_Data.csv', index=False)