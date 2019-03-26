#####Example Syntax for Meaning Extraction Method Analysis#####
#####Author: Kayla Jordan, modified by Mohini Tellakat ########
#Packages to install
install.packages("stringr")
install.packages("psych")
install.packages("GPArotation")

#Set your working directory. This should be the folder on your computer that has the files
#you want to use as well as where new files will be saved.
setwd("G:/My Drive/GradSchoolStuff-UT/Research-Data/Gaming Data/centrality analysis/in-depth-DotA2/MEM_hml_2000")

#Load MEH Output (either Binary or Verbose file)
data = read.csv("2019-03-07_MEH_DTM_Verbose(1).csv")

#Clean Filename Data (this will change depending on the exact format of the data)
library(stringr)
data$File = str_split_fixed(data$Filename, "__",3)[,1]
data$Obs = str_split_fixed(data$Filename, "__",3)[,2]
data$Pronoun_Match = str_split_fixed(data$Filename, "__",3)[,3]
data$Pronoun_Match = as.factor(noquote(data$Pronoun_Match))
#Code gender of Pronoun
data$Gender = as.factor(ifelse(data$Pronoun_Match=="his"|data$Pronoun_Match=="he"|
                       data$Pronoun_Match=="him", "Male", "Female"))

#Generate themes or topics
library(psych); library(GPArotation)

###################################
#####Code for finding themes#######
###################################
#Change number of variables (i.e. data[c(6:1006)]) and number of factors (i.e nfactors=20)
#Make sure to only include word frequencies as variables; use names(data) to look at the 
#names and number of variables in the data set
fac2 = principal(data[c(5:1251)], nfactors=20)
#To get a sense of how many factors to choose, look for a drop/break in the eigenvalues
#For example, if the 5th eigenvalue is 5.3 and the 6th is 4.8, then 5 factors may be a good solution
fac2$values
#Extract the factor loadings (which show which word clump together in a single theme)
#The first set of numbers in the brackets should be the number of variables and the 
#second set of numbers should be the number of factors. If you are unsure, you can use
#dim(fac10$loadings) which will tell you the numbers to use
x = fac2$loadings[1:1247,1:20]
#Write the loadings to a csv file. Make sure to change the name of the file if you are 
#running this multiple times or you will loss previous files you have saved.
write.csv(x, "Dota2 20 factors 1247 words.csv")

###################################
########USING SUBSETS of DATA######
###################################

#Split the data into male and female references
maledata = subset(data, Gender=="Male")
femaledata = subset(data, Gender=="Female")

#Analysis themes of male and female pronouns separately
#Test different numbers of factors and words
fac2M = principal(maledata[c(6:80)], nfactors=2)
fac2F = principal(femaledata[c(6:664)], nfactors=2)

#Extract the factor loadings
xM = fac2M$loadings[1:75,1:2]
xF = fac2F$loadings[1:75,1:2]

#Write to new files
write.csv(xM, "NYT 2 factors 75 words MALE.csv")
write.csv(xF, "NYT 2 factors 75 words FEMALE.csv")


#Extract the first five and last 4 columns
femaledata1 = as.data.frame(cbind(femaledata[,1:5],femaledata[,666:669]))
#Drop any word that wasn't used at all; just change the numbers to include all the word frequencies
for(i in 6:665){if(colSums(femaledata[i])!=0){femaledata1=cbind(femaledata1,femaledata[i])}}
#Run PCA on the word frequencies; change first number after c( to 10
fac2F = principal(femaledata1[c(10:668)], nfactors=2)

######################################
######Computing Factor Scores#########
######################################
#Change to data file which include the word frequencies (i.e. MEH Verbose output)
freq = read.csv("2019-03-07_MEH_DTM_Verbose(1).csv")
#Change to data file where each column includes the words in each theme. 
#The name of the themes should be the headers
comps = read.csv("word_lists.csv", stringsAsFactors = FALSE)

#Just run this entire fuction
compute_scores = function(frequencies, component_words)
{
  for(i in 1:ncol(component_words))
  {
    words = as.vector(as.character((component_words[,i])))
    words = words[words!=""]
    C1 = as.data.frame(apply(frequencies[,words], MARGIN = 1, sum))
    colnames(C1) = colnames(component_words[i])
    frequencies = cbind(frequencies, C1)
  }
  assign("data_scores", frequencies, .GlobalEnv)
}

#Arguments should be the frequency data and word lists for themes respectively
#The factor scores will be added to the frequency data in a new data frame, data_scores
compute_scores(freq, comps)

#######################
###Group Comparisons###
#######################

##t-tests for two-independent groups##
#Change the first variable to theme name
#Change the second to group categories (must be binary)
t.test(data_scores$Comp1~data_scores$Gender)
#If significant the 95 percent confidence interval will NOT include 0
#To report results: t(<insert df>) = <insert t>, p = <insert p-value>



