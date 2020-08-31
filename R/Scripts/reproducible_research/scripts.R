library(ggplot2)
url = "https://d396qusza40orc.cloudfront.net/repdata%2Fdata%2FStormData.csv.bz2"
file = "Data/FStormData.csv.bz2"
if(!file.exists(file)){
  download.file(url,destfile = file)
}
data <- read.csv(file)

ggplot(data, aes(x=EVTYPE,y=FATALITIES)) + 
  geom_bar(fill="red",stat="identity" ) + 
  ggtitle("Fatalities per event type") + 
  theme_dark()
