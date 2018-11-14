library(foreign)
fall2015 <- read.spss("C:/Users/mohin/Dropbox/GradSchoolStuff(UT)/Research-Data/Canvas-Tower-Click-Data/Final-48hr-Fall2015-where-aggregate-by-eid.sav")
spring2016 <- read.spss("C:/Users/mohin/Dropbox/GradSchoolStuff(UT)/Research-Data/Canvas-Tower-Click-Data/Final-48hr-Spring2016-Where-aggregate-by-eid.sav")

#t-tests for age
age1 <- fall2015$Age
age2 <- spring2016$Age

t.test(age1,age2)

esc_t(p=0.0003824, grp1n = 1384, grp2n = 671)

#chisquared-tests for sex
sex1 <- data.frame(as.factor(fall2015$Sex))
sex2 <- data.frame(as.factor(spring2016$Sex))
sex1$semester <- 0
sex2$semester <- 1

names(sex1) <- c("Sex", "Semester")
names(sex2)<- c("Sex", "Semester")

sexdata <- rbind(sex1, sex2)
sex_table <- table(sexdata$Sex, sexdata$Semester)

chisq.test(sex_table, correct=FALSE)
library(esc)
esc_chisq(p = .677, totaln = 2055)

#t-tests for SAT
sat1 <- fall2015$SAT_Tot
sat2 <- spring2016$SAT_Tot

t.test(sat1, sat2)

esc_t(p=0.006, grp1n = 1384, grp2n = 671)

#t-tests for first time in college
FTIC1 <- fall2015$FTIC_enrolled_JWP
FTIC2 <- spring2016$FTIC_enrolled_JWP

t.test(FTIC1, FTIC2)

#chisquared tests for ethnicity

IsBlack <- data.frame(fall2015$Ethnicity == 1)
IsAsian <- data.frame(fall2015$Ethnicity == 2)
IsHispanic <- data.frame(fall2015$Ethnicity == 3)
IsWhite <- data.frame(fall2015$Ethnicity == 4)
IsNativeAm <- data.frame(fall2015$Ethnicity == 5)
IsPacIsl <- data.frame(fall2015$Ethnicity == 6)
IsOther <- data.frame(fall2015$Ethnicity == 7)

IsBlack$Semester <- 0
IsAsian$Semester <- 0
IsHispanic$Semester <- 0
IsWhite$Semester <- 0
IsNativeAm$Semester <- 0
IsPacIsl$Semester <- 0
IsOther$Semester <- 0

names(IsBlack) <- c("IsBlack", "Semester")
names(IsAsian) <- c("IsAsian", "Semester")
names(IsHispanic) <- c("IsHispanic", "Semester")
names(IsWhite) <- c("IsWhite", "Semester")
names(IsNativeAm) <- c("IsNAPI", "Semester")
names(IsPacIsl) <- c("IsNAPI", "Semester")
names(IsOther) <- c("IsOther", "Semester")

IsBlack[IsBlack == FALSE] <- 0
IsAsian[IsAsian == FALSE] <- 0
IsHispanic[IsHispanic == FALSE] <- 0
IsWhite[IsWhite == FALSE] <- 0
IsNativeAm[IsNativeAm == FALSE] <- 0
IsPacIsl[IsPacIsl == FALSE] <- 0
IsOther[IsOther == FALSE] <- 0


IsBlack2 <- data.frame(spring2016$Ethnicity_Black)
IsAsian2 <- data.frame(spring2016$Ethnicity_AsianAmerican)
IsHispanic2 <- data.frame(spring2016$Ethnicity_Hispanic)
IsWhite2 <- data.frame(spring2016$Ethnicity_White)
IsNativeAm2 <- data.frame(spring2016$Ethnicity_NativeAmerican)
IsPacIsl2 <- data.frame(spring2016$Ethnicity_PacificIslander)
IsOther2 <- data.frame(spring2016$Ethnicity_Other)

IsBlack2$Semester <- 1
IsAsian2$Semester <- 1
IsHispanic2$Semester <- 1
IsWhite2$Semester <- 1
IsNativeAm2$Semester <- 1
IsPacIsl2$Semester <- 1
IsOther2$Semester <- 1

names(IsBlack2) <- c("IsBlack", "Semester")
names(IsAsian2) <- c("IsAsian", "Semester")
names(IsHispanic2) <- c("IsHispanic", "Semester")
names(IsWhite2) <- c("IsWhite", "Semester")
names(IsNativeAm2) <- c("IsNAPI", "Semester")
names(IsPacIsl2) <- c("IsNAPI", "Semester")
names(IsOther2) <- c("IsOther", "Semester")

IsBlack2[is.na(IsBlack2)] <- 0
IsAsian2[is.na(IsAsian2)] <- 0
IsHispanic2[is.na(IsHispanic2)] <- 0
IsWhite2[is.na(IsWhite2)] <- 0
IsNativeAm2[is.na(IsNativeAm2)] <- 0
IsPacIsl2[is.na(IsPacIsl2)] <- 0
IsOther2[is.na(IsOther2)] <- 0

blackdata <- rbind(IsBlack, IsBlack2)
black_table <- table(blackdata$IsBlack, sexdata$Semester)

chisq.test(black_table, correct=FALSE)
esc_chisq(p = .245, totaln = 2055)

asiandata <- rbind(IsAsian, IsAsian2)
asian_table <- table(asiandata$IsAsian, sexdata$Semester)

chisq.test(asian_table, correct=FALSE)
esc_chisq(p = 0.0002328, totaln = 2055)

hispanicdata <- rbind(IsHispanic, IsHispanic2)
hispanic_table <- table(hispanicdata$IsHispanic, hispanicdata$Semester)

chisq.test(hispanic_table, correct=FALSE)
esc_chisq(p = 0.263, totaln = 2055)

whitedata <- rbind(IsWhite, IsWhite2)
white_table <- table(whitedata$IsWhite, whitedata$Semester)

chisq.test(white_table, correct=FALSE)
esc_chisq(p = 0.561, totaln = 2055)

napidata <- rbind(IsNativeAm, IsNativeAm2, IsPacIsl, IsPacIsl2)
napi_table <- table(napidata$IsNAPI, napidata$Semester)

chisq.test(napi_table, correct=FALSE)
esc_chisq(p = 0.002, totaln = 2055)

otherdata <- rbind(IsOther, IsOther2)
other_table <- table(otherdata$IsOther, otherdata$Semester)

chisq.test(other_table, correct=FALSE)

##Chisquared tests for people who didn't have click data/ we didn't use

#CR/NC
semester1 <- data.frame(crnc = 23, grade = 1546)
semester2 <- data.frame(crnc = 9, grade = 727)
crnc_data <- rbind(semester1, semester2)

chisq.test(crnc_data, correct=FALSE)
esc_chisq(p=.6419, totaln = 2305)

#dropped
s1 <- data.frame(drop = 78, grade = 1491)
s2 <- data.frame(drop = 3, grade = 733)
drop_data <- rbind(s1, s2)

chisq.test(drop_data, correct=FALSE)
esc_chisq(p=2.899e-08, totaln = 2305)

#no grade
sm1 <- data.frame(ng = 84, grade = 1485)
sm2 <- data.frame(ng = 53, grade = 683)
ng_data <- rbind(sm1, sm2)

chisq.test(ng_data, correct=FALSE)
esc_chisq(p=0.08032, totaln = 2305)
