#set folder_path
folder_path <- "C:/Users/mt34546/Desktop/SB_script_test"

files <- list.files(path = folder_path)

library(plyr)

for (f in files){
  filepath <- paste(folder_path , "/" , f, sep='')
  
  # if the merged dataset doesn't exist, create it
  if (!exists("dataset")){
    dataset <- read.csv(filepath)
  }
  
  # if the merged dataset does exist, append to it
  if (exists("dataset")){
    temp_dataset <- read.csv(filepath)
    dataset<-rbind.fill(dataset, temp_dataset)
    rm(temp_dataset)
  }

  
}

write.csv(dataset, file="C:/Users/mt34546/Desktop/SB_script_test/merged-csv-data-SB.csv")


