videogames <- read.csv("C:/Users/mt34546/Dropbox/GradSchoolStuff(UT)/Research-Data/Reddit-VideoGames-LIWC-communities-subset/LIWC_with_playermodes_videogame_community_subset.csv")

singleplayer <- subset(videogames, singleplayer == 1)
multiplayer <- subset(videogames, multiplayer == 1)
bothplayermodes <- subset(videogames, both_player_modes == 1)

#single vs multiplayer csvs

write.csv(singleplayer, "C:/Users/mt34546/Dropbox/GradSchoolStuff(UT)/Research-Data/Reddit-VideoGames-LIWC-communities-subset/LIWC_singleplayer_videogame_community_subset.csv")
write.csv(multiplayer, "C:/Users/mt34546/Dropbox/GradSchoolStuff(UT)/Research-Data/Reddit-VideoGames-LIWC-communities-subset/LIWC_multiplayer_videogame_community_subset.csv")
write.csv(bothplayermodes, "C:/Users/mt34546/Dropbox/GradSchoolStuff(UT)/Research-Data/Reddit-VideoGames-LIWC-communities-subset/LIWC_bothplayermodes_videogame_community_subset.csv")

#trim unnecessary data
singleplayer2 <- subset(singleplayer, WC >= 50)
multiplayer2 <- subset(multiplayer, WC >= 50)
multiplayer2 <- subset(multiplayer2, subreddit != "ArenaFPS")
bothplayermodes2 <- subset(bothplayermodes, WC >= 50)

#get descriptive statistics on each subset
library(psych)
singleplayerstats <- describe(singleplayer2)
multiplayerstats <- describe(multiplayer2)
bothplayermodesstats <- describe(bothplayermodes2)

#assign category numbers to each subset
singleplayerstats$catnum = 1
multiplayerstats$catnum = 2
bothplayermodesstats$catnum = 3

#merge stats together into one dataframe
statsdata <- rbind(singleplayerstats, multiplayerstats, bothplayermodesstats)

write.csv(statsdata, "C:/Users/mt34546/Dropbox/GradSchoolStuff(UT)/Research-Data/Reddit-VideoGames-LIWC-communities-subset/LIWC_videogame_community_subset_stats.csv")

statsdata$catnum <- factor(statsdata$catnum)

library(ggplot2)
ggplot(statsdata, aes(x=catnum, y=mean(), fill=supp)) + 
  geom_bar(position=position_dodge(), stat="identity") +
  geom_errorbar(aes(ymin=len-ci, ymax=len+ci),
                width=.2,                    # Width of the error bars
                position=position_dodge(.9))

# Error bars represent standard error of the mean
ggplot(statsdata, aes(x=dose, y=len, fill=supp)) + 
  geom_bar(position=position_dodge(), stat="identity") +
  geom_errorbar(aes(ymin=len-se, ymax=len+se),
                width=.2,                    # Width of the error bars
                position=position_dodge(.9))