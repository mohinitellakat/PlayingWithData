# -*- coding: utf-8 -*-
#
# python version : 3.6.1

###########################################################################
##
##      .o oOOOOOOOo                                            OOOo
##       Ob.OOOOOOOo  OOOo.      oOOo.                      .adOOOOOOO
##       OboO"""""""""""".OOo. .oOOOOOo.    OOOo.oOOOOOo.."""""""""'OO
##       OOP.oOOOOOOOOOOO "POOOOOOOOOOOo.   `"OOOOOOOOOP,OOOOOOOOOOOB'
##       `O'OOOO'     `OOOOo"OOOOOOOOOOO` .adOOOOOOOOO"oOOO'    `OOOOo
##       .OOOO'            `OOOOOOOOOOOOOOOOOOOOOOOOOO'            `OO
##       OOOOO                 '"OOOOOOOOOOOOOOOO"`                oOO
##      oOOOOOba.                .adOOOOOOOOOOba               .adOOOOo.
##     oOOOOOOOOOOOOOba.    .adOOOOOOOOOO@^OOOOOOOba.     .adOOOOOOOOOOOO
##    OOOOOOOOOOOOOOOOO.OOOOOOOOOOOOOO"`  '"OOOOOOOOOOOOO.OOOOOOOOOOOOOO
##    OOOO"       "YOoOOOOMOIONODOO"`  .   '"OOROAOPOEOOOoOY"     "OOO"
##       Y           'OOOOOOOOOOOOOO: .oOOo. :OOOOOOOOOOO?'         :`
##       :            .oO%OOOOOOOOOOo.OOOOOO.oOOOOOOOOOOOO?         .
##       .            oOOP"%OOOOOOOOoOOOOOOO?oOOOOO?OOOO"OOo
##                    '%o  OOOO"%OOOO%"%OOOOO"OOOOOO"OOO':
##                         `$"  `OOOO' `O"Y ' `OOOO'  o             .
##       .                  .     OP"          : o     .
##                                :
##
##    Reddit Archival Data Extraction Script
##            Ryan L. Boyd
##            The University of Texas at Austin
##            Last updated on 2017-07-17
##
############################################################################





import os
import sys
import bz2
import json
import csv
import datetime

## °º¤ø,¸¸,ø¤º°`°º¤ø,¸,ø¤°º¤ø,¸¸,ø¤º°`°º¤ø,¸
##            IMPORTANT NOTE!!!
## °º¤ø,¸¸,ø¤º°`°º¤ø,¸,ø¤°º¤ø,¸¸,ø¤º°`°º¤ø,¸
## The dictionary structure of the comments
## and the submissions files are different.
## You do NOT want to run this script to
## include both parts of the data at the
## same time. You will want to run this
## script separately for each of the 2 sets
## even if you're filtering by the same key
## (e.g., subreddit). Make sure to set your
## header_keys list accordingly below.





#define the folder that the data is in
InputDirectory = 'E:/Dataset/Comments/'
#define the folder where we'd like to place out output data
OutputDirectory = 'D:/Games/Reddit-Comments-GameNetwork/DotA2'
#Define the filename of the output file
OutputFilename = 'Extracted Reddit Data - Comments'

#define the dictionary key by which we want to extract information.
#this key is **CASE SENSITIVE**
retain_key = 'author'

#define a list of items from the dictionary key that we want to
#include in the data that is being extracted. Anything equal to this
#will be included in the output file (case insensitive)
#an example of what this line can look like:
#
#retain_values = ['the_donald', 'sandersforpresident']
#
#these values are CASE INSENSITIVE. if you need case sensitivity,
#you will need to edit the key conditional later in this script
#to ensure that the matching lines up

Users_To_Keep = set()
User_List_Filename = 'D:/Games/authors-DotA2-Post100-Dota1.txt'

with open(User_List_Filename, 'r', encoding='utf8') as UserFileIncoming:
    for line in UserFileIncoming:
        if line.strip() not in Users_To_Keep:
            Users_To_Keep.add(line.strip())


retain_values = list(Users_To_Keep)


#convert all to lowercase, convert to set for faster lookups
retain_values = set([x.lower() for x in retain_values])

print(retain_values)


## °º¤ø,¸¸,ø¤º°`°º¤ø,¸,ø¤°º¤ø,¸¸,ø¤º°`°º¤ø,¸
##   header_keys for SUBMISSIONS files
## °º¤ø,¸¸,ø¤º°`°º¤ø,¸,ø¤°º¤ø,¸¸,ø¤º°`°º¤ø,¸
##
##
#header_keys = ['author_id', 'created', 'original_link', 'stickied', 'score', 'report_reasons', 'created_utc', 'author_flair_css_class', 'subreddit', 'secure_media_embed', 'link_flair_css_class', 'media', 'archived', 'saved', 'secure_media', 'ups', 'preview', 'adserver_imp_pixel', 'promoted_by', 'url', 'is_self', 'from_kind', 'from', 'retrieved_on', 'media_embed', 'num_comments', 'third_party_tracking_2', 'thumbnail', 'hide_score', 'href_url', 'user_reports', 'thumbnail_width', 'thumbnail_height', 'mobile_ad_url', 'mod_reports', 'likes', 'locked', 'imp_pixel', 'third_party_tracking', 'contest_mode', 'distinguished', 'author_flair_text', 'gilded', 'from_id', 'domain', 'over_18', 'promoted', 'hidden', 'promoted_url', 'id', 'can_gild', 'is_video', 'post_hint', 'name', 'disable_comments', 'num_reports', 'edited', 'suggested_sort', 'third_party_trackers', 'link_flair_text', 'downs', 'approved_by', 'clicked', 'spoiler', 'view_count', 'permalink', 'promoted_display_name', 'subreddit_id', 'author_cakeday', 'adserver_click_url', 'banned_by', 'author', 'brand_safe', 'quarantine']
#header_keys_text = ['subreddit', 'created_utc', 'id', 'title', 'selftext', 'selftext_html', ]




