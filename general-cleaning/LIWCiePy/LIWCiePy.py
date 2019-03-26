#!/usr/bin/env python
# encoding: utf-8
# python 3.6.2
# LIWCiePy version 0.95
# 2017-12-09
# by Ryan L. Boyd, Ph.D.
# ryanboyd@utexas.edu
# The University of Texas at Austin

import os
import re
import json
from math import erf, sqrt


class LIWCer:

        def __init__(self, DicFilename= '2017-04-15-LIWC2015 Dictionary.dic', file_encoding='utf8'):

                self.LIWC_Dict_Layout = {'cat_order': [],
                                         'cat_codes': {}}
                self.LIWC_Dict = {}
                self.WildCardFixes = {}
                self.LookBehindFixes = []



                DicText = []

                find_lookbehind = re.compile(r'\(.*?\)')

                with open(DicFilename, 'r', encoding=file_encoding) as incoming:
                        DicText = incoming.readlines()

                print('Loading dictionary file...')
                
                readHeaders = False
                for line in DicText:

                        #figure out if we're reading the headers in or not
                        if line.strip() == '%' and readHeaders == False:
                                readHeaders = True
                                continue
                        elif line.strip() == '%' and readHeaders == True:
                                readHeaders = False
                                continue

                        #if we're reading in the headers still, this is what we want to do with each line
                        if readHeaders:
                                line_split = line.lower().strip().split('\t')
                                self.LIWC_Dict_Layout['cat_order'] += [line_split[0]]
                                self.LIWC_Dict_Layout['cat_codes'][line_split[0]] = line_split[1]





                        #once we've moved past the headers, we want to actually fill out our dictionary.
                        #the final "dictionary" will be regex driven, so that we can essentially just
                        #scan texts as they come in
                        else:


                                word = line.lower().strip().split('\t')[0]
                                cats = line.lower().strip().split('\t')[1:len(line.strip().split('\t'))]


                                #see if we need to impose a negative lookbehind
                                lookbehind_matches = find_lookbehind.findall(word)

                                lookbehindprefix = ''
                                lookbehindregex = r''
                                

                                #if we do, then we need to split those off and format them for regex                             
                                if len(lookbehind_matches) > 0:

                                        #now, we have the clean word with the lookbehinds split off
                                        word = find_lookbehind.sub(r'', word).strip()

                                        #then, we want to do 3 things. First, we want to look at any of the look at all of the
                                        #words in the lookbehinds and, if any of them are asterisked, we want to add those to
                                        #the wildcard fixes

                                        #then, we want to set up a special regex to find instances of the lookbehind, and replace
                                        #it with a clean version.
                                        #for example, "(could not) like" should become "couldnotlike". This lets us capture this
                                        #instance specifically.

                                        #then, we want to make sure that the word being coded in the dictionary is this "clean" version
                                        #e.g., "couldnotlike"

                                        
                                        #this does #1 -- add wildcards in the lookbehinds to the wildcard fix list
                                        for lookbehind in lookbehind_matches:

                                                if '*' in lookbehind:
                                                        if lookbehind.replace('(', '').replace(')', '').strip()[0] not in self.WildCardFixes.keys():
                                                               self.WildCardFixes[lookbehind.replace('(', '').replace(')', '').strip()[0]] = [lookbehind.replace('(', '').replace(')', '').replace('*', '').strip()]
                                                        elif lookbehind.replace('(', '').replace(')', '').replace('*', '').strip() not in self.WildCardFixes[lookbehind.replace('(', '').replace(')', '').strip()[0]]:
                                                                self.WildCardFixes[lookbehind.replace('(', '').replace(')', '').strip()[0]] += [lookbehind.replace('(', '').replace(')', '').replace('*', '').strip()]
                                                                

                                                lookbehindprefix += lookbehind.replace('*', '').replace('(', '').replace(')', '').replace(' ', '').strip()
                                                lookbehindregex += lookbehind.replace('*', '').replace('(', '').replace(')', '').strip()


                                        #now we're at #2 -- we want to set up a compiled regex that will replace the original version of the word
                                        #with a "clean" version of the word
                                        lookbehindregex = r'(?<=\s)(?<=' + re.escape(lookbehindregex) + r'\s)' + re.escape(word.replace('*', 'CONVERTMEINTOAWILDCARD')).replace('CONVERTMEINTOAWILDCARD', '.*?') + r'(?=\s)'

                                        self.LookBehindFixes += [[re.compile(lookbehindregex), lookbehindprefix + word.replace('*', '').strip()]]
                                                                


                                                
                                #now that we're back to looking at the word itself, we want to add it to the wildcard fixes
                                if '*' in word:
                                        if word[0] not in self.WildCardFixes.keys():
                                               self.WildCardFixes[word[0]] = [word.replace('*', '').strip()]
                                        elif word.replace('*', '').strip() not in self.WildCardFixes[word[0]]:
                                                self.WildCardFixes[word[0]] += [word.replace('*', '').strip()]

                                word = lookbehindprefix + word.replace('*', '')
                                word = word.strip()

                                

                                #print(word)                              

                                self.LIWC_Dict[word] = cats


                print('Dictionary is loaded.')
                                                                                                
                                        
                                        
                             




                        

                        
        def dump_my_dict(self, file_encoding='utf8'):

                dump_path = '_LIWCiePy_Output/'
        
                if not os.path.exists(dump_path):
                    os.makedirs(dump_path)
                
                with open(dump_path + 'dictionary.txt', 'w', encoding=file_encoding) as outgoing:
                        json.dump(self.LIWC_Dict, outgoing, sort_keys=True, indent=4, ensure_ascii=False)

                with open(dump_path + 'wildcard_fixes.txt', 'w', encoding=file_encoding) as outgoing:
                        json.dump(self.WildCardFixes, outgoing, sort_keys=True, indent=4, ensure_ascii=False)

                with open(dump_path + 'lookbehind_fixes.txt', 'w', encoding=file_encoding) as outgoing:
                        for item in self.LookBehindFixes:
                                outgoing.write(str(item[0]) + '\t\t' + item[1] + '\n')


        
        def analyze(self, text, SummaryMeasures=False):

                results = {}
                for cat in self.LIWC_Dict_Layout['cat_order']:
                        results[self.LIWC_Dict_Layout['cat_codes'][cat]] = 0

                results['Dic'] = 0
                results['SixLtr'] = 0

                text, results = self.prepare_text(text, results)

                text = text.split()
                results['WC'] = len(text)

                for word in text:
                        if word in self.LIWC_Dict:
                                results['Dic'] += (1 / results['WC']) * 100
                                for cat in self.LIWC_Dict[word]:
                                        results[self.LIWC_Dict_Layout['cat_codes'][cat]] += (1 / results['WC']) * 100

                        

                

                if (results['WC'] > 0):
                        #clean up the numbers a bit
                       
                                                
                        results['Dic'] = round(results['Dic'] * 100) / 100
                        results['SixLtr'] = round((results['SixLtr'] / results['WC']) * 10000) / 100

                        for cat in self.LIWC_Dict_Layout['cat_order']:
                                results[self.LIWC_Dict_Layout['cat_codes'][cat]] = round(results[self.LIWC_Dict_Layout['cat_codes'][cat]] * 100) / 100


                        if SummaryMeasures:

                                results['Analytic'] = None
                                results['Authentic'] = None
                                results['Clout'] = None
                                results['Tone'] = None
                        
                                results['Analytic'] = 30 + results['article'] + results['prep'] - results['ppron'] - results['ipron'] - results['auxverb'] - results['adverb'] - results['conj'] - results['negate']
                                results['Authentic'] = results['i'] + results['insight'] + results['differ'] + results['relativ'] - results['discrep'] - results['shehe']
                                results['Clout'] = 10 + results['we'] + results['you'] + results['social'] - results['i'] - results['swear'] - results['negate'] - results['differ']
                                results['Tone'] = results['posemo'] - results['negemo']

                                results['Analytic'] = (results['Analytic'] - 9.5) / 14
                                results['Authentic'] = (results['Authentic'] - 21) / 6
                                results['Clout'] = (results['Clout'] - 10) / 10
                                results['Tone'] = (results['Tone'] - 1.3) / 2

                                results['Analytic'] = round((0.5 * (1 + erf(results['Analytic'] / sqrt(2)))) * 10000) / 100
                                results['Authentic'] = round((0.5 * (1 + erf(results['Authentic'] / sqrt(2)))) * 10000) / 100
                                results['Clout'] = round((0.5 * (1 + erf(results['Clout'] / sqrt(2)))) * 10000) / 100
                                results['Tone'] = round((0.5 * (1 + erf(results['Tone'] / sqrt(2)))) * 10000) / 100
        

                return results


        def text_process_debug(self, text):
                results = {}
                for cat in self.LIWC_Dict_Layout['cat_order']:
                        results[self.LIWC_Dict_Layout['cat_codes'][cat]] = 0

                results['Dic'] = 0
                results['SixLtr'] = 0
                        
                text, results = self.prepare_text(text, results)

                return text

        

        def prepare_text(self, text, results):
                
                text = text.lower()
                #we want to clean up a lot of stuff about the text first,
                #which means that we have to make it clean enough for the
                #regexes that we've set up to be able to do their job
                number_replace = re.compile(r'\d+([\d,]?\d)*(\.\d+)?')
                text = number_replace.sub(' 65432168435121654651 ', text)
                
                punct_cleaner = re.compile(r'[^a-z0-9äöüÄÖÜß\ \'\-]+')

                text = punct_cleaner.sub(" ", text)
                words = text.split()

                #make sure that there isn't punctuation on either tail of word,
                #with the exception of a hyphen or apostrophe. we want to keep
                #these 2 intact because there are several wildcard versions of
                #words where they might end with those still (e.g., bro'*)
                words = [word.lstrip("'-") for word in words]

                #remove blank words at this point
                words = list(filter(None, words))
                
                for i in range(0, len(words)):
                        while '\'\'' in words[i]:
                                words[i] = words[i].replace('\'\'', '\'')
                        while '--' in words[i]:
                                words[i] = words[i].replace('--', '-')

                        if (len(words[i]) > 6) and (words[i] != '65432168435121654651'):
                                results['SixLtr'] += 1

                        #this was just to debug
                        #if i > 0:
                        #        print(words[i-1] + ' ' + words[i] + ' ' + words[i+1])

                        
                        if words[i][0] in self.WildCardFixes.keys():
                                for wildcard in self.WildCardFixes[words[i][0]]:
                                        if words[i].startswith(wildcard):
                                                words[i] = wildcard
                                                break

                text = ' ' + ' '.join(words) + ' '
                words = None


                #now, we go in and fix up lookbehinds
                for lookbehind in self.LookBehindFixes:
                        text = lookbehind[0].sub(lookbehind[1], text)


                return text, results



        


if __name__ == '__main__':
    LIWC = LIWCer('2017-04-15-LIWC2015 Dictionary.dic', file_encoding='utf8')
    results = LIWC.analyze('I am very pleased and pleased to meet all 863.51 of you.', SummaryMeasures=False)
    #print(LIWC.text_process_debug('I am very pleased and pleased to meet all 863.51 of you.'))
    #LIWC.dump_my_dict(file_encoding='utf8')
    print(results)

    
    


