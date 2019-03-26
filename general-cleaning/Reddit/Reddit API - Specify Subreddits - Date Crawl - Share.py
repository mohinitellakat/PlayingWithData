'Reddit API Crawler, using PRAW

'*This script was built for Python 2.7
'*This script requires the PRAW package
'*e.g., pip install praw



import os
import csv
import time
import praw
import codecs
import cStringIO
from praw.handlers import MultiprocessHandler
from datetime import datetime
import calendar


#set the directory where you would like for your output to go
OutputDir = "C:/Users/mt34546/Dropbox/GradSchoolStuff(UT)/parkinsons-subreddit-2011-2016"
#if old CSVs with the filenames are in this location,
#do you want to delete them? Deleting them will write new variable
#names to the header before starting as well.
WipeExistingCSVs = True
#for each user found in the subreddit that you specify, do you want to
#crawl their entire post history and log that as well?
#WARNING -- this will make the entire process take much longer, and the
#dataset will be much, much larger if you do this. In order to
#help offset this, you can set a limit to how much of a user's history you want
#to pull from the API as well.
Pull_User_History = False
#if we want to tally a file that keeps track of the number of threads that we
# *haven't* saved -- basically skipped threads not relevant to our sub search
Debug_Skip_Threads = True

#make sure that it ends with a trailing slash so that
#you know that it's there for future directory use in the script
if OutputDir.endswith("/") == False:
        OutputDir += "/"



