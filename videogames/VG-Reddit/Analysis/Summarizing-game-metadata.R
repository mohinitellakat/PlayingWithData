#set directory
setwd("D:/Games")

#read in data
metadata <- read.csv("2018-04-20 - Extracted Reddit Data - Comments - MetaData.csv")

#aggregate data
library(doBy)
summaryBy(ups + downs + controversiality ~ author + subreddit, data = metadata, 
          FUN = function(x) { c(m = mean(x), s = sum(x), c=length(x)) } )

