# code to merge and label LIWC data for arc of narrative and games project

american_football <- read.csv("C:/Users/mt34546/Dropbox/GradSchoolStuff(UT)/Research-Data/sports-mole-transcripts/LIWC2015 Results (american-football (108 files)).csv")
basketball<- read.csv("C:/Users/mt34546/Dropbox/GradSchoolStuff(UT)/Research-Data/sports-mole-transcripts/LIWC2015 Results (basketball (2 files)).csv")
boxing <- read.csv("C:/Users/mt34546/Dropbox/GradSchoolStuff(UT)/Research-Data/sports-mole-transcripts/LIWC2015 Results (boxing (32 files)).csv")
cricket<- read.csv("C:/Users/mt34546/Dropbox/GradSchoolStuff(UT)/Research-Data/sports-mole-transcripts/LIWC2015 Results (cricket (206 files)).csv")
diving<- read.csv("C:/Users/mt34546/Dropbox/GradSchoolStuff(UT)/Research-Data/sports-mole-transcripts/LIWC2015 Results (diving (12 files)).csv")
football<- read.csv("C:/Users/mt34546/Dropbox/GradSchoolStuff(UT)/Research-Data/sports-mole-transcripts/LIWC2015 Results (football (4915 files)).csv")
golf<- read.csv("C:/Users/mt34546/Dropbox/GradSchoolStuff(UT)/Research-Data/sports-mole-transcripts/LIWC2015 Results (golf (17 files)).csv")
racing<- read.csv("C:/Users/mt34546/Dropbox/GradSchoolStuff(UT)/Research-Data/sports-mole-transcripts/LIWC2015 Results (racing (1 files)).csv")
rugby_league<- read.csv("C:/Users/mt34546/Dropbox/GradSchoolStuff(UT)/Research-Data/sports-mole-transcripts/LIWC2015 Results (rugby-league (9 files)).csv")
rugby_union<- read.csv("C:/Users/mt34546/Dropbox/GradSchoolStuff(UT)/Research-Data/sports-mole-transcripts/LIWC2015 Results (rugby-union (104 files)).csv")
swimming<- read.csv("C:/Users/mt34546/Dropbox/GradSchoolStuff(UT)/Research-Data/sports-mole-transcripts/LIWC2015 Results (swimming (12 files)).csv")
tennis<- read.csv("C:/Users/mt34546/Dropbox/GradSchoolStuff(UT)/Research-Data/sports-mole-transcripts/LIWC2015 Results (tennis (356 files)).csv")
wwe<- read.csv("C:/Users/mt34546/Dropbox/GradSchoolStuff(UT)/Research-Data/sports-mole-transcripts/LIWC2015 Results (wwe (3 files)).csv")


american_football$catnum = 1
basketball$catnum = 2
boxing$catnum = 3
cricket$catnum = 4
diving$catnum = 5
football$catnum = 6
golf$catnum = 7
racing$catnum = 8
rugby_league$catnum = 9
rugby_union$catnum = 10
swimming$catnum = 11
tennis$catnum = 12
wwe$catnum = 13

sports_narratives <- rbind(american_football, basketball, boxing, cricket, diving, football, golf, racing, rugby_league, rugby_union, swimming, tennis, wwe)

write.csv(sports_narratives, "C:/Users/mt34546/Dropbox/GradSchoolStuff(UT)/Research-Data/sports-mole-transcripts/LIWC_Sports_Narrative_PreRearranging.csv")