#specify which subreddits you would like to examine
#IMPORTANT -- SUBS SHOULD BE IN LOWERCASE TO BE PROPERLY ACQUIRED
Subreddits = ['parkinsons']
#users to omit from comments -- good for keeping bots out, etc.
#this is case sensitive
Omitted_Users = ['flair_your_post_bot', 'A858DE45F56D9BC9', 'AAbot', 'ADHDbot', 'ALTcointip', 'AVR_Modbot', 'A_random_gif', 'AltCodeBot', 'Antiracism_Bot', 'ApiContraption', 'AssHatBot', 'AtheismModBot', 'AutoInsult', 'BELITipBot', 'BadLinguisticsBot', 'BanishedBot', 'BeetusBot', 'BensonTheBot', 'Bible_Verses_Bot', 'BlackjackBot', 'BlockchainBot', 'Brigade_Bot', 'Bronze-Bot', 'CAH_BLACK_BOT', 'CHART_BOT', 'CLOSING_PARENTHESIS', 'CPTModBot', 'Cakeday-Bot', 'CalvinBot', 'CaptionBot', 'CarterDugSubLinkBot', 'CasualMetricBot', 'Chemistry_Bot', 'ChristianityBot', 'Codebreakerbreaker', 'Comment_Codebreaker', 'ComplimentingBot', 'CreepierSmileBot', 'CreepySmileBot', 'CuteBot6969', 'DDBotIndia', 'DNotesTip', 'DRKTipBot', 'DefinitelyBot', 'DeltaBot', 'Dictionary__Bot', 'DidSomeoneSayBoobs', 'DogeLotteryModBot', 'DogeTipStatsBot', 'DogeWordCloudBot', 'DotaCastingBot', 'Downtotes_Plz', 'DownvotesMcGoats', 'DropBox_Bot', 'EmmaBot', 'Epic_Face_Bot', 'EscapistVideoBot', 'ExmoBot', 'ExplanationBot', 'FTFY_Cat6', 'FTFY_Cat', 'FedoraTipAutoBot', 'FelineFacts', 'Fixes_GrammerNazi_', 'FriendSafariBot', 'FriendlyCamelCaseBot', 'FrontpageWatch', 'Frown_Bot', 'GATSBOT', 'GabenCoinTipBot', 'GameDealsBot', 'Gatherer_bot', 'GeekWhackBot', 'GiantBombBot', 'GifAsHTML5', 'GoneWildResearcher', 'GooglePlusBot', 'GotCrypto', 'GrammerNazi_', 'GreasyBacon', 'Grumbler_bot', 'GunnersGifsBot', 'GunnitBot', 'HCE_Replacement_Bot', 'HScard_display_bot', 'Handy_Related_Sub', 'HighResImageFinder', 'HockeyGT_Bot', 'HowIsThisBestOf_Bot', 'IAgreeBot', 'ICouldntCareLessBot', 'IS_IT_SOLVED', 'I_BITCOIN_CATS', 'I_Say_No_', 'Insane_Photo_Bot', 'IsItDownBot', 'JiffyBot', 'JotBot', 'JumpToBot', 'KSPortBot', 'KarmaConspiracy_Bot', 'LazyLinkerBot', 'LinkFixerBotSnr', 'Link_Correction_Bot', 'Link_Demobilizer', 'Link_Rectifier_Bot', 'LinkedCommentBot', 'LocationBot', 'MAGNIFIER_BOT', 'Makes_Small_Text_Bot', 'Meta_Bot', 'MetatasticBot', 'MetricPleaseBot', 'Metric_System_Bot', 'MontrealBot', 'MovieGuide', 'MultiFunctionBot', 'MumeBot', 'NASCARThreadBot', 'NFLVideoBot', 'NSLbot', 'Nazeem_Bot', 'New_Small_Text_Bot', 'Nidalee_Bot', 'NightMirrorMoon', 'NoSleepAutoMod', 'NoSobStoryBot2', 'NobodyDoesThis', 'NotRedditEnough', 'PHOTO_OF_CAPTAIN_RON', 'PJRP_Bot', 'PhoenixBot', 'PigLatinsYourComment', 'PlayStoreLinks_Bot', 'PlaylisterBot', 'PleaseRespectTables', 'PloungeMafiaVoteBot', 'PokemonFlairBot', 'PoliteBot', 'PoliticBot', 'PonyTipBot', 'PornOverlord', 'Porygon-Bot', 'PresidentObama___', 'ProselytizerBot', 'PunknRollBot', 'QUICHE-BOT', 'RFootballBot', 'Random-ComplimentBOT', 'RandomTriviaBot', 'Rangers_Bot', 'Readdit_Bot', 'Reads_Small_Text_Bot', 'RealtechPostBot', 'ReddCoinGoldBot', 'Relevant_News_Bot', 'RequirementsBot', 'RfreebandzBOT', 'RiskyClickBot', 'SERIAL_JOKE_KILLER', 'SMCTipBot', 'SRD_Notifier', 'SRS_History_Bot', 'SRScreenshot', 'SWTOR_Helper_Bot', 'SakuraiBot_test', 'SakuraiBot', 'SatoshiTipBot', 'ShadowBannedBot', 'ShibeBot', 'ShillForMonsanto', 'Shiny-Bot', 'ShittyGandhiQuotes', 'ShittyImageBot', 'SketchNotSkit', 'SmallTextReader', 'Smile_Bot', 'Somalia_Bot', 'Some_Bot', 'StackBot', 'StarboundBot', 'StencilTemplateBOT', 'StreetFightMirrorBot', 'SuchModBot', 'SurveyOfRedditBot', 'TOP_COMMENT_OF_YORE', 'Text_Reader_Bot', 'TheSwedishBot', 'TipMoonBot', 'TitsOrGTFO_Bot', 'TweetPoster', 'Twitch2YouTube', 'Unhandy_Related_Sub', 'UnobtaniumTipBot', 'UrbanDicBot', 'UselessArithmeticBot', 'UselessConversionBot', 'VideoLinkBot', 'VideopokerBot', 'VsauceBot', 'WWE_Network_Bot', 'WeAppreciateYou', 'Website_Mirror_Bot', 'WeeaBot', 'WhoWouldWinBot', 'Wiki_Bot', 'Wiki_FirstPara_bot', 'WikipediaCitationBot', 'Wink-Bot', 'WordCloudBot2', 'WritingPromptsBot', 'X_BOT', 'YT_Bot', '_Definition_Bot_', '_FallacyBot_', '_Rita_', '__bot__', 'albumbot', 'allinonebot', 'annoying_yes_bot', 'asmrspambot', 'astro-bot', 'auto-doge', 'automoderator', 'autourbanbot', 'autowikibot', 'bRMT_Bot', 'bad_ball_ban_bot', 'ban_pruner', 'baseball_gif_bot', 'beecointipbot', 'bitcoinpartybot', 'bitcointip', 'bitofnewsbot', 'bocketybot', 'c5bot', 'c5bot', 'cRedditBot', 'callfloodbot', 'callibot', 'canada_goose_tip_bot', 'changetip', 'cheesecointipbot', 'chromabot', 'classybot', 'coinflipbot', 'coinyetipper', 'colorcodebot', 'comment_copier_bot', 'compilebot', 'conspirobot', 'creepiersmilebot', 'cris9696', 'cruise_bot', 'd3posterbot', 'define_bot', 'demobilizer', 'dgctipbot', 'digitipbot', 'disapprovalbot', 'dogetipbot', 'earthtipbot', 'edmprobot', 'elMatadero_bot', 'elwh392', 'expired_link_bot', 'fa_mirror', 'fact_check_bot', 'faketipbot', 'fedora_tip_bot', 'fedoratips', 'flappytip', 'flips_title', 'foreigneducationbot', 'frytipbot', 'fsctipbot', 'gabenizer-bot', 'gabentipbot', 'gfy_bot', 'gfycat-bot-sucksdick', 'gifster_bot', 'gives_you_boobies', 'givesafuckbot', 'gocougs_bot', 'godwin_finder', 'golferbot', 'gracefulcharitybot', 'gracefulclaritybot', 'gregbot', 'groompbot', 'gunners_gif_bot', 'haiku_robot', 'havoc_bot', 'hearing-aid_bot', 'hearing_aid_bot', 'hearingaid_bot', 'hit_bot', 'hockey_gif_bot', 'howstat', 'hwsbot', 'imgurHostBot', 'imgur_rehosting', 'imgurtranscriber', 'imirror_bot', 'isitupbot', 'jerkbot-3hunna', 'keysteal_bot', 'kittehcointipbot', 'last_cakeday_bot', 'linkfixerbot1', 'linkfixerbot2', 'linkfixerbot3', 'loser_detector_bot', 'luckoftheshibe', 'makesTextSmall', 'malen-shutup-bot', 'matthewrobo', 'meme_transcriber', 'memedad-transcriber', 'misconception_fixer', 'mma_gif_bot', 'moderator-bot', 'nba_gif_bot', 'new_eden_news_bot', 'nhl_gif_bot', 'not_alot_bot', 'notoverticalvideo', 'nyantip', 'okc_rating_bot', 'pandatipbot', 'pandatips', 'potdealer', 'provides-id', 'qznc_bot', 'rSGSpolice', 'r_PictureGame', 'raddit-bot', 'randnumbot', 'rarchives', 'readsmalltextbot', 'redditbots', 'redditreviewbot', 'redditreviewbot', 'reddtipbot', 'relevantxkcd-bot', 'request_bot', 'rhiever-bot', 'rightsbot', 'rnfl_robot', 'roger_bot', 'rss_feed', 'rubycointipbot', 'rule_bot', 'rusetipbot', 'sentimentviewbot', 'serendipitybot', 'shadowbanbot', 'slapbot', 'slickwom-bot', 'snapshot_bot', 'soccer_gif_bot', 'softwareswap_bot', 'sports_gif_bot', 'spursgifs_xposterbot', 'stats-bot', 'steam_bot', 'subtext-bot', 'synonym_flash', 'tabledresser', 'techobot', 'tennis_gif_bot', 'test_bot0x00', 'tipmoonbot1', 'tipmoonbot2', 'tittietipbot', 'topcoin_tip', 'topredditbot', 'totes_meta_bot', 'ttumblrbots', 'unitconvert', 'valkyribot', 'versebot', 'vertcoinbot', 'vertcointipbot', 'wheres_the_karma_bot', 'wooshbot', 'xkcd_bot', 'xkcd_number_bot', 'xkcd_number_bot', 'xkcd_number_bot', 'xkcd_transcriber', 'xkcdcomic_bot', 'yes_it_is_weird', 'yourebot', ]

