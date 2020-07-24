# 1
url <- "https://d396qusza40orc.cloudfront.net/getdata%2Fdata%2Fss06hid.csv"
download.file(url,"Data/2Fss06hid.csv")

data <- read.csv("Data/2Fss06hid.csv")
splited <- strsplit(names(data),"wgtp")

# 2
url <- "https://d396qusza40orc.cloudfront.net/getdata%2Fdata%2FGDP.csv"
download.file(url,"Data/2FGDP.csv")

data <- read.csv("Data/2FGDP.csv")
gpd <-ssub(",","",data[[5]])
mean <- mean(as.numeric(gpd[1:190]),na.rm = TRUE)

#3
url <- "https://d396qusza40orc.cloudfront.net/getdata%2Fdata%2FEDSTATS_Country.csv"
download.file(url,"Data/2FEDSTATS_Country.csv")

data2 <- read.csv("Data/2FEDSTATS_Country.csv")

library(dplyr)

data2_subset <- select(data2,CountryCode,Special.Notes)
data2_filtered <- filter(data2_subset, grepl("June",Special.Notes))

x <- as.vector(data[,1])
y <- as.vector(data2_filtered[,1])
unique(x) == unique(y)

#4
install.packages("quantmod")
library(quantmod)
amzn = getSymbols("AMZN",auto.assign=FALSE)
sampleTimes = index(amzn)



library(lubridate)
date <- ymd(sampleTimes)
years <- year(date)
years[years == 2012]
table(years)
