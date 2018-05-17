singleplayer <- read.csv("C:/Users/mt34546/Dropbox/GradSchoolStuff(UT)/Research-Data/Reddit-VideoGames-LIWC-communities-subset/LIWC_singleplayer_videogame_community_subset.csv")
multiplayer <- read.csv("C:/Users/mt34546/Dropbox/GradSchoolStuff(UT)/Research-Data/Reddit-VideoGames-LIWC-communities-subset/LIWC_multiplayer_videogame_community_subset.csv")

#trim unnecessary data
singleplayer2 <- subset(singleplayer, WC >= 50)
multiplayer2 <- subset(multiplayer, WC >= 50)
multiplayer2 <- subset(multiplayer2, subreddit != "ArenaFPS")
write.csv(multiplayer2, "C:/Users/mt34546/Dropbox/GradSchoolStuff(UT)/Research-Data/Reddit-VideoGames-LIWC-communities-subset/LIWC_multiplayerblah_videogame_community_subset.csv")

multiplayer3 <- read.csv("C:/Users/mt34546/Dropbox/GradSchoolStuff(UT)/Research-Data/Reddit-VideoGames-LIWC-communities-subset/LIWC_multiplayerblah_videogame_community_subset.csv")




singleplayer2$category = as.numeric(singleplayer2$subreddit)
multiplayer3$category = as.numeric(multiplayer3$subreddit)

write.csv(singleplayer2, "C:/Users/mt34546/Dropbox/GradSchoolStuff(UT)/Research-Data/Reddit-VideoGames-LIWC-communities-subset/LIWC_singleplayerFACTORS_videogame_community_subset.csv")
write.csv(multiplayer3, "C:/Users/mt34546/Dropbox/GradSchoolStuff(UT)/Research-Data/Reddit-VideoGames-LIWC-communities-subset/LIWC_multiplayerFACTORS_videogame_community_subset.csv")