#how many times should the script crawl through the subreddits
#to look for new posts?
Number_of_Crawls = 1
#how long should the script wait between each crawl?
Hours_Between_Crawls = 0
#how many threads to look for
#this can also be set to "None" (without the quotes)
MaxThreads = None
#if digging into user's history data, this will determine
#how far (number of posts) to go back in the person's
#history. again, "None" is an option to get all of their history
User_Post_History_Limit = 75
#check to make sure that you're not recapturing the same information multiple times
Check_Preexisting = False
#set the day, month, and year to begin/end search
Starting_Year = 2011
Starting_Month = 1
Starting_Day = 1
Ending_Year = 2016
Ending_Month = 12
Ending_Day = 31
#How many days to increment during each loop
Days_To_Increment = 5


#this is our function that we'll use to check for already-captured submissions/comments
def Already_Captured_Submission(post_id):
    Already_Capped = False
    with open(OutputDir + '_Captured_Threads.txt', 'rb+') as f:
        for line in f:
            if line.strip() == post_id:
                Already_Capped = True
                break
    return Already_Capped

def Already_Captured_User(user_id):
    Already_Capped = False
    with open(OutputDir + '_Captured_Users.txt', 'rb+') as f:
        for line in f:
            if line.strip() == user_id:
                Already_Capped = True
                break
    return Already_Capped

def Log_Submission(post_id):
    with open(OutputDir + '_Captured_Threads.txt', 'ab+') as f:
        f.write(post_id + '\r\n')

def Log_User(user_id):
    with open(OutputDir + '_Captured_Users.txt', 'ab+') as f:
        f.write(user_id + '\r\n')



