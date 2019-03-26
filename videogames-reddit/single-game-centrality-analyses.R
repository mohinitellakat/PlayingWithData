#set directory
setwd("G:/My Drive/GradSchoolStuff-UT/Research-Data/Gaming Data/centrality analysis/inital 3 game analysis")

#read in data
pergame_data <- read.csv("G:/My Drive/GradSchoolStuff-UT/Research-Data/Gaming Data/centrality analysis/post_stats_centrality.csv")
liwc_data <- read.csv("DotA2_results.csv")
single_game_centrality_data <- read.csv("G:/My Drive/GradSchoolStuff-UT/Research-Data/Gaming Data/centrality analysis/in-depth-DotA2/dota_centrality.csv")

#rename filename to author
colnames(liwc_data)[colnames(liwc_data) == 'Filename'] <- 'author'

#delete .txt and _results.csv from author and subreddit
liwc_data$author <- gsub(".txt", "", liwc_data$author)

#make WC cutoff 
FH_data <- subset(liwc_data, WC >= 25)

###Get general metrics about the sample
#merge percent gaming data into the file
merged_data <- merge(FH_data, pergame_data)
merged_data <- merge(merged_data, single_game_centrality_data)
merged_data$total_posts <- merged_data$gaming_posts + merged_data$non_gaming_posts

write.csv(merged_data[,c("author", "total_posts", "gaming_posts", "non_gaming_posts", "dota2_num_posts", "game_centrality", "dota2_centrality")], file="post-info-DotA2.csv")
write.csv(merged_data$author, file="authors-DotA2-WCg25.csv")

subset_data <- subset(merged_data, dota2_num_posts >=1)
subset_data <- subset(subset_data, total_posts >=100)

#Get author list
write.csv(subset_data$author, file="authors-DotA2-Post100-Dota1.csv", row.names = FALSE, col.names = FALSE)

#look at distributions of post-values
library(ggplot2)

ggplot(subset_data, aes(x=total_posts)) + xlim(100,200) + ylim (0,15000) + geom_histogram(binwidth = 1, color = "black", fill="white")
ggplot(subset_data, aes(x=gaming_posts)) + xlim(1,200) + ylim(0,15000) +geom_histogram(binwidth = 1, color = "black", fill="white")
ggplot(subset_data, aes(x=non_gaming_posts)) + xlim(1,200) + ylim(0,8000) + geom_histogram(binwidth = 1, color = "black", fill="white")
ggplot(subset_data, aes(x=dota2_num_posts)) + xlim(1,200) + ylim(0, 10000) + geom_histogram(binwidth = 1, color = "black", fill="white")
ggplot(subset_data, aes(x=game_centrality)) + geom_histogram(binwidth = 0.1, color = "black", fill="white")
ggplot(subset_data, aes(x=dota2_centrality)) + xlim(0,1) + ylim(0, 20000) + geom_histogram(binwidth = 0.1, color = "black", fill="white")



#get means of important datapoints
mean(subset_data$total_posts)
mean(subset_data$gaming_posts)
mean(subset_data$non_gaming_posts)
mean(subset_data$dota2_num_posts)
mean(subset_data$dota2_centrality)
mean(subset_data$game_centrality)

#calculating num_game_posts-dota posts
subset_data$game_not_dota <- subset_data$gaming_posts - subset_data$dota2_num_posts

#create new variable thirdperson
subset_data$thirdperson <- subset_data$shehe + subset_data$they

#correlate num_posts
cor(subset_data$gaming_posts, subset_data$game_not_dota) #0.99
cor(subset_data$gaming_posts, subset_data$dota2_num_posts) #0.34
cor(subset_data$dota2_num_posts, subset_data$game_not_dota) #0.22

#means for each subset of centrality data
firstgroup <- subset(subset_data, game_centrality <= 0.1)
secondgroup <- subset(subset_data, game_centrality > 0.1 & game_centrality <=0.2)
thirdgroup <- subset(subset_data, game_centrality > 0.2 & game_centrality <=0.3)
fourthgroup <- subset(subset_data, game_centrality > 0.3 & game_centrality <=0.4)
fifthgroup <- subset(subset_data, game_centrality > 0.4 & game_centrality <=0.5)
sixthgroup <- subset(subset_data, game_centrality > 0.5 & game_centrality <=0.6)
seventhgroup <- subset(subset_data, game_centrality > 0.6 & game_centrality <=0.7)
eighthgroup <- subset(subset_data, game_centrality > 0.7 & game_centrality <=0.8)
ninthgroup <- subset(subset_data, game_centrality > 0.8 & game_centrality <=0.9)
tenthgroup <- subset(subset_data, game_centrality > 0.9)

d_firstgroup <- subset(subset_data, dota2_centrality <= 0.1)
d_secondgroup <- subset(subset_data, dota2_centrality > 0.1 & dota2_centrality <=0.2)
d_thirdgroup <- subset(subset_data, dota2_centrality > 0.2 & dota2_centrality <=0.3)
d_fourthgroup <- subset(subset_data, dota2_centrality > 0.3 & dota2_centrality <=0.4)
d_fifthgroup <- subset(subset_data, dota2_centrality > 0.4 & dota2_centrality <=0.5)
d_sixthgroup <- subset(subset_data, dota2_centrality > 0.5 & dota2_centrality <=0.6)
d_seventhgroup <- subset(subset_data, dota2_centrality > 0.6 & dota2_centrality <=0.7)
d_eighthgroup <- subset(subset_data, dota2_centrality > 0.7 & dota2_centrality <=0.8)
d_ninthgroup <- subset(subset_data, dota2_centrality > 0.8 & dota2_centrality <=0.9)
d_tenthgroup <- subset(subset_data, dota2_centrality > 0.9)

#Means for High, Med, Low Dota2 Centrality
d_low <- subset(subset_data, dota2_centrality <= 0.3)
d_med <- subset(subset_data, dota2_centrality > 0.3 & dota2_centrality <=0.7)
d_high <- subset(subset_data, dota2_centrality > 0.7)


#posts stats on centrality groupings
mean(firstgroup$total_posts) #2904.80
mean(firstgroup$gaming_posts) #112.96
mean(firstgroup$non_gaming_posts) #2781.83
mean(firstgroup$dota2_num_posts) #16.23
mean(firstgroup$dota2_centrality) # 0.02
mean(firstgroup$game_centrality) # 0.04