## °º¤ø,¸¸,ø¤º°`°º¤ø,¸,ø¤°º¤ø,¸¸,ø¤º°`°º¤ø,¸
##      header_keys for COMMENTS files
## °º¤ø,¸¸,ø¤º°`°º¤ø,¸,ø¤°º¤ø,¸¸,ø¤º°`°º¤ø,¸
##
##
#header_keys = ['subreddit_id', 'can_gild', 'score', 'saved', 'gilded', 'replies', 'mod_reports', 'can_mod_post', 'name', 'archived', 'parent_id', 'approved_at_utc', 'created', 'author', 'author_flair_text', 'author_cakeday', 'retrieved_on', 'removal_reason', 'distinguished', 'approved_by', 'link_id', 'user_reports', 'report_reasons', 'controversiality', 'likes', 'downs', 'banned_by', 'created_utc', 'ups', 'edited', 'author_flair_css_class', 'score_hidden', 'num_reports', 'subreddit', 'id', 'stickied']
#header_keys_text = ['subreddit', 'created_utc', 'author', 'id', 'parent_id', 'body', 'body_html', ]
header_keys = ['gilded', 'replies', 'name', 'parent_id', 'created', 'author', 'author_flair_text', 'user_reports', 'report_reasons', 'controversiality', 'likes', 'downs', 'banned_by', 'created_utc', 'ups', 'edited', 'subreddit', 'id',]
header_keys_text = ['subreddit', 'created_utc', 'author', 'id', 'parent_id', 'body',]








#number of rows in each file to read before updating progress
#if you don't want to print row report output, you can
#change the value to a decimal, such as .01
row_report = 100000


#simple validation of our input/output locations
#create output directory if nonexistent
if InputDirectory.endswith('/') == False:
    InputDirectory = InputDirectory + '/'
if OutputDirectory.endswith('/') == False:
    OutputDirectory = OutputDirectory + '/'
if not os.path.exists(OutputDirectory):
    os.makedirs(OutputDirectory)


#initializing for later use
headerlen = len(header_keys)
headerlen_text = len(header_keys_text)
EntriesFound = 0
ErrorsFound = 0


#begin processing
with open(OutputDirectory + datetime.datetime.now().strftime("%Y-%m-%d") + ' - ' + OutputFilename + ' - MetaData.csv', 'w', newline='', encoding='utf-8') as out, open(OutputDirectory + datetime.datetime.now().strftime("%Y-%m-%d") + ' - ' + OutputFilename + ' - TextData.csv', 'w', newline='', encoding='utf-8') as out_text:
    csvout_meta = csv.writer(out, dialect='excel')
    csvout_text = csv.writer(out_text, dialect='excel')

    csvout_meta.writerow(header_keys)
    csvout_text.writerow(header_keys_text)

    for root, subdirs, files in os.walk(InputDirectory):
        for single_file in files:
            if single_file.endswith('.bz2'):



                file_row = 0
                print('\n----------------------------------------------')
                print('\nScanning Comments file: ' + single_file + '...')

                with bz2.BZ2File(root + single_file, 'rb') as bz:
                    for line in bz:

                        try: 

                            file_row += 1

                            if file_row % row_report == 0:
                                print('Reading ' + single_file + ' row ' + str(file_row) + '... ' + str(EntriesFound) + ' entries found so far...')
                            
                            data = json.loads(line)




                            #this 'if' statement is the determiner of what stays in the data
                            #as it stands now, it's just seeing if the key/value pair matches
                            #is congruent with what was specified at the beginning of the script
                            #this can be changed to do pretty much anything. For example, if you want
                            #to set it up so that you're pulling out any post where 'ups' is greater
                            #than 10, you could changes this to:
                            #
                            #if data['ups'] > 10:
                            #
                            #and so on. So, this next line is really the lynch pin of the whole thing
                            #in determining what data is extracted and what data is not.
                            
                                ###this line is the one to edit for data retention
                                #       |     |     |
                                #       |     |     |
                                #       |     |     |
                                #      vvv   vvv   vvv
                                #       v     v     v
                            if retain_key in data.keys() and \
                                data[retain_key].lower() in retain_values:
                                #       ^     ^     ^
                                #      ^^^   ^^^   ^^^
                                #       |     |     |
                                #       |     |     |
                                #       |     |     |
                                ##this line is the one to edit for data retention
                                
                                    EntriesFound += 1
                                    output_row_meta = [None] * headerlen
                                    output_row_text = [None] * headerlen_text

                                    #pull out metadata
                                    for col_index in range(0, headerlen):
                                        if header_keys[col_index] in data.keys():
                                            output_row_meta[col_index] = data[header_keys[col_index]]

                                    #pull out text data
                                    for col_index in range(0, headerlen_text):
                                        if header_keys_text[col_index] in data.keys():
                                            output_row_text[col_index] = data[header_keys_text[col_index]]

                                    #write the row already!
                                    csvout_meta.writerow(output_row_meta)
                                    csvout_text.writerow(output_row_text)

                        except Exception as e:
                            ErrorsFound += 1
                            print('----There was an error while processing row ' + str(file_row))
                            print('----' + str(e))






print('Finished processing data.')
print('Encountered ' + str(ErrorsFound) + ' data errors while processing.')