## the classic unicode csv writer. So nice.
class UTF8Recoder:
    def __init__(self, f, encoding):
        self.reader = codecs.getreader(encoding)(f)
    def __iter__(self):
        return self
    def next(self):
        return self.reader.next().encode("utf-8")

class UnicodeReader:
    def __init__(self, f, dialect=csv.excel, encoding="utf-8-sig", **kwds):
        f = UTF8Recoder(f, encoding)
        self.reader = csv.reader(f, dialect=dialect, **kwds)
    def next(self):
        '''next() -> unicode
        This function reads and returns the next line as a Unicode string.
        '''
        row = self.reader.next()
        return [unicode(s, "utf-8") for s in row]
    def __iter__(self):
        return self

class UnicodeWriter:
    def __init__(self, f, dialect=csv.excel, encoding="utf-8-sig", **kwds):
        self.queue = cStringIO.StringIO()
        self.writer = csv.writer(self.queue, dialect=dialect, **kwds)
        self.stream = f
        self.encoder = codecs.getincrementalencoder(encoding)()
    def writerow(self, row):
        '''writerow(unicode) -> None
        This function takes a Unicode string and encodes it to the output.
        '''
        self.writer.writerow([s.encode("utf-8") for s in row])
        data = self.queue.getvalue()
        data = data.decode("utf-8")
        data = self.encoder.encode(data)
        self.stream.write(data)
        self.queue.truncate(0)

    def writerows(self, rows):
        for row in rows:
            self.writerow(row)
## the classic unicode csv writer. So nice.









#create a nice little output directory tree.
#this is all here to start setting things up for the data
if not os.path.exists(OutputDir + "Submission_OP_Text/"):
    os.makedirs(OutputDir + "Submission_OP_Text/")
if not os.path.exists(OutputDir + "Submission_Responses_Text/"):
    os.makedirs(OutputDir + "Submission_Responses_Text/")
if not os.path.exists(OutputDir + "User_Data-Past_Activity_Text - Merged/"):
    os.makedirs(OutputDir + "User_Data-Past_Activity_Text - Merged/")
#rather than dump all of their posts to separate files, it might make sense (for now)
#to just do the aggregated fashion, since we're omitting all of their posts from
#the official list of comments pulled from the subreddits of interest
##if not os.path.exists(OutputDir + "User_Activity_Text - Separate/"):
##    os.makedirs(OutputDir + "User_Activity_Text - Separate/")
for Subreddit in Subreddits:
    if not os.path.exists(OutputDir + "Submission_OP_Text/" + Subreddit):
        os.makedirs(OutputDir + "Submission_OP_Text/" + Subreddit)
    if not os.path.exists(OutputDir + "Submission_Responses_Text/" + Subreddit):
        os.makedirs(OutputDir + "Submission_Responses_Text/" + Subreddit)



if WipeExistingCSVs:

    for Subreddit in Subreddits:

        with open(OutputDir + Subreddit + '-Submission_Response_Data.csv', 'wb+') as f:
            writer = UnicodeWriter(f,quoting=csv.QUOTE_ALL)
            writer.writerow(['Subreddit', 'post.id', 'parent_id', 'author.id', 'author.name', 'time.localtime', 'ups', 'downs', 'controversiality', 'gilded', 'body'])

        with open(OutputDir + Subreddit + '-Submission_OP_Data.csv', 'wb+') as f:
            writer = UnicodeWriter(f,quoting=csv.QUOTE_ALL)
            writer.writerow(['Subreddit', 'post.id', 'post.title', 'author.id', 'author.name', 'created', 'edited', 'ups', 'downs', 'gilded', 'link', 'body'])

    with open(OutputDir + 'User_Data-Post_History.csv', 'wb+') as f:
        writer = UnicodeWriter(f,quoting=csv.QUOTE_ALL)
        writer.writerow(['subreddit', 'post.id', 'parent_id', 'author.id', 'author.name', 'created', 'ups', 'downs', 'controversiality', 'gilded', 'body'])

    with open(OutputDir + 'User_Data-General.csv', 'wb+') as f:
        writer = UnicodeWriter(f,quoting=csv.QUOTE_ALL)
        writer.writerow(['author.id', 'author.name', 'total.comment_karma', 'total.link_karma', 'User.is_gold', 'User.is_mod', 'User.has_verified_email', 'User.created'])

    open(OutputDir + '_Captured_Threads.txt', 'wb+').close()
    open(OutputDir + '_Captured_Users.txt', 'wb+').close()



















#this is where things really get started



handler = MultiprocessHandler()

#fill in the X's with your username / application name
r = praw.Reddit(user_agent='python:praw_agent:/u/mohtell')

Counter = 1
Skipped_Counter = 0

