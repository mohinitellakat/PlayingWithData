# -*- coding: utf-8 -*-
"""
Mohini Tellakat
2018_06_05

Running LIWCiePy on a ton of data
"""
#import the lib
import LIWCiePy
from collections import defaultdict
from csv import DictWriter
import os
from multiprocessing.dummy import Pool as ThreadPool 
import time

### Functions

def get_username_from_filename(filename):
    return os.path.basename(filename)

def analyze_text_file(file_text_path):
    #need to read in the file text:
    with open(file_text_path, 'r', encoding='utf-8') as file_text_incoming:
        results = LIWC.analyze(file_text_incoming.read(), SummaryMeasures=True)
        results['Filename'] = get_username_from_filename(file_text_path) 
        return results

    
def write_results(results_filename, results):
    """
    Write the results of running LIWC over a single game to a CSV file.
    FP should be a file pointer that is opened for writing.
    """
    with open(results_filename, 'w') as csvfile:
        header = results[0].keys()
        writer = DictWriter(csvfile, fieldnames = header, lineterminator='\n')
        writer.writeheader()
        for row in results:
            writer.writerow(row)
            
def process_game(game_root):
    """
    multithreads the process of actually LIWCing the data and writes the
    results to a csv.
    """
    pool = ThreadPool(4)
    all_files_for_game = []
    for path, subdirs, files in os.walk(game_root):
        for file in files:
            if file.endswith('.txt') == True:
                all_files_for_game.append(os.path.join(path, file))
        
    results = pool.map(analyze_text_file, all_files_for_game)
    #output goes in the game EZPZTXT folder. If you want to change the location
    #of the text file, change the path of results.csv
    game = get_username_from_filename(game_root)
    results_filename = os.path.join(game_root, game + '_results.csv')
    print('writing results to {}'.format(results_filename))

    write_results(results_filename, results)
            
### Script      
    
start_time = time.time()

#instantiate a new "LIWCer" object
#the first parameter is the location/filename of the dictionary file
#the directory is not needed if the dictionary file is in the same directory as this script
#the second parameter is the encoding of your dictionary file
LIWC = LIWCiePy.LIWCer('D:/LIWCiePy-OG-code/2017-04-15-LIWC2015 Dictionary.dic', file_encoding='utf-8')

#analyze some text:
#file_text should be the string that you want to analyze
#the "SummaryMeasures" parameter is for if you are using the LIWC2015 dictionary and
#want to calculate Analytic, Tone, Clout, and Authentic. This will break if set to "True"
#and using any dictionary other than the official LIWC2015 English dictionary

#test file path: D:\Games\TestLIWCiePyFolder OR r'D:\Games\20180423_Game_Comments\EZPZTXT\Minesweeper'
#This is the path to where your file that has all of the sub files is located
#folder_path = input('Enter your filepath here:')
folder_path = 'D:\Games\TestLIWCiePyFolder'

#creates a list of all the folders inside your main folder
all_folders = os.listdir(folder_path)
    
for game_folder in all_folders:
    game_root = os.path.join(folder_path, game_folder)
    #game_root = folder_path
    process_game(game_root)
    
print ("My program took", time.time() - start_time, "to run")