mean(secondgroup$total_posts) #1824.36
mean(secondgroup$gaming_posts) #226.81
mean(secondgroup$non_gaming_posts) #1557.54
mean(secondgroup$dota2_num_posts) #48.37
mean(secondgroup$dota2_centrality) #0.04
mean(secondgroup$game_centrality) #0.15

mean(thirdgroup$total_posts) #1677.65
mean(thirdgroup$gaming_posts) #414.82
mean(thirdgroup$non_gaming_posts) #1262.82
mean(thirdgroup$dota2_num_posts) #80.52
mean(thirdgroup$dota2_centrality) #0.07
mean(thirdgroup$game_centrality) #0.24

mean(fourthgroup$total_posts) #1569.37
mean(fourthgroup$gaming_posts) #545.93
mean(fourthgroup$non_gaming_posts) #1023.44
mean(fourthgroup$dota2_num_posts) #111.80
mean(fourthgroup$dota2_centrality) #0.11
mean(fourthgroup$game_centrality) #0.35

mean(fifthgroup$total_posts) #1423.96
mean(fifthgroup$gaming_posts) #639.38
mean(fifthgroup$non_gaming_posts) #784.58
mean(fifthgroup$dota2_num_posts)# 132.82
mean(fifthgroup$dota2_centrality) #0.14
mean(fifthgroup$game_centrality) #0.44

mean(sixthgroup$total_posts) #1438.86
mean(sixthgroup$gaming_posts) #788.94
mean(sixthgroup$non_gaming_posts) #649.91
mean(sixthgroup$dota2_num_posts) #179.43
mean(sixthgroup$dota2_centrality) #0.19
mean(sixthgroup$game_centrality) #0.55

mean(seventhgroup$total_posts) #1312.32
mean(seventhgroup$gaming_posts) #850.73
mean(seventhgroup$non_gaming_posts) #461.58
mean(seventhgroup$dota2_num_posts) #232.42
mean(seventhgroup$dota2_centrality) #0.24
mean(seventhgroup$game_centrality) #0.65

mean(eighthgroup$total_posts) #1264.90
mean(eighthgroup$gaming_posts) #947.47
mean(eighthgroup$non_gaming_posts) #317.42
mean(eighthgroup$dota2_num_posts) #283.19
mean(eighthgroup$dota2_centrality) #0.31
mean(eighthgroup$game_centrality) #0.75

mean(ninthgroup$total_posts) #1074.8
mean(ninthgroup$gaming_posts) #910.35
mean(ninthgroup$non_gaming_posts) #164.45
mean(ninthgroup$dota2_num_posts) #313.91
mean(ninthgroup$dota2_centrality) #0.41
mean(ninthgroup$game_centrality) #0.85

mean(tenthgroup$total_posts) #800.1
mean(tenthgroup$gaming_posts) #761.82
mean(tenthgroup$non_gaming_posts) #38.28
mean(tenthgroup$dota2_num_posts) #374.15
mean(tenthgroup$dota2_centrality) #0.59
mean(tenthgroup$game_centrality) #0.96

mean(d_firstgroup$total_posts) #2263.69
mean(d_firstgroup$gaming_posts) #442.40
mean(d_firstgroup$non_gaming_posts) #1821.29
mean(d_firstgroup$dota2_num_posts) #21.50
mean(d_firstgroup$dota2_centrality) # 0.02
mean(d_firstgroup$game_centrality) # 0.24

mean(d_secondgroup$total_posts) #1084.65
mean(d_secondgroup$gaming_posts) #356.69
mean(d_secondgroup$non_gaming_posts) #727.96
mean(d_secondgroup$dota2_num_posts) #155.95
mean(d_secondgroup$dota2_centrality) #0.14
mean(d_secondgroup$game_centrality) #0.15

mean(d_thirdgroup$total_posts) #1065.14
mean(d_thirdgroup$gaming_posts) #451.82
mean(d_thirdgroup$non_gaming_posts) #613.32
mean(d_thirdgroup$dota2_num_posts) #262.89
mean(d_thirdgroup$dota2_centrality) #0.25
mean(d_thirdgroup$game_centrality) #0.42

mean(d_fourthgroup$total_posts) #978.30
mean(d_fourthgroup$gaming_posts) #499.89
mean(d_fourthgroup$non_gaming_posts) #478.41
mean(d_fourthgroup$dota2_num_posts) #388.83
mean(d_fourthgroup$dota2_centrality) #0.35
mean(d_fourthgroup$game_centrality) #0.50

mean(d_fifthgroup$total_posts) #891.16
mean(d_fifthgroup$gaming_posts) #517.61
mean(d_fifthgroup$non_gaming_posts) #373.55
mean(d_fifthgroup$dota2_num_posts)# 400.13
mean(d_fifthgroup$dota2_centrality) #0.45
mean(d_fifthgroup$game_centrality) #0.57

mean(d_sixthgroup$total_posts) #882.88
mean(d_sixthgroup$gaming_posts) #578.52
mean(d_sixthgroup$non_gaming_posts) #304.35
mean(d_sixthgroup$dota2_num_posts) #483.41
mean(d_sixthgroup$dota2_centrality) #0.55
mean(d_sixthgroup$game_centrality) #0.64

mean(d_seventhgroup$total_posts) #860.913
mean(d_seventhgroup$gaming_posts) #626.09
mean(d_seventhgroup$non_gaming_posts) #234.82
mean(d_seventhgroup$dota2_num_posts) #559.33
mean(d_seventhgroup$dota2_centrality) #0.65
mean(d_seventhgroup$game_centrality) #0.72

mean(d_eighthgroup$total_posts) #828.74
mean(d_eighthgroup$gaming_posts) #668.62
mean(d_eighthgroup$non_gaming_posts) #160.12
mean(d_eighthgroup$dota2_num_posts) #619.27
mean(d_eighthgroup$dota2_centrality) #0.75
mean(d_eighthgroup$game_centrality) #0.80

mean(d_ninthgroup$total_posts) #705.76
mean(d_ninthgroup$gaming_posts) #623.94
mean(d_ninthgroup$non_gaming_posts) #81.82
mean(d_ninthgroup$dota2_num_posts) #599.11
mean(d_ninthgroup$dota2_centrality) #0.85
mean(d_ninthgroup$game_centrality) #0.88

