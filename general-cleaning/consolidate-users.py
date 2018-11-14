# -*- coding: utf-8 -*-
"""
Created on Tue Jun 19 12:36:06 2018

@author: mohini

1) Get a list of all of the files for a game
2) Check list for for multiples of usernames
3) Combine the text from the files with multiples of usernames and delete the previous seperate 
   files
"""


from collections import defaultdict
import os

def get_file_list(game_root):
    all_files_for_game = []
    for path, subdirs, files in os.walk(game_root):
        for file in files:
            if file.endswith('.txt') == True:
                all_files_for_game.append(os.path.join(path, file))
    return all_files_for_game

def extract_username_from_filename(filename):
	basename = os.path.basename(filename)
	# Not sure if this is required
	# Depends on whether or not reddit usernames can have '.' in them
	username = ''.join(os.path.splitext(basename)[:-1])
	return username

def get_files_by_username(all_files):
    files_by_username = defaultdict(lambda: [])
    for file in all_files:
        username = extract_username_from_filename(file)
        files_by_username[username].append(file)
    
    return files_by_username

def consolidate_files_by_username(username, filenames):
	# Will concatenate all the text from filenames into a single file,
	# and write it to the first given filename, then deletes all the other
	# files.
	all_text = []
	for filename in filenames:
		with open(filename, encoding="utf8") as txtfile:
			all_text.append(txtfile.read())

	# If you want two lines between each file, use '\n\n'
	all_text_str = '\n'.join(all_text)
	with open(filenames[0], 'w', encoding="utf8") as outfile:
		outfile.write(all_text_str)

	for file in filenames[1:]:
		os.remove(file)

# Will return something like:
# {
#	'user1': ['/a/1/user1.txt'],
#   'user2': ['/a/1/user2.txt', '/a/4/2.txt', '/a/124/2.txt']
#   'user3': [...]
#   ...
# }
        
###Script
        
game_root = r'D:\Games\20180423_Game_Comments\EZPZTXT'

all_folders = os.listdir(game_root)

print(all_folders)

for folder in all_folders: 
    print ("Starting: " + folder)
    folder_path = os.path.join(game_root, folder)
    files_by_username = get_files_by_username(get_file_list(folder_path))
    files_by_username = {user: filenames for user, filenames in files_by_username.items() if len(filenames) > 1}
    for username, files in files_by_username.items():
    	consolidate_files_by_username(username, files)
    print ("Finished: " + folder)