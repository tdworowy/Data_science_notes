# example 1
url <- "http://d396qusza40orc.cloudfront.net/getdata%2Fdata%2Fss06hid.csv"
download.file(url,destfile = "Data/comm.csv",method = "curl")

data <- read.csv("Data/comm.csv")

filtered_data <-subset(data, data["VAL"] == 24 )
nrow(filtered_data)

#example 2
install.packages("tidyverse")
library(readxl)
library(data.table)
url <- "http://d396qusza40orc.cloudfront.net/getdata%2Fdata%2FDATA.gov_NGAP.xlsx"
download.file(url,destfile = "Data/gov_NGAP.xlsx",method = "curl")

data <- read_excel("Data/gov_NGAP.xlsx")
data <- data.table(data)
data <- data[18:23,7:15]

zpi_values <- sapply(data[,1],as.numeric)

ext_values <-sapply(data[,6],as.numeric)
sum(zpi_values*ext_values,na.rm=T)

#example3
install.packages("XML")
library("XML")

url <- "http://d396qusza40orc.cloudfront.net/getdata%2Fdata%2Frestaurants.xml"
download.file(url,destfile = "Data/restaurants.xml",method = "curl")

data <- xmlParse(file = "Data/restaurants.xml")
rootnode <- xmlRoot(data)
zipcodes <- xpathApply(rootnode,"//zipcode", xmlValue)

max_zip_code <- max(as.numeric(zipcodes))

# how many rows has zpicode == 21231
result <- as.numeric(zipcodes) == 21231
length(as.numeric(zipcodes)[result]) 