mean(d_tenthgroup$total_posts) #588.31
mean(d_tenthgroup$gaming_posts) #568.46
mean(d_tenthgroup$non_gaming_posts) #19.85
mean(d_tenthgroup$dota2_num_posts) #563.10
mean(d_tenthgroup$dota2_centrality) #0.96
mean(d_tenthgroup$game_centrality) #0.97

#post stats for High, Med, Low Dota2 Centrality
mean(d_low$total_posts) #2113.76
mean(d_low$gaming_posts) #464.16
mean(d_low$non_gaming_posts) #1649.60
mean(d_low$dota2_num_posts) #65.32
mean(d_low$dota2_centrality) #0.06
mean(d_low$game_centrality) #0.28

mean(d_med$total_posts) #915.21
mean(d_med$gaming_posts) #543.99
mean(d_med$non_gaming_posts) #371.22
mean(d_med$dota2_num_posts) #424.56
mean(d_med$dota2_centrality) #0.47
mean(d_med$game_centrality) #0.59

mean(d_high$total_posts) #691.35
mean(d_high$gaming_posts) #613.5
mean(d_high$non_gaming_posts) #77.85
mean(d_high$dota2_num_posts) #589.94
mean(d_high$dota2_centrality) #0.87
mean(d_high$game_centrality) #0.90

#Randomly select 2000 people from each group (high med low)
d_low_rand2000 <- d_low[sample(nrow(d_low), 2000), ]
d_med_rand2000 <- d_med[sample(nrow(d_med), 2000), ]
d_high_rand2000 <- d_high[sample(nrow(d_high), 2000), ]

#mean
liwc_means <- colMeans(subset_data[sapply(subset_data, is.numeric)])
write.csv(liwc_means, file="liwc-means-DotA2.csv")

#Subsetted LIWC means (game centrality)
liwc_means_g1 <- colMeans(firstgroup[sapply(firstgroup, is.numeric)])
liwc_means_g2 <- colMeans(secondgroup[sapply(secondgroup, is.numeric)])
liwc_means_g3 <- colMeans(thirdgroup[sapply(thirdgroup, is.numeric)])
liwc_means_g4 <- colMeans(fourthgroup[sapply(fourthgroup, is.numeric)])
liwc_means_g5 <- colMeans(fifthgroup[sapply(fifthgroup, is.numeric)])
liwc_means_g6 <- colMeans(sixthgroup[sapply(sixthgroup, is.numeric)])
liwc_means_g7 <- colMeans(seventhgroup[sapply(seventhgroup, is.numeric)])
liwc_means_g8 <- colMeans(eighthgroup[sapply(eighthgroup, is.numeric)])
liwc_means_g9 <- colMeans(ninthgroup[sapply(ninthgroup, is.numeric)])
liwc_means_g10 <- colMeans(tenthgroup[sapply(tenthgroup, is.numeric)])

#Subsetted LIWC means (dota2 centrality)
d_liwc_means_g1 <- colMeans(d_firstgroup[sapply(firstgroup, is.numeric)])
d_liwc_means_g2 <- colMeans(d_secondgroup[sapply(secondgroup, is.numeric)])
d_liwc_means_g3 <- colMeans(d_thirdgroup[sapply(thirdgroup, is.numeric)])
d_liwc_means_g4 <- colMeans(d_fourthgroup[sapply(fourthgroup, is.numeric)])
d_liwc_means_g5 <- colMeans(d_fifthgroup[sapply(fifthgroup, is.numeric)])
d_liwc_means_g6 <- colMeans(d_sixthgroup[sapply(sixthgroup, is.numeric)])
d_liwc_means_g7 <- colMeans(d_seventhgroup[sapply(seventhgroup, is.numeric)])
d_liwc_means_g8 <- colMeans(d_eighthgroup[sapply(eighthgroup, is.numeric)])
d_liwc_means_g9 <- colMeans(d_ninthgroup[sapply(ninthgroup, is.numeric)])
d_liwc_means_g10 <- colMeans(d_tenthgroup[sapply(tenthgroup, is.numeric)])

#subsetted LIWC means (dota2 centrality High, Med, Low)
d_liwc_means_low <- colMeans(d_low[sapply(d_low, is.numeric)])
d_liwc_means_med <- colMeans(d_med[sapply(d_med, is.numeric)])
d_liwc_means_high <- colMeans(d_high[sapply(d_high, is.numeric)])


cent_liwc_means <- rbind(liwc_means_g1, liwc_means_g2, liwc_means_g3, liwc_means_g4, liwc_means_g5, liwc_means_g6, liwc_means_g7, liwc_means_g8, liwc_means_g9, liwc_means_g10)
d_cent_liwc_means <- rbind(d_liwc_means_g1, d_liwc_means_g2, d_liwc_means_g3, d_liwc_means_g4, d_liwc_means_g5, d_liwc_means_g6, d_liwc_means_g7, d_liwc_means_g8, d_liwc_means_g9, d_liwc_means_g10)
d_cent_liwc_means_hml <- rbind(d_liwc_means_low, d_liwc_means_med, d_liwc_means_high)
d_cent_liwc_means_hml_rand2000 <- rbind(d_liwc_means_rand2000low, d_liwc_means_rand2000med, d_liwc_means_rand2000high)

write.csv(d_cent_liwc_means_hml_rand2000, file="rand2000-d-cent-liwc-means-hml-DotA2.csv")

cent_liwc_means <- data.frame(cent_liwc_means)
d_cent_liwc_means <- data.frame(d_cent_liwc_means)
d_cent_liwc_means_hml <- data.frame(d_cent_liwc_means_hml)

d_cent_liwc_means_hml$exclusivity <- c("Low", "Medium", "High")

d_cent_liwc_means_hml$exclusivity <- factor(d_cent_liwc_means_hml$exclusivity, levels = c("Low", "Medium", "High"))

#calculate and add se's to dataset
library(plotrix)

d_low_authentic_se <- std.error(d_low$Authentic)
d_med_authentic_se <- std.error(d_med$Authentic)
d_high_authentic_se <- std.error(d_high$Authentic)

d_cent_liwc_means_hml$se_authentic <- c(d_low_authentic_se, d_med_authentic_se, d_high_authentic_se)


