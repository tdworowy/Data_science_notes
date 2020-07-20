url <- "https://d396qusza40orc.cloudfront.net/getdata%2Fdata%2Fss06hid.csv"
download.file(url,"Data/2Fss06hid.csv")

data <- read.csv("Data/2Fss06hid.csv")
library(dplyr)
agriculture <- filter(data, ACR ==3, AGS == 6)
agricultureLogical <- data$ACR==3 & data$AGS==6
which(agricultureLogical)

#read jpg
install.packages("jpeg")
library(jpeg)
url <- "https://d396qusza40orc.cloudfront.net/getdata%2Fjeff.jpg"
download.file(url,"Data/getdata_jeff.jpg")
data_jpg <- readJPEG("Data/getdata_jeff.jpg",native=TRUE)

quantile(data_jpg,probs = c(0.30, 0.80))

## next one
url1 <- "https://d396qusza40orc.cloudfront.net/getdata%2Fdata%2FGDP.csv"
url2 <- "https://d396qusza40orc.cloudfront.net/getdata%2Fdata%2FEDSTATS_Country.csv"
download.file(url1,"Data/2FGDP.csv")
download.file(url2,"Data/2FEDSTATS_Country.csv")

data1 <- read.csv("Data/2FGDP.csv")
data2<- read.csv("Data/2FEDSTATS_Country.csv")



z <-data1$X
x <-data2$CountryCode

sum(table(z[z %in% x]))
