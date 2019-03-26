#set directory
setwd("G:/My Drive/GradSchoolStuff(UT)/Research-Data/Gaming Data/centrality analysis")

#read in data
merged_data <- read.csv("pergame-merged-LIWC64.csv")

#look at distribution of per_gaming values
hist(merged_data$per_gaming,breaks=100)

#Get median to do a median split on high vs. low gaming community involvement
median (merged_data$per_gaming) #0.07692308
mean(merged_data$per_gaming) #0.2015462

#make WC > 100 words
hund_merged_data <- subset(merged_data, WC >= 100)
hist(hund_merged_data$per_gaming, breaks = 100)

#correlate per_gaming with all other LIWC variables across games
nums <- unlist(lapply(hund_merged_data, is.numeric))
per_gaming_cor <- cor(hund_merged_data$per_gaming, hund_merged_data[,] )

# library(psych)
# per_gaming_cor_test <- corr.test(merged_data$per_gaming, merged_data[, nums])

write.csv(per_gaming_cor, file="hund_correlations-pergaming.csv")

#Data is skewed, so let's z-score it so we can split it. 
merged_data$per_gaming_zscore <- scale(merged_data$per_gaming, center=TRUE, scale = TRUE)