d_low_you_se <- std.error(d_low$you)
d_med_you_se <- std.error(d_med$you)
d_high_you_se <- std.error(d_high$you)

d_cent_liwc_means_hml$se_you <- c(d_low_you_se, d_med_you_se, d_high_you_se)

d_low_clout_se <- std.error(d_low$Clout)
d_med_clout_se <- std.error(d_med$Clout)
d_high_clout_se <- std.error(d_high$Clout)

d_cent_liwc_means_hml$se_clout <- c(d_low_clout_se, d_med_clout_se, d_high_clout_se)

d_low_tone_se <- std.error(d_low$Tone)
d_med_tone_se <- std.error(d_med$Tone)
d_high_tone_se <- std.error(d_high$Tone)

d_cent_liwc_means_hml$se_tone <- c(d_low_tone_se, d_med_tone_se, d_high_tone_se)

d_low_analytic_se <- std.error(d_low$Analytic)
d_med_analytic_se <- std.error(d_med$Analytic)
d_high_analytic_se <- std.error(d_high$Analytic)

d_cent_liwc_means_hml$se_analytic <- c(d_low_analytic_se, d_med_analytic_se, d_high_analytic_se)


d_low_affiliation_se <- std.error(d_low$affiliation)
d_med_affiliation_se <- std.error(d_med$affiliation)
d_high_affiliation_se <- std.error(d_high$affiliation)

d_cent_liwc_means_hml$se_affiliation <- c(d_low_affiliation_se, d_med_affiliation_se, d_high_affiliation_se)

d_low_i_se <- std.error(d_low$i)
d_med_i_se <- std.error(d_med$i)
d_high_i_se <- std.error(d_high$i)

d_cent_liwc_means_hml$se_i <- c(d_low_i_se, d_med_i_se, d_high_i_se)

d_low_we_se <- std.error(d_low$we)
d_med_we_se <- std.error(d_med$we)
d_high_we_se <- std.error(d_high$we)

d_cent_liwc_means_hml$se_we <- c(d_low_we_se, d_med_we_se, d_high_we_se)

d_low_swear_se <- std.error(d_low$swear)
d_med_swear_se <- std.error(d_med$swear)
d_high_swear_se <- std.error(d_high$swear)

d_cent_liwc_means_hml$se_swear <- c(d_low_swear_se, d_med_swear_se, d_high_swear_se)

d_low_anger_se <- std.error(d_low$anger)
d_med_anger_se <- std.error(d_med$anger)
d_high_anger_se <- std.error(d_high$anger)

d_cent_liwc_means_hml$se_anger <- c(d_low_anger_se, d_med_anger_se, d_high_anger_se)

d_low_cogproc_se <- std.error(d_low$cogproc)
d_med_cogproc_se <- std.error(d_med$cogproc)
d_high_cogproc_se <- std.error(d_high$cogproc)

d_cent_liwc_means_hml$se_cogproc <- c(d_low_cogproc_se, d_med_cogproc_se, d_high_cogproc_se)


d_low_social_se <- std.error(d_low$social)
d_med_social_se <- std.error(d_med$social)
d_high_social_se <- std.error(d_high$social)

d_cent_liwc_means_hml$se_social <- c(d_low_social_se, d_med_social_se, d_high_social_se)

d_low_thirdperson_se <- std.error(d_low$thirdperson)
d_med_thirdperson_se <- std.error(d_med$thirdperson)
d_high_thirdperson_se <- std.error(d_high$thirdperson)

d_cent_liwc_means_hml$se_thirdperson <- c(d_low_thirdperson_se, d_med_thirdperson_se, d_high_thirdperson_se)

d_low_posemo_se <- std.error(d_low$posemo)
d_med_posemo_se <- std.error(d_med$posemo)
d_high_posemo_se <- std.error(d_high$posemo)

d_cent_liwc_means_hml$se_posemo <- c(d_low_posemo_se, d_med_posemo_se, d_high_posemo_se)

d_low_negemo_se <- std.error(d_low$negemo)
d_med_negemo_se <- std.error(d_med$negemo)
d_high_negemo_se <- std.error(d_high$negemo)

d_cent_liwc_means_hml$se_negemo <- c(d_low_negemo_se, d_med_negemo_se, d_high_negemo_se)


#get author lists for rand2000 samples
authors_low_rand2000 <- d_low_rand2000['author']
authors_med_rand2000 <- d_med_rand2000['author']
authors_high_rand2000 <- d_high_rand2000['author']

rand2000_author_list <- rbind(authors_low_rand2000, authors_med_rand2000, authors_high_rand2000)

write.csv(rand2000_author_list, file="rand2000-author-list-DotA2.csv")


#Combine high med low data
d_low$level <- rep("low",nrow(d_low))
d_med$level <- rep("med",nrow(d_med))
d_high$level <- rep("high",nrow(d_high))

combined_data <- rbind(d_low, d_med, d_high)
combined_data <-data.frame(combined_data)

##Add factor scores to data
fac_scores_data <- read.csv("G:/My Drive/GradSchoolStuff-UT/Research-Data/Gaming Data/centrality analysis/in-depth-DotA2/MEM_hml_2000/vb-fac-scores.csv")
colnames(fac_scores_data)[colnames(fac_scores_data) == 'Filename'] <- 'author'
fac_scores_data$author <- gsub(".txt", "", fac_scores_data$author)

new_fac_scores <- data.frame(fac_scores_data[,c("author","FAC1","FAC2","FAC3","FAC4","FAC5","FAC6","FAC7","FAC8","FAC9","FAC10","FAC11","FAC12","FAC13","FAC14","FAC15","FAC16","FAC17","FAC18","FAC19","FAC20")])

ncombined <- merge(combined_data, new_fac_scores, by = "author", all.x = TRUE)

#reduce down to subset of 6000 people
n_combined_6000_subset <- ncombined[complete.cases(ncombined), ]

################################################################
###################ANALYSES#####################################
################################################################

library(ggplot2)
library(tidyquant)
library(gridExtra)

