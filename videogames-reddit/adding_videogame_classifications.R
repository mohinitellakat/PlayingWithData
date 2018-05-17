videogame_LIWC_subset <- read.csv("C:/Users/mt34546/Dropbox/GradSchoolStuff(UT)/Research-Data/Reddit-VideoGames-LIWC-communities-subset/LIWC_merged_videogame_community_subset.csv")

player_modes <- read.csv("D:/Games/games_list_withmetadata.csv")

joined_data <- merge(x = videogame_LIWC_subset, y = player_modes, by = "subreddit", all = TRUE)

write.csv(joined_data, "C:/Users/mt34546/Dropbox/GradSchoolStuff(UT)/Research-Data/Reddit-VideoGames-LIWC-communities-subset/LIWC_with_playermodes_videogame_community_subset.csv")
