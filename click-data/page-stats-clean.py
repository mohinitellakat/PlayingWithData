# -*- coding: utf-8 -*-
"""
Cleaning page_stats.csv file and adding necessary rows for analysis
Created on Wed Jul 27 21:55:50 2016

@author: Mohini
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


# Lists to hold data
date_list = []
time_list = []

class_status_list = []
in_class_list = []
out_of_class_list = []
before_class_list = []
after_class_list = []
in_benchmark_list = []


office_hours_list = []
grades_list = []
quizzes_list = []
discussion_topics_list = []
conversations_list = []
course_materials_list = []
downloads_list = []
modules_list = []
pages_list = []
assignments_list = []
syllabus_list = []
other_list = []
video_archive_list = []
piazza_list = []
survey_list = []
canvas_homepage_list = []
psych_homepage_list = []
external_tools_list = []

hour_list=[]

benchmark_num_list = []


#Sums column data with respect to a given key
def make_sum_dataframe(key, colname):
    dfx = df1.groupby(by=[key])[colname].sum().to_frame()
    dfx = dfx.reset_index()
    return dfx

#getting rid of excess or duplicate data in the dataframe    
def continuous_merge (df_list, key):
    for i in range(len(df_list)):
        if i < len(df_list):
            if (i+1) < len(df_list):
                this_item = df_list[i]
                next_item = df_list[i+1]
                merged_item = pd.merge(this_item, next_item, on=key)
                df_list[i+1] = merged_item
            elif (i+1) == len(df_list):
                df_list[i] = merged_item
            else:
                print "This is out of range1"
        else:
            print "This is out of range2"                     
    return merged_item

#FALL FILE PATH: C:\Users\mt34546\Documents\UTStuff\PennebakerLabStuff\Click Data\Starting Data\page_stats_Fall2015.csv
#SPRING FILE PATH: C:\Users\mt34546\Documents\UTStuff\PennebakerLabStuff\Click Data\Starting Data\page_stats_Spring2016.csv

file_path = raw_input('Enter your filepath here:')

df = pd.read_csv(file_path)

df1 = df.dropna(axis='rows', how='all')

df1 = df1[['eid','url','created_at','media_type']]

#Seperate out date and time
for row in df1['created_at']:
    ts = pd.Timestamp(row)
    try:
        ts.replace(tzinfo=None)
        central = pytz.timezone('US/Central')
        central_normal = central.normalize(ts)
        date_list.append(str(central_normal).rsplit(' ', 1)[0])
        time_list.append(str(central_normal).rsplit(' ', 1)[1])
    except: 
        date_list.append("nan")
        time_list.append("nan")
    
    year = central_normal.year
    month = central_normal.month
    day = central_normal.day
    hour = central_normal.hour
    minute = central_normal.minute

    #Check to see what part of class the students are in    
    if str(central_normal.date()) in semesterdates:   
        if str(central_normal.date()) in classdates:
            if (hour==15 and minute>=30 and minute<=45):
                timeperiod = "in benchmark"
                class_status_list.append(timeperiod)
            elif (hour==15 and minute>45 and minute<=59) or (hour==17 and minute>=0 and minute<=45):
                #print True
                timeperiod = "in class"
                class_status_list.append(timeperiod)
                
            elif (hour<=14 or (hour==15 and minute<30)):
                timeperiod = "before class"
                class_status_list.append(timeperiod)
            else:
                timeperiod = "after class"
                class_status_list.append(timeperiod)
        else:
            timeperiod = "out of class"
            class_status_list.append(timeperiod)
    else:
        timeperiod = "out of class"
        class_status_list.append(timeperiod)
        

df1['Date'] = date_list
df1['Time'] = time_list
df1['In Class Status'] = class_status_list

print "done with date, time, and in class status"




#Put in a boolean value and create an associated column if the time falls into an hour bucket
for each_time in df1['Time']:
    time2=pd.Timestamp(each_time)
    hour_et=time2.hour
    hour_list.append(hour_et)
df1['Hour'] = hour_list

for each_hour in df1['Hour'].unique():
    if each_hour in hours_of_day:
        df1["Click Hour " + str(each_hour)] = (df1['Hour'] == each_hour).astype(int)
    else:
        print "bad time"
        

# Put in a boolean value and create an associated column if the date falls into a date bucket
for each_date in df1['Date'].unique():
    if each_date in semesterdates:
        df1["Semester Day " + each_date] = (df1['Date']== each_date).astype(int)
    if each_date in classdates:
        df1["Class Day " + each_date] = (df1['Date']== each_date).astype(int)
    else:
        print 'Bad date'

print "done with click hour and semester/class day indicators"



# Put in a boolean value if the URL falls into a certain category
for i, url in enumerate(df1['url']):
    if df1['media_type'][i] == 'video_archive':
        office_hours_list.append(0)
        grades_list.append(0)
        quizzes_list.append(0)
        discussion_topics_list.append(0)
        conversations_list.append(0)
        course_materials_list.append(0)
        downloads_list.append(0)
        modules_list.append(0)
        pages_list.append(0)
        assignments_list.append(0)
        syllabus_list.append(0)
        video_archive_list.append(1)
        piazza_list.append(0)
        survey_list.append(0)
        canvas_homepage_list.append(0)
        psych_homepage_list.append(0)
        external_tools_list.append(0)
        other_list.append(0)
    elif df1['media_type'][i] == 'piazza':
        office_hours_list.append(0)
        grades_list.append(0)
        quizzes_list.append(0)
        discussion_topics_list.append(0)
        conversations_list.append(0)
        course_materials_list.append(0)
        downloads_list.append(0)
        modules_list.append(0)
        pages_list.append(0)
        assignments_list.append(0)
        syllabus_list.append(0)
        video_archive_list.append(0)
        piazza_list.append(1)
        survey_list.append(0)
        canvas_homepage_list.append(0)
        psych_homepage_list.append(0)
        external_tools_list.append(0)
        other_list.append(0)
    elif df1['media_type'][i] == 'survey':
        office_hours_list.append(0)
        grades_list.append(0)
        quizzes_list.append(0)
        discussion_topics_list.append(0)
        conversations_list.append(0)
        course_materials_list.append(0)
        downloads_list.append(0)
        modules_list.append(0)
        pages_list.append(0)
        assignments_list.append(0)
        syllabus_list.append(0)
        video_archive_list.append(0)
        piazza_list.append(0)
        survey_list.append(1)
        canvas_homepage_list.append(0)
        psych_homepage_list.append(0)
        external_tools_list.append(0)
        other_list.append(0)
    else:   
        if "contacts" in str(url):
            office_hours_list.append(1)
            grades_list.append(0)
            quizzes_list.append(0)
            discussion_topics_list.append(0)
            conversations_list.append(0)
            course_materials_list.append(0)
            downloads_list.append(0)
            modules_list.append(0)
            pages_list.append(0)
            assignments_list.append(0)
            syllabus_list.append(0)
            video_archive_list.append(0)
            piazza_list.append(0)
            survey_list.append(0)
            canvas_homepage_list.append(0)
            psych_homepage_list.append(0)
            external_tools_list.append(0)
            other_list.append(0)
        elif "mentors-office-hours" in str(url):
            office_hours_list.append(1)
            grades_list.append(0)
            quizzes_list.append(0)
            discussion_topics_list.append(0)
            conversations_list.append(0)
            course_materials_list.append(0)
            downloads_list.append(0)
            modules_list.append(0)
            pages_list.append(0)
            assignments_list.append(0)
            syllabus_list.append(0)
            video_archive_list.append(0)
            piazza_list.append(0)
            survey_list.append(0)
            canvas_homepage_list.append(0)
            psych_homepage_list.append(0)
            external_tools_list.append(0)
            other_list.append(0)
        elif "grades" in str(url):
            office_hours_list.append(0)
            grades_list.append(1)
            quizzes_list.append(0)
            discussion_topics_list.append(0)
            conversations_list.append(0)
            course_materials_list.append(0)
            downloads_list.append(0)
            modules_list.append(0)
            pages_list.append(0)
            assignments_list.append(0)
            syllabus_list.append(0)
            video_archive_list.append(0)
            piazza_list.append(0)
            survey_list.append(0)
            canvas_homepage_list.append(0)
            psych_homepage_list.append(0)
            external_tools_list.append(0)
            other_list.append(0)
        elif "assignments" in str(url):
            office_hours_list.append(0)
            grades_list.append(0)
            quizzes_list.append(0)
            discussion_topics_list.append(0)
            conversations_list.append(0)
            course_materials_list.append(0)
            downloads_list.append(0)
            modules_list.append(0)
            pages_list.append(0)
            assignments_list.append(1)
            syllabus_list.append(0)
            video_archive_list.append(0)
            piazza_list.append(0)
            survey_list.append(0)
            canvas_homepage_list.append(0)
            psych_homepage_list.append(0)
            external_tools_list.append(0)
            other_list.append(0)
        elif "quizzes" in str(url):
            office_hours_list.append(0)
            grades_list.append(0)
            quizzes_list.append(1)
            discussion_topics_list.append(0)
            conversations_list.append(0)
            course_materials_list.append(0)
            downloads_list.append(0)
            modules_list.append(0)
            pages_list.append(0)
            assignments_list.append(0)
            syllabus_list.append(0)
            video_archive_list.append(0)
            piazza_list.append(0)
            survey_list.append(0)
            canvas_homepage_list.append(0)
            psych_homepage_list.append(0)
            external_tools_list.append(0)
            other_list.append(0)
        elif "discussion_topics" in str(url):
            office_hours_list.append(0)
            grades_list.append(0)
            quizzes_list.append(0)
            discussion_topics_list.append(1)
            conversations_list.append(0)
            course_materials_list.append(0)
            downloads_list.append(0)
            modules_list.append(0)
            pages_list.append(0)
            assignments_list.append(0)
            syllabus_list.append(0)
            video_archive_list.append(0)
            piazza_list.append(0)
            survey_list.append(0)
            canvas_homepage_list.append(0)
            psych_homepage_list.append(0)
            external_tools_list.append(0)
            other_list.append(0)
        elif "conversations" in str(url):
            office_hours_list.append(0)
            grades_list.append(0)
            quizzes_list.append(0)
            discussion_topics_list.append(0)
            conversations_list.append(1)
            course_materials_list.append(0)
            downloads_list.append(0)
            modules_list.append(0)
            pages_list.append(0)
            assignments_list.append(0)
            syllabus_list.append(0)
            video_archive_list.append(0)
            piazza_list.append(0)
            survey_list.append(0)
            canvas_homepage_list.append(0)
            psych_homepage_list.append(0)
            external_tools_list.append(0)
            other_list.append(0)
        elif "course-materials" in str(url):
            office_hours_list.append(0)
            grades_list.append(0)
            quizzes_list.append(0)
            discussion_topics_list.append(0)
            conversations_list.append(0)
            course_materials_list.append(1)
            downloads_list.append(0)
            modules_list.append(0)
            pages_list.append(0)
            assignments_list.append(0)
            syllabus_list.append(0)
            video_archive_list.append(0)
            piazza_list.append(0)
            survey_list.append(0)
            canvas_homepage_list.append(0)
            psych_homepage_list.append(0)
            external_tools_list.append(0)
            other_list.append(0)
        elif "download" in str(url):
            office_hours_list.append(0)
            grades_list.append(0)
            quizzes_list.append(0)
            discussion_topics_list.append(0)
            conversations_list.append(0)
            course_materials_list.append(0)
            downloads_list.append(1)
            modules_list.append(0)
            pages_list.append(0)
            assignments_list.append(0)
            syllabus_list.append(0)
            video_archive_list.append(0)
            piazza_list.append(0)
            survey_list.append(0)
            canvas_homepage_list.append(0)
            psych_homepage_list.append(0)
            external_tools_list.append(0)
            other_list.append(0)
        elif "modules" in str(url):
            office_hours_list.append(0)
            grades_list.append(0)
            quizzes_list.append(0)
            discussion_topics_list.append(0)
            conversations_list.append(0)
            course_materials_list.append(0)
            downloads_list.append(0)
            modules_list.append(1)
            pages_list.append(0)
            assignments_list.append(0)
            syllabus_list.append(0)
            video_archive_list.append(0)
            piazza_list.append(0)
            survey_list.append(0)
            canvas_homepage_list.append(0)
            psych_homepage_list.append(0)
            external_tools_list.append(0)
            other_list.append(0)
        elif "pages" in str(url):
            office_hours_list.append(0)
            grades_list.append(0)
            quizzes_list.append(0)
            discussion_topics_list.append(0)
            conversations_list.append(0)
            course_materials_list.append(0)
            downloads_list.append(0)
            modules_list.append(0)
            pages_list.append(1)
            assignments_list.append(0)
            syllabus_list.append(0)
            video_archive_list.append(0)
            piazza_list.append(0)
            survey_list.append(0)
            canvas_homepage_list.append(0)
            psych_homepage_list.append(0)
            external_tools_list.append(0)
            other_list.append(0)
        elif "syllabus" in str(url):
            office_hours_list.append(0)
            grades_list.append(0)
            quizzes_list.append(0)
            discussion_topics_list.append(0)
            conversations_list.append(0)
            course_materials_list.append(0)
            downloads_list.append(0)
            modules_list.append(0)
            pages_list.append(0)
            assignments_list.append(0)
            syllabus_list.append(1)
            video_archive_list.append(0)
            piazza_list.append(0)
            survey_list.append(0)
            canvas_homepage_list.append(0)
            psych_homepage_list.append(0)
            external_tools_list.append(0)
            other_list.append(0)
        elif str(url) == "https://utexas.instructure.com/":
            office_hours_list.append(0)
            grades_list.append(0)
            quizzes_list.append(0)
            discussion_topics_list.append(0)
            conversations_list.append(0)
            course_materials_list.append(0)
            downloads_list.append(0)
            modules_list.append(0)
            pages_list.append(0)
            assignments_list.append(0)
            syllabus_list.append(0)
            video_archive_list.append(0)
            piazza_list.append(0)
            survey_list.append(0)
            canvas_homepage_list.append(1)
            psych_homepage_list.append(0)
            external_tools_list.append(0)
            other_list.append(0)
        elif str(url) == "https://utexas.instructure.com/courses/1151140":
            office_hours_list.append(0)
            grades_list.append(0)
            quizzes_list.append(0)
            discussion_topics_list.append(0)
            conversations_list.append(0)
            course_materials_list.append(0)
            downloads_list.append(0)
            modules_list.append(0)
            pages_list.append(0)
            assignments_list.append(0)
            syllabus_list.append(0)
            video_archive_list.append(0)
            piazza_list.append(0)
            survey_list.append(0)
            canvas_homepage_list.append(0)
            psych_homepage_list.append(1)
            external_tools_list.append(0)
            other_list.append(0)
        elif "external_tools" in str(url):
            office_hours_list.append(0)
            grades_list.append(0)
            quizzes_list.append(0)
            discussion_topics_list.append(0)
            conversations_list.append(0)
            course_materials_list.append(0)
            downloads_list.append(0)
            modules_list.append(0)
            pages_list.append(0)
            assignments_list.append(0)
            syllabus_list.append(0)
            video_archive_list.append(0)
            piazza_list.append(0)
            survey_list.append(0)
            canvas_homepage_list.append(0)
            psych_homepage_list.append(0)
            external_tools_list.append(1)
            other_list.append(0)
        else:
            office_hours_list.append(0)
            grades_list.append(0)
            quizzes_list.append(0)
            discussion_topics_list.append(0)
            conversations_list.append(0)
            course_materials_list.append(0)
            downloads_list.append(0)
            modules_list.append(0)
            pages_list.append(0)
            assignments_list.append(0)
            syllabus_list.append(0)
            video_archive_list.append(0)
            piazza_list.append(0)
            survey_list.append(0)
            canvas_homepage_list.append(0)
            psych_homepage_list.append(0)
            external_tools_list.append(0)
            other_list.append(1)

df1['URL: Office Hours'] = office_hours_list
df1['URL: Grades'] = grades_list
df1['URL: Course Materials'] = course_materials_list
df1['URL: Quizzes'] = quizzes_list
df1['URL: Discussion Topics'] = discussion_topics_list
df1['URL: Conversations'] = conversations_list
df1['URL: Downloads'] = downloads_list
df1['URL: Modules'] = modules_list
df1['URL: Pages'] = pages_list
df1['URL: Syllabus'] = syllabus_list
df1['URL: Assignments'] = assignments_list
df1['URL: Video Archives'] = video_archive_list
df1['URL: Piazza'] = piazza_list
df1['URL: Survey'] = survey_list
df1['URL: Canvas Homepage'] = canvas_homepage_list
df1['URL: Psych Homepage'] = psych_homepage_list
df1['URL: External Tools'] = external_tools_list
df1['URL: Other'] = other_list

print "done url indicators"

      

##CHANGE THE FILE NAME TO REFLECT WHAT SEMESTER AND TYPE OF DATA YOU ARE USING##
df1.to_csv('ps-data-clean/ps_data_Spring2016_intermediate_no_benchmark.csv' , index=False)
#result.to_csv('ps-data-clean/ps_data_short_Fall2015_clicks_and_class_status_sums.csv', index=False)