### COGNITIVE GRAPHS ###
#Analytic
analytic_graph <- ggplot(data=d_cent_liwc_means_hml, aes(x=exclusivity, y=Analytic, fill = exclusivity)) +
  geom_bar(stat="identity") +
  coord_cartesian(ylim=c(45, 50)) +
  geom_errorbar(aes(ymin=Analytic-se_analytic, ymax=Analytic+se_analytic), width=.2,
                position=position_dodge(.9)) +
  xlab("Centrality")+
  theme(legend.position="none",panel.border = element_blank(), 
        panel.grid.major = element_blank(),
        panel.grid.minor = element_blank(),
        panel.background = element_blank(),
        axis.line = element_line(colour = "grey"))+
  scale_fill_manual("legend", values = c("Low" = "seagreen2", "Medium" = "seagreen3", "High" = "seagreen4"))

#cogproc
cogproc_graph <- ggplot(data=d_cent_liwc_means_hml, aes(x=exclusivity, y=cogproc, fill = exclusivity)) +
  geom_bar(stat="identity") +
  coord_cartesian(ylim=c(10, 15)) +
  geom_errorbar(aes(ymin=cogproc-se_cogproc, ymax=cogproc+se_cogproc), width=.2,
                position=position_dodge(.9)) +
  xlab("Centrality")+
  theme(legend.position="none",panel.border = element_blank(), 
        panel.grid.major = element_blank(),
        panel.grid.minor = element_blank(),
        panel.background = element_blank(),
        axis.line = element_line(colour = "grey"))+
  scale_fill_manual("legend", values = c("Low" = "seagreen2", "Medium" = "seagreen3", "High" = "seagreen4"))

grid.arrange(analytic_graph, cogproc_graph, ncol=2)

### EMOTION GRAPHS ###
#PosEmo
posemo_graph <- ggplot(data=d_cent_liwc_means_hml, aes(x=exclusivity, y=posemo, fill = exclusivity)) +
  geom_bar(stat="identity") +
  coord_cartesian(ylim=c(4, 5)) +
  geom_errorbar(aes(ymin=posemo-se_posemo, ymax=posemo+se_posemo), width=.2,
                position=position_dodge(.9)) +
  xlab("Centrality")+
  theme(legend.position="none",panel.border = element_blank(), 
        panel.grid.major = element_blank(),
        panel.grid.minor = element_blank(),
        panel.background = element_blank(),
        axis.line = element_line(colour = "grey"))+
  scale_fill_manual("legend", values = c("Low" = "seagreen2", "Medium" = "seagreen3", "High" = "seagreen4"))

#NegEmo
negemo_graph <- ggplot(data=d_cent_liwc_means_hml, aes(x=exclusivity, y=negemo, fill = exclusivity)) +
  geom_bar(stat="identity") +
  coord_cartesian(ylim=c(2, 3)) +
  geom_errorbar(aes(ymin=negemo-se_negemo, ymax=negemo+se_negemo), width=.2,
                position=position_dodge(.9)) +
  xlab("Centrality")+
  theme(legend.position="none",panel.border = element_blank(), 
        panel.grid.major = element_blank(),
        panel.grid.minor = element_blank(),
        panel.background = element_blank(),
        axis.line = element_line(colour = "grey"))+
  scale_fill_manual("legend", values = c("Low" = "seagreen2", "Medium" = "seagreen3", "High" = "seagreen4"))

grid.arrange(posemo_graph, negemo_graph, ncol=2)

#Anger
anger_graph <- ggplot(data=d_cent_liwc_means_hml, aes(x=exclusivity, y=anger, fill = exclusivity)) +
  geom_bar(stat="identity") +
  coord_cartesian(ylim=c(1, 1.5)) +
  geom_errorbar(aes(ymin=anger-se_anger, ymax=anger+se_anger), width=.2,
                position=position_dodge(.9)) +
  xlab("Centrality")+
  theme(legend.position="none",panel.border = element_blank(), 
        panel.grid.major = element_blank(),
        panel.grid.minor = element_blank(),
        panel.background = element_blank(),
        axis.line = element_line(colour = "grey"))+
  scale_fill_manual("legend", values = c("Low" = "seagreen2", "Medium" = "seagreen3", "High" = "seagreen4"))

#Swear
swear_graph <- ggplot(data=d_cent_liwc_means_hml, aes(x=exclusivity, y=swear, fill = exclusivity)) +
  geom_bar(stat="identity") +
  coord_cartesian(ylim=c(0.5, 0.8)) +
  geom_errorbar(aes(ymin=swear-se_swear, ymax=swear+se_swear), width=.2,
                position=position_dodge(.9)) +
  xlab("Centrality")+
  theme(legend.position="none",panel.border = element_blank(), 
        panel.grid.major = element_blank(),
        panel.grid.minor = element_blank(),
        panel.background = element_blank(),
        axis.line = element_line(colour = "grey"))+
  scale_fill_manual("legend", values = c("Low" = "seagreen2", "Medium" = "seagreen3", "High" = "seagreen4"))

grid.arrange(anger_graph, swear_graph, ncol=2)

### SOCIAL GRAPHS ###
#Social
social_graph <- ggplot(data=d_cent_liwc_means_hml, aes(x=exclusivity, y=social, fill = exclusivity)) +
  geom_bar(stat="identity") +
  coord_cartesian(ylim=c(7.5, 11)) +
  geom_errorbar(aes(ymin=social-se_social, ymax=social+se_social), width=.2,
                position=position_dodge(.9)) +
  xlab("Centrality")+
  theme(legend.position="none",panel.border = element_blank(), 
        panel.grid.major = element_blank(),
        panel.grid.minor = element_blank(),
        panel.background = element_blank(),
        axis.line = element_line(colour = "grey"))+
  scale_fill_manual("legend", values = c("Low" = "seagreen2", "Medium" = "seagreen3", "High" = "seagreen4"))

#Affiliation
affiliation_graph <- ggplot(data=d_cent_liwc_means_hml, aes(x=exclusivity, y=affiliation, fill = exclusivity)) +
  geom_bar(stat="identity") +
  coord_cartesian(ylim=c(2, 2.5)) +
  geom_errorbar(aes(ymin=affiliation-se_affiliation, ymax=affiliation+se_affiliation), width=.2,
                position=position_dodge(.9)) +
  xlab("Centrality")+
  theme(legend.position="none",panel.border = element_blank(), 
        panel.grid.major = element_blank(),
        panel.grid.minor = element_blank(),
        panel.background = element_blank(),
        axis.line = element_line(colour = "grey"))+
  scale_fill_manual("legend", values = c("Low" = "seagreen2", "Medium" = "seagreen3", "High" = "seagreen4"))