for crawlnumber in range(1, Number_of_Crawls + 1):






        for Subreddit in Subreddits:

                print('\r\nBEGINNING SEARCH OF ' + Subreddit + '\r\n')
                #this specifies your starting date
                Year = Starting_Year
                Month = Starting_Month
                Day = Starting_Day
                
                Roll_To_Next_Month = False
        
                while True:

                    if Day + Days_To_Increment > calendar.monthrange(Year, Month)[1]:
                        Roll_To_Next_Month = True
                    
                    if (Year >= Ending_Year) and (Month >= Ending_Month) and (Day + Days_To_Increment >= Ending_Day):
                        break

                    try:

                            #this little block is just for display purposes
                            Ending_Search_Day = 0
                            Peek_into_Next_Month = False
                            if Day + Days_To_Increment > calendar.monthrange(Year, Month)[1]:
                                Ending_Search_Day = calendar.monthrange(Year, Month)[1]
                                Peek_into_Next_Month = True
                            else:
                                Ending_Search_Day = Day + Days_To_Increment
                            
                            
                            start_time = str(int(time.mktime(datetime(Year,Month,Day).timetuple())))
                            if Peek_into_Next_Month == False:
                                end_time = str(int(time.mktime(datetime(Year,Month,Ending_Search_Day).timetuple())))
                                print('Trying ' + str(Year) + '-' + str(Month) + '-' + str(Day) + ' through ' + str(Year) + '-' + str(Month) + '-' + str(Ending_Search_Day))
                            else:
                                Peek_Year = Year
                                Peek_Month = Month + 1
                                Peek_Day = 1

                                if Peek_Month > 12:
                                    Peek_Month = 1
                                    Peek_Year += 1
                                end_time = str(int(time.mktime(datetime(Peek_Year,Peek_Month,Peek_Day).timetuple())))
                                print('Trying ' + str(Year) + '-' + str(Month) + '-' + str(Day) + ' through ' + str(Peek_Year) + '-' + str(Peek_Month) + '-' + str(Peek_Day))

                            #increment our date
                            if Roll_To_Next_Month == True:
                                Roll_To_Next_Month = False
                                Day = 1
                                Month += 1
                                if Month > 12:
                                    Month = 1
                                    Year += 1
                            else:
                                Day += Days_To_Increment
                                if Day > calendar.monthrange(Year, Month)[1]:
                                    Day = calendar.monthrange(Year, Month)[1]

                    
                            #make the initial submission request
                            submissions = r.search('timestamp:' + start_time + '..' + end_time, subreddit=Subreddit, syntax='cloudsearch', limit=MaxThreads)
                    except:
                        print('\t\tProblem with searching specified date range. Sleeping for 15.')
                        time.sleep(15)
                        continue




