# Set the working directory
setwd("C:/Users/mt34546/Downloads")

#read in data
metadata <- read.csv("game_metadata_example.csv", header=TRUE)
liwcoutput <- read.csv("LIWC example.csv", header=TRUE)

# merge two data frames by ID
mergeddata <- merge(metadata,liwcoutput,by="Filename")

#correlations
cor(mergeddata$Liked, mergeddata[6:86])


#write to csv
write.csv(mergeddata, file = "mergeddata.csv", row.names=F)