grid.arrange(social_graph, affiliation_graph, ncol=2)

#i
i_graph <- ggplot(data=d_cent_liwc_means_hml, aes(x=exclusivity, y=i, fill = exclusivity)) +
  geom_bar(stat="identity") +
  coord_cartesian(ylim=c(3, 4.5)) +
  geom_errorbar(aes(ymin=i-se_i, ymax=i+se_i), width=.2,
                position=position_dodge(.9)) +
  xlab("Centrality")+
  theme(legend.position="none",panel.border = element_blank(), 
        panel.grid.major = element_blank(),
        panel.grid.minor = element_blank(),
        panel.background = element_blank(),
        axis.line = element_line(colour = "grey"))+
  scale_fill_manual("legend", values = c("Low" = "seagreen2", "Medium" = "seagreen3", "High" = "seagreen4"))

#we
we_graph <- ggplot(data=d_cent_liwc_means_hml, aes(x=exclusivity, y=we, fill = exclusivity)) +
  geom_bar(stat="identity") +
  coord_cartesian(ylim=c(0.3, 0.4)) +
  geom_errorbar(aes(ymin=we-se_we, ymax=we+se_we), width=.2,
                position=position_dodge(.9)) +
  xlab("Centrality")+
  theme(legend.position="none",panel.border = element_blank(), 
        panel.grid.major = element_blank(),
        panel.grid.minor = element_blank(),
        panel.background = element_blank(),
        axis.line = element_line(colour = "grey"))+
  scale_fill_manual("legend", values = c("Low" = "seagreen2", "Medium" = "seagreen3", "High" = "seagreen4"))

#you
you_graph <- ggplot(data=d_cent_liwc_means_hml, aes(x=exclusivity, y=you, fill = exclusivity)) +
  geom_bar(stat="identity") +
  coord_cartesian(ylim=c(2, 2.5)) +
  geom_errorbar(aes(ymin=you-se_you, ymax=you+se_you), width=.2,
                position=position_dodge(.9)) +
  xlab("Centrality")+
  theme(legend.position="none",panel.border = element_blank(), 
        panel.grid.major = element_blank(),
        panel.grid.minor = element_blank(),
        panel.background = element_blank(),
        axis.line = element_line(colour = "grey"))+
  scale_fill_manual("legend", values = c("Low" = "seagreen2", "Medium" = "seagreen3", "High" = "seagreen4"))

#thirdperson
thirdperson_graph <- ggplot(data=d_cent_liwc_means_hml, aes(x=exclusivity, y=thirdperson, fill = exclusivity)) +
  geom_bar(stat="identity") +
  coord_cartesian(ylim=c(1.5, 2.5)) +
  geom_errorbar(aes(ymin=thirdperson-se_thirdperson, ymax=thirdperson+se_thirdperson), width=.2,
                position=position_dodge(.9)) +
  xlab("Centrality")+
  theme(legend.position="none",panel.border = element_blank(), 
        panel.grid.major = element_blank(),
        panel.grid.minor = element_blank(),
        panel.background = element_blank(),
        axis.line = element_line(colour = "grey"))+
  scale_fill_manual("legend", values = c("Low" = "seagreen2", "Medium" = "seagreen3", "High" = "seagreen4"))

grid.arrange(i_graph, we_graph, you_graph, thirdperson_graph, ncol=4)

### LEADERSHIP (Clout) ###
clout_graph <- ggplot(data=d_cent_liwc_means_hml, aes(x=exclusivity, y=Clout, fill = exclusivity)) +
  geom_bar(stat="identity") +
  coord_cartesian(ylim=c(40, 60)) +
  geom_errorbar(aes(ymin=Clout-se_clout, ymax=Clout+se_clout), width=.2,
                position=position_dodge(.9)) +
  xlab("Centrality")+
  theme(legend.position="none",panel.border = element_blank(), 
        panel.grid.major = element_blank(),
        panel.grid.minor = element_blank(),
        panel.background = element_blank(),
        axis.line = element_line(colour = "grey"))+
  scale_fill_manual("legend", values = c("Low" = "seagreen2", "Medium" = "seagreen3", "High" = "seagreen4"))

clout_graph


### EXTRA GRAPHS ####

# Authentic
authenticity_graph <- ggplot(data=d_cent_liwc_means_hml, aes(x=exclusivity, y=Authentic, fill = exclusivity)) +
  geom_bar(stat="identity") +
  coord_cartesian(ylim=c(20, 45)) +
  geom_errorbar(aes(ymin=Authentic-se_authentic, ymax=Authentic+se_authentic), width=.2,
                position=position_dodge(.9)) +
  xlab("Centrality")+
  theme(legend.position="none",panel.border = element_blank(), 
        panel.grid.major = element_blank(),
        panel.grid.minor = element_blank(),
        panel.background = element_blank(),
        axis.line = element_line(colour = "grey"))+
  scale_fill_manual("legend", values = c("Low" = "seagreen2", "Medium" = "seagreen3", "High" = "seagreen4"))

authenticity_graph

#Tone
ggplot(data=d_cent_liwc_means_hml, aes(x=exclusivity, y=Tone, fill = exclusivity)) +
  geom_bar(stat="identity") +
  geom_errorbar(aes(ymin=Tone-se_tone, ymax=Tone+se_tone), width=.2,
                position=position_dodge(.9)) +
  scale_fill_manual("legend", values = c("Low" = "#906bff", "Medium" = "#6bb5ff", "High" = "#6bffb5"))






#Correlations and T-Tests
cor(subset_data$Authentic, subset_data$Clout)



t.test(d_med['Authentic'], d_high['Authentic'])

effsize <- escalc(measure="SMD",m1i=d_low.Clout.mean, d_low.Clout.sd, n1i=153115,                   
                  m2i=d_high.Clout.mean, sd2i=d_high.Clout.sd, n2i=9463,
                  data=rawdata,                   
                  var.names = c("delta", "v"))

### LIWC ANOVAS
library(DescTools)
library(lsr)

cogproc_aov <- aov(cogproc ~ level, data = combined_data)
summary(cogproc_aov)
TukeyHSD(cogproc_aov, data=combined_data)
etaSquared(cogproc_aov)