####INDENT ALREADY PERFORMED BELOW THIS POINT
                
                    while True: 

                        Number_of_503s = 0
                        try:
                            #we have to do it this way, rather than a "for item in submissions" loop
                            #since submissions is an iterable that can break with a 503 error when trying to get a response
                            item = submissions.next()
                            Number_of_503s = 0


                            

                            if item.subreddit.display_name.lower() in Subreddits:

                                #if any issues are encountered, RETRY X number of times (right now 5)
                                Successful_Completion = False
                                Retries = 0





                                while (Successful_Completion == False) and (Retries < 2):

                                    try:

                                        #try to print the first parts of the title -- if all else
                                        #fails, we'll just print the item.id
                                        try:
                                            print('\t' + str(Counter) + '. ' + Subreddit + ' ' + item.id + ', ' + item.title[0:20])
                                        except:
                                            print('\t' + str(Counter) + '. ' + Subreddit + ' ' + item.id)
                            
                                        item.replace_more_comments(limit=None, threshold=0)
                                        item_comments = praw.helpers.flatten_tree(item.comments)

                                        #print('SUBMISSION SUBMISSION SUBMISSION SUBMISSION SUBMISSION ')
                                        Submission_Output = [item.subreddit.display_name]
                                        Submission_Output.append(item.id)
                                        Submission_Output.append(item.title)

                                        try:
                                            Item_ID_Var = item.author.id
                                            Item_NAME_Var = item.author.name
                                        except:
                                            Item_ID_Var = 'ID_DELETED'
                                            Item_NAME_Var = 'USER_DELETED'

                                        Submission_Output.append(Item_ID_Var)
                                        Submission_Output.append(Item_NAME_Var)
                                                        
                                        Submission_Output.append(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(item.created)))
                                        Submission_Output.append(item.edited)
                                        Submission_Output.append(item.ups)
                                        Submission_Output.append(item.downs)
                                        Submission_Output.append(item.gilded)
                                        Submission_Output.append(item.url)

                                        Submission_Body = item.selftext.replace('`', '\'').splitlines(True)
                                        Submission_Body_Clean = ''
                                        for line in Submission_Body:
                                            if line.strip().startswith('&gt;'):
                                                Submission_Body_Clean += line.strip().replace('\r\n', ' ').replace('\r', ' ').replace('\n', ' ').replace('&gt;', '[START_QUOTE]') + '[END_QUOTE] '
                                            else:
                                                Submission_Body_Clean += line.strip().replace('\r\n', ' ').replace('\r', ' ').replace('\n', ' ') + ' '
                                        if Retries == 0:
                                            Submission_Output.append(Submission_Body_Clean.replace('\r\n', ' ').replace('\r', ' ').replace('\n', ' ').replace('&amp;', '&').replace('&lt;', '<').replace('&gt;', '>'))
                                        else:
                                            Submission_Output.append(Submission_Body_Clean.replace('\r\n', ' ').replace('\r', ' ').replace('\n', ' ').replace('&amp;', '&').replace('&lt;', '<').replace('&gt;', '>').decode('utf-8', 'ignore').encode('ascii', 'ignore'))


                                        
                                        

                                        #add the submission author to our list
                                        if (Already_Captured_User(Item_NAME_Var) == False) and (Item_NAME_Var not in Omitted_Users):
                                            Log_User(Item_NAME_Var)
                                           
                                        
                                        for comment in item_comments:

                                            #see comment below -- we'll do this only if the comment hasn't already been written to the data
                                            if ((Check_Preexisting == False) or (Already_Captured_Submission(comment.id) == False)) and (comment.body != '[deleted]'):

                                                    try:
                                                        Comment_ID_Var = comment.author.id
                                                        Comment_NAME_Var = comment.author.name
                                                    except:
                                                        Comment_ID_Var = 'ID_DELETED'
                                                        Comment_NAME_Var = 'USER_DELETED'

                                                    if (Comment_NAME_Var not in Omitted_Users):

                                                        #print('COMMENT COMMENT COMMENT COMMENT COMMENT ')
                                                        Comment_Output = [item.subreddit.display_name]
                                                        Comment_Output.append(comment.id)
                                                        Comment_Output.append(comment.parent_id.replace('t3_', '').replace('t1_', ''))

                                                        Comment_Output.append(Comment_ID_Var)
                                                        Comment_Output.append(Comment_NAME_Var)
                                                        
                                                        Comment_Output.append(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(comment.created)))
                                                        Comment_Output.append(comment.ups)
                                                        Comment_Output.append(comment.downs)
                                                        Comment_Output.append(comment.controversiality)
                                                        Comment_Output.append(comment.gilded)

                                                        Comment_Body = comment.body.replace('`', '\'').splitlines(True)
                                                        Comment_Body_Clean = ''
                                                        for line in Comment_Body:
                                                            if line.strip().startswith('&gt;'):
                                                                Comment_Body_Clean += line.strip().replace('\r\n', ' ').replace('\r', ' ').replace('\n', ' ').replace('&gt;', '[START_QUOTE]') + '[END_QUOTE] '
                                                            else:
                                                                Comment_Body_Clean += line.strip().replace('\r\n', ' ').replace('\r', ' ').replace('\n', ' ') + ' '

                                                        if Retries == 0:
                                                            Comment_Output.append(Comment_Body_Clean.replace('\r\n', ' ').replace('\r', ' ').replace('\n', ' ').replace('&amp;', '&').replace('&lt;', '<').replace('&gt;', '>'))
                                                        else:
                                                            Comment_Output.append(Comment_Body_Clean.replace('\r\n', ' ').replace('\r', ' ').replace('\n', ' ').replace('&amp;', '&').replace('&lt;', '<').replace('&gt;', '>').decode('utf-8', 'ignore').encode('ascii', 'ignore'))

                                                        ##print(comment.id)
                                                        ##print(comment.body)

                                                        Comment_Output = [unicode(i) for i in Comment_Output]
                                                        #WRITE THE COMMMENT OUTPUT LINE HERE
                                                        with open(OutputDir + item.subreddit.display_name + '-Submission_Response_Data.csv', 'ab+') as f:
                                                            writer = UnicodeWriter(f,quoting=csv.QUOTE_ALL)
                                                            writer.writerow(Comment_Output)
                                                        #WRITE THE TXT FILE HERE
                                                        with open(OutputDir + 'Submission_Responses_Text/' + item.subreddit.display_name + '/' + item.subreddit.display_name + '_post.id-' + comment.id + '_author.id-' + Comment_ID_Var + '_post.parent-' + comment.parent_id.replace('t3_', '') + '.txt', 'wb+') as f:
                                                            if Retries == 0:
                                                                f.write(Comment_Body_Clean.encode('utf-8', 'ignore'))
                                                            else:
                                                                f.write(Comment_Body_Clean.decode('utf-8', 'ignore').encode('ascii', 'ignore'))


                                                        #logs the unique ID of this submission, but only AFTER it has been written
                                                        #that way, if something fails in the superior loop, it won't retry and then
                                                        #rewrite all of this again
                                                        Log_Submission(comment.id)
                                                        #add the submission author to our list

                                                    if (Already_Captured_User(Comment_NAME_Var) == False) and (Comment_NAME_Var not in Omitted_Users):
                                                        Log_User(Comment_NAME_Var)



                                        
                                        #we do the 'if' here because we don't want to rewrite the submission on a subsequent pass
                                        #if we've already logged it. The upvotes might've changed, but we just want the snapshots
                                        #note that we will still get fresh comments using this method, just not rewrite the submission
                                        #itself
                                        if (Check_Preexisting == False) or (Already_Captured_Submission(item.id) == False):
                                            #this is where you'll write all of the data at this point -- only upon full completion will we let
                                            #Successful_Completion be set to True
                                            Submission_Output = [unicode(i) for i in Submission_Output]
                                            #WRITE THE COMMMENT OUTPUT LINE HERE
                                            #WRITE THE COMMMENT OUTPUT LINE HERE
                                            with open(OutputDir + item.subreddit.display_name + '-Submission_OP_Data.csv', 'ab+') as f:
                                                writer = UnicodeWriter(f,quoting=csv.QUOTE_ALL)
                                                writer.writerow(Submission_Output)
                                            #WRITE THE TXT FILE HERE
                                            with open(OutputDir + 'Submission_OP_Text/' + item.subreddit.display_name + '/' + item.subreddit.display_name + '_post.id-' + item.id + '_author.id-' + Item_ID_Var + '.txt', 'wb+') as f:
                                                if Retries == 0:
                                                    f.write(Submission_Body_Clean.encode('utf-8', 'ignore'))
                                                else:
                                                    f.write(Submission_Body_Clean.decode('utf-8', 'ignore').encode('ascii', 'ignore'))
                                            #logs the unique ID of this submission
                                            Log_Submission(item.id)
                                        Successful_Completion = True
                                        Counter += 1



                                    except:
                                        print('\t\terror writing output!')
            ##                            print(Submission_Output)
            ##                            try:
            ##                                print(Comment_Output)
            ##                            except:
            ##                                print('Comments not yet loaded for this submission.')
                                        Retries += 1
                                        time.sleep(10)

                            else:
                                if Debug_Skip_Threads == True:
                                    try:
                                        with open(OutputDir + '_DEBUG_Skipped_Submissions.txt', 'wb+') as f:
                                            f.write(str(Skipped_Counter))
                                    except:
                                        print('\t\tSkipped submission, couldn\'t write file')
                                    Skipped_Counter += 1

                        #if we've hit the end of the iterable "submissions", then we'll break from the while
                        #loop and move to the top level "for" loop specified above
                        except StopIteration:
                            #if Number_of_503s >= 2:
                             #print('Finished pulling all of date range! Moving on...')
                             break
                    
                        #if we hit any other exceptions (I kept running into 503 errors), then what we do is just
                        #sleep it off for 60 seconds and then try reconnecting again, since the "while" loop is
                        #completely indefinite and will continue until a StopIteration error has been encountered
                        except:
                            print('\t\tThere was an issue getting a response from the server. Sleeping for 60 secs.')
                            time.sleep(60)
                            Number_of_503s += 1

                
                #this is for if the crawls have been set to more than 1
                #not recommended for this method whatsoever, but just in case
        if Number_of_Crawls > 1:
            print('All finished with crawl #' + str(crawlnumber) + '. Now sleeping for ' + str(Hours_Between_Crawls) + ' hours.')
            time.sleep(int(float(Hours_Between_Crawls * 60 * 60)))












#AFTER we've done all of the great stuff above, then we can go through and get all of the other comments
#and user data -- this will include ONLY comments by them that were not collected anywhere above in any
#of the subreddits looked at in the above loops
                
#NEED TO DO ANOTHER 'RETRY' LOOP HERE USING WHILE AND TRY

print('Success in looking at all subreddits!!! Moving on to user data!\r\n\r\n')




with open(OutputDir + '_Captured_Users.txt', 'rb+') as f:
    for line in f:

        Person = line.strip().replace('\r\n','')


        Successful_Completion = False
        Retries = 0

        while (Successful_Completion == False) and (Retries < 2):

            try:
                User = r.get_redditor(Person)
                User_Output = [User.id]
                User_Output.append(User.name)
                User_Output.append(User.comment_karma)
                User_Output.append(User.link_karma)
                User_Output.append(User.is_gold)
                User_Output.append(User.is_mod)
                User_Output.append(User.has_verified_email)
                User_Output.append(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(User.created)))

                User_Output = [unicode(i) for i in User_Output]

                with open(OutputDir + 'User_Data-General.csv', 'ab+') as f:
                    writer = csv.writer(f)
                    writer.writerow(User_Output)
                Successful_Completion = True

                #once we have the "for real" user data above that covers the bulk of it,
                #we go ahead and set success to TRUE, since that's the most important thing
                #beyond that, we just go through and will fail out every user update with
                #a simpler try-catch

                if Pull_User_History == True:


   
                        User_Activity = User.get_comments(limit=User_Post_History_Limit)

                        while True:

                            try:

                                user_comment = User_Activity.next()    

                                if (user_comment.subreddit.display_name.lower() not in Subreddits) and (user_comment.body != '[deleted]'):
                                    #print('USER COMMENT COMMENT COMMENT COMMENT COMMENT ')
                                    User_Comment_Output = [user_comment.subreddit.display_name]
                                    User_Comment_Output.append(user_comment.id)
                                    User_Comment_Output.append(user_comment.parent_id.replace('t3_', '').replace('t1_', ''))
                                    User_Comment_Output.append(user_comment.author.id)
                                    User_Comment_Output.append(user_comment.author.name)
                                    User_Comment_Output.append(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(user_comment.created)))
                                    User_Comment_Output.append(user_comment.ups)
                                    User_Comment_Output.append(user_comment.downs)
                                    User_Comment_Output.append(user_comment.controversiality)
                                    User_Comment_Output.append(user_comment.gilded)

                                    User_Comment_Body = user_comment.body.replace('`', '\'').splitlines(True)
                                    User_Comment_Body_Clean = ''
                                    for line in User_Comment_Body:
                                        if line.strip().startswith('&gt;'):
                                            User_Comment_Body_Clean += line.strip().replace('\r\n', ' ').replace('\r', ' ').replace('\n', ' ').replace('&gt;', '[START_QUOTE]') + '[END_QUOTE] '
                                        else:
                                            User_Comment_Body_Clean += line.strip().replace('\r\n', ' ').replace('\r', ' ').replace('\n', ' ') + ' '


                                    #basically, we're setting this up so that if it fails the first time
                                    #we'll try it again as unicode
                                    Write_Retries = 0
                                    while Write_Retries < 2:
                                        try:
                                            if Write_Retries == 0:
                                                User_Comment_Output.append(User_Comment_Body_Clean.replace('\r\n', ' ').replace('\r', ' ').replace('\n', ' ').replace('&amp;', '&').replace('&lt;', '<').replace('&gt;', '>').encode('utf-8', 'ignore'))
                                                Write_Retries = 2
                                            else:
                                                User_Comment_Output.append(User_Comment_Body_Clean.replace('\r\n', ' ').replace('\r', ' ').replace('\n', ' ').replace('&amp;', '&').replace('&lt;', '<').replace('&gt;', '>').decode('utf-8', 'ignore').encode('ascii', 'ignore'))
                                                Write_Retries = 2
                                        except:
                                            Write_Retries += 1
                                            

                                    User_Comment_Output = [unicode(i) for i in User_Comment_Output]
                                    with open(OutputDir + 'User_Data-Post_History.csv', 'ab+') as f:
                                        writer = UnicodeWriter(f,quoting=csv.QUOTE_ALL)
                                        writer.writerow(User_Comment_Output)


                                    #WRITE THE TXT FILE HERE
                                    with open(OutputDir + 'User_Data-Past_Activity_Text - Merged/user.id-' + user_comment.author.id + '.txt', 'ab+') as f:
                                        if Write_Retries == 0:
                                            f.write(User_Comment_Body_Clean.encode('utf-8', 'ignore'))
                                        else:
                                            f.write(User_Comment_Body_Clean.decode('utf-8', 'ignore').encode('ascii', 'ignore'))    
                                    #log that we've written it so we don't write it again on the off chance that it shows up
                                    Log_Submission(user_comment.id)

                            except StopIteration:
                                break

                            except:
                                print('\tError writing ' + Person + '\'s archived comment! Retrying as ascii...')
                                #print(User_Comment_Output)
                                time.sleep(5)
                                continue


            except:
                Retries += 1
                print('\tError writing user output!')
                #print(User_Output)
                #print('\r\n')
                time.sleep(30)
                



             

        print('Pulled user history: ' + Person)
                
                

print('ALL DONE!!!')