Analytic_aov <- aov(Analytic ~ level, data = combined_data)
summary(Analytic_aov)
TukeyHSD(Analytic_aov, data=combined_data)
etaSquared(Analytic_aov)

posemo_aov <- aov(posemo ~ level, data = combined_data)
summary(posemo_aov)
TukeyHSD(posemo_aov, data=combined_data)
etaSquared(posemo_aov)

negemo_aov <- aov(negemo ~ level, data = combined_data)
summary(negemo_aov)
TukeyHSD(negemo_aov, data=combined_data)
etaSquared(negemo_aov)

anger_aov <- aov(anger ~ level, data = combined_data)
summary(anger_aov)
TukeyHSD(anger_aov, data=combined_data)
etaSquared(anger_aov)

swear_aov <- aov(swear ~ level, data = combined_data)
summary(swear_aov)
TukeyHSD(swear_aov, data=combined_data)
etaSquared(swear_aov)

social_aov <- aov(social ~ level, data = combined_data)
summary(social_aov)
TukeyHSD(social_aov, data=combined_data)
etaSquared(social_aov)

affiliation_aov <- aov(affiliation ~ level, data = combined_data)
summary(affiliation_aov)
TukeyHSD(affiliation_aov, data=combined_data)
etaSquared(affiliation_aov)

i_aov <- aov(i ~ level, data = combined_data)
summary(i_aov)
TukeyHSD(i_aov, data=combined_data)
etaSquared(i_aov)

we_aov <- aov(we ~ level, data = combined_data)
summary(we_aov)
TukeyHSD(we_aov, data=combined_data)
etaSquared(we_aov)

you_aov <- aov(you ~ level, data = combined_data)
summary(you_aov)
TukeyHSD(you_aov, data=combined_data)
etaSquared(you_aov)

thirdperson_aov <- aov(thirdperson ~ level, data = combined_data)
summary(thirdperson_aov)
TukeyHSD(thirdperson_aov, data=combined_data)
etaSquared(thirdperson_aov)

clout_aov <- aov(Clout ~ level, data = combined_data)
summary(clout_aov)
TukeyHSD(clout_aov, data=combined_data)
etaSquared(clout_aov)

#Extra LIWC comparisons

tone_aov <- aov(Tone ~ level, data = combined_data)
summary(tone_aov)
TukeyHSD(tone_aov, data=combined_data)
etaSquared(tone_aov)


authenticity_aov <- aov(Authentic ~ level, data = combined_data)
summary(authenticity_aov)
TukeyHSD(authenticity_aov, data=combined_data)
etaSquared(authenticity_aov)





library(psych)

n_combined_6000_subset$level <- factor(n_combined_6000_subset$level)

fac1_aov <- aov(FAC1 ~ level, data = n_combined_6000_subset)
summary(fac1_aov)
TukeyHSD(fac1_aov, data=n_combined_6000_subset)
etaSquared(fac1_aov)

fac2_aov <- aov(FAC2 ~ level, data = n_combined_6000_subset)
summary(fac2_aov)
TukeyHSD(fac2_aov, data=n_combined_6000_subset)
etaSquared(fac2_aov)

fac3_aov <- aov(FAC3 ~ level, data = n_combined_6000_subset)
summary(fac3_aov)
TukeyHSD(fac3_aov, data=n_combined_6000_subset)
etaSquared(fac3_aov)

fac4_aov <- aov(FAC4 ~ level, data = n_combined_6000_subset)
summary(fac4_aov)
TukeyHSD(fac4_aov, data=n_combined_6000_subset)
etaSquared(fac4_aov)

fac5_aov <- aov(FAC5 ~ level, data = n_combined_6000_subset)
summary(fac5_aov)
TukeyHSD(fac5_aov, data=n_combined_6000_subset)
etaSquared(fac5_aov)

fac6_aov <- aov(FAC6 ~ level, data = n_combined_6000_subset)
summary(fac6_aov)
TukeyHSD(fac6_aov, data=n_combined_6000_subset)
etaSquared(fac6_aov)

fac7_aov <- aov(FAC7 ~ level, data = n_combined_6000_subset)
summary(fac7_aov)
TukeyHSD(fac7_aov, data=n_combined_6000_subset)
etaSquared(fac7_aov)

fac8_aov <- aov(FAC8 ~ level, data = n_combined_6000_subset)
summary(fac8_aov)
TukeyHSD(fac8_aov, data=n_combined_6000_subset)
etaSquared(fac8_aov)

fac9_aov <- aov(FAC9 ~ level, data = n_combined_6000_subset)
summary(fac9_aov)
TukeyHSD(fac9_aov, data=n_combined_6000_subset)
etaSquared(fac9_aov)

fac10_aov <- aov(FAC10 ~ level, data = n_combined_6000_subset)
summary(fac10_aov)
TukeyHSD(fac10_aov, data=n_combined_6000_subset)
etaSquared(fac10_aov)

fac11_aov <- aov(FAC11 ~ level, data = n_combined_6000_subset)
summary(fac11_aov)
TukeyHSD(fac11_aov, data=n_combined_6000_subset)
etaSquared(fac11_aov)

fac12_aov <- aov(FAC12 ~ level, data = n_combined_6000_subset)
summary(fac12_aov)
TukeyHSD(fac12_aov, data=n_combined_6000_subset)
etaSquared(fac12_aov)

fac13_aov <- aov(FAC13 ~ level, data = n_combined_6000_subset)
summary(fac13_aov)
TukeyHSD(fac13_aov, data=n_combined_6000_subset)
etaSquared(fac13_aov)

fac14_aov <- aov(FAC14 ~ level, data = n_combined_6000_subset)
summary(fac14_aov)
TukeyHSD(fac14_aov, data=n_combined_6000_subset)
etaSquared(fac14_aov)

fac15_aov <- aov(FAC15 ~ level, data = n_combined_6000_subset)
summary(fac15_aov)
TukeyHSD(fac15_aov, data=n_combined_6000_subset)
etaSquared(fac15_aov)

fac16_aov <- aov(FAC16 ~ level, data = n_combined_6000_subset)
summary(fac16_aov)
TukeyHSD(fac16_aov, data=n_combined_6000_subset)
etaSquared(fac16_aov)

fac17_aov <- aov(FAC17 ~ level, data = n_combined_6000_subset)
summary(fac17_aov)
TukeyHSD(fac17_aov, data=n_combined_6000_subset)
etaSquared(fac17_aov)

fac18_aov <- aov(FAC18 ~ level, data = n_combined_6000_subset)
summary(fac18_aov)
TukeyHSD(fac18_aov, data=n_combined_6000_subset)
etaSquared(fac18_aov)

fac19_aov <- aov(FAC19 ~ level, data = n_combined_6000_subset)
summary(fac19_aov)
TukeyHSD(fac19_aov, data=n_combined_6000_subset)
etaSquared(fac19_aov)

fac20_aov <- aov(FAC20 ~ level, data = n_combined_6000_subset)
summary(fac20_aov)
TukeyHSD(fac20_aov, data=n_combined_6000_subset)
etaSquared(fac20_aov)


cor_dota_exclusivity <- cor(n_combined_6000_subset[sapply(n_combined_6000_subset, is.numeric)])[,85]
write.csv(cor_dota_exclusivity, "exclusivity_cor_with_fac.csv")

d_low_6000 <- subset(n_combined_6000_subset, level=="low")
d_med_6000 <- subset(n_combined_6000_subset, level=="med")
d_high_6000 <- subset(n_combined_6000_subset, level=="high")

d_fac_means_low <- colMeans(d_low_6000[sapply(d_low_6000, is.numeric)])
d_fac_means_med <- colMeans(d_med_6000[sapply(d_med_6000, is.numeric)])
d_fac_means_high <- colMeans(d_high_6000[sapply(d_high_6000, is.numeric)])

d_fac_means_6000 <- rbind(d_fac_means_low, d_fac_means_med, d_fac_means_high)
d_fac_means_6000 <- data.frame(d_fac_means_6000)
d_fac_means_6000$levels <-c("Low", "Medium", "High")
d_fac_means_6000$levels  <- factor(d_fac_means_6000$levels , levels = c("Low", "Medium", "High"))


###MEM stderrors
d_low_FAC1_se <- std.error(d_low_6000$FAC1)
d_med_FAC1_se <- std.error(d_med_6000$FAC1)
d_high_FAC1_se <- std.error(d_high_6000$FAC1)

d_fac_means_6000$se_FAC1 <- c(d_low_FAC1_se, d_med_FAC1_se, d_high_FAC1_se)

d_low_FAC2_se <- std.error(d_low_6000$FAC2)
d_med_FAC2_se <- std.error(d_med_6000$FAC2)
d_high_FAC2_se <- std.error(d_high_6000$FAC2)

d_fac_means_6000$se_FAC2 <- c(d_low_FAC2_se, d_med_FAC2_se, d_high_FAC2_se)

d_low_FAC5_se <- std.error(d_low_6000$FAC5)
d_med_FAC5_se <- std.error(d_med_6000$FAC5)
d_high_FAC5_se <- std.error(d_high_6000$FAC5)

d_fac_means_6000$se_FAC5 <- c(d_low_FAC5_se, d_med_FAC5_se, d_high_FAC5_se)



####MEM ANOVA GRAPHS
# FAC1
FAC1_graph <- ggplot(data=d_fac_means_6000, aes(x=levels, y=FAC1, fill = levels)) +
  geom_bar(stat="identity") +
  #coord_cartesian(ylim=c(20, 45)) +
  geom_errorbar(aes(ymin=FAC1-se_FAC1, ymax=FAC1+se_FAC1), width=.2,
                position=position_dodge(.9)) +
  xlab("Centrality")+
  theme(legend.position="none",panel.border = element_blank(), 
        panel.grid.major = element_blank(),
        panel.grid.minor = element_blank(),
        panel.background = element_blank(),
        axis.line = element_line(colour = "grey"))+
  scale_fill_manual("legend", values = c("Low" = "seagreen2", "Medium" = "seagreen3", "High" = "seagreen4"))

FAC1_graph

FAC2_graph <- ggplot(data=d_fac_means_6000, aes(x=levels, y=FAC2, fill = levels)) +
  geom_bar(stat="identity") +
  #coord_cartesian(ylim=c(20, 45)) +
  geom_errorbar(aes(ymin=FAC2-se_FAC2, ymax=FAC2+se_FAC2), width=.2,
                position=position_dodge(.9)) +
  xlab("Centrality")+
  theme(legend.position="none",panel.border = element_blank(), 
        panel.grid.major = element_blank(),
        panel.grid.minor = element_blank(),
        panel.background = element_blank(),
        axis.line = element_line(colour = "grey"))+
  scale_fill_manual("legend", values = c("Low" = "seagreen2", "Medium" = "seagreen3", "High" = "seagreen4"))

FAC2_graph

FAC5_graph <- ggplot(data=d_fac_means_6000, aes(x=levels, y=FAC5, fill = levels)) +
  geom_bar(stat="identity") +
  #coord_cartesian(ylim=c(20, 45)) +
  geom_errorbar(aes(ymin=FAC5-se_FAC5, ymax=FAC5+se_FAC5), width=.2,
                position=position_dodge(.9)) +
  xlab("Centrality")+
  theme(legend.position="none",panel.border = element_blank(), 
        panel.grid.major = element_blank(),
        panel.grid.minor = element_blank(),
        panel.background = element_blank(),
        axis.line = element_line(colour = "grey"))+
  scale_fill_manual("legend", values = c("Low" = "seagreen2", "Medium" = "seagreen3", "High" = "seagreen4"))

FAC5_graph

grid.arrange(FAC1_graph, FAC2_graph, FAC5_graph, ncol=3)

#create wordclouds for MEM
word_facs <- read.csv('G:/My Drive/GradSchoolStuff-UT/Research-Data/Gaming Data/centrality analysis/in-depth-DotA2/MEM_hml_2000/fac-word-lists.csv')

word_facs<- data.frame(word_facs)

word_facs[is.na(word_facs)] <- 0 
library (wordcloud)

GEW <- wordcloud(words = word_facs$Game_Elements, freq = word_facs$GE_Freq, min.freq = 20, rotate = FALSE)

PTW <- wordcloud(words = word_facs$ProTeams, freq = word_facs$PT_Freq, min.freq = 0.2)

SW <- wordcloud(words = word_facs$Skill, freq = word_facs$S_Freq, min.freq = 0.1)

grid.arrange(GEW, PTW, SW)
