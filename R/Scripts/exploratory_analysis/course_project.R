download.file("https://d396qusza40orc.cloudfront.net/exdata%2Fdata%2FNEI_data.zip",
              destfile = "Data/project2.zip")

unzip("Data/project2.zip")
NEI <- readRDS("Data/summarySCC_PM25.rds")
SCC <- readRDS("Data/Source_Classification_Code.rds")

#Plot 1
emissions_sum_by_year <- with(NEI, tapply(Emissions, year, sum, na.rm=TRUE))
dt <- data.frame(year = names(emissions_sum_by_year), emission_sum = emissions_sum_by_year)

with(dt,plot(x=year,y=emission_sum, type = "l", col = "blue",
             xlab = "Year", ylab = "Sum of emmission"))
dev.copy(jpeg,filename="plot1.png")
dev.off()

#plot 2
emissions_sum_by_year_baltimore <- with(subset(NEI,fips==24510), tapply(Emissions, year, sum, na.rm=TRUE))
dt <- data.frame(year = names(emissions_sum_by_year_baltimore), emission_sum = emissions_sum_by_year_baltimore)

with(dt,plot(x=year,y=emission_sum, type = "l", col = "blue",
             xlab = "Year", ylab = "Sum of emmission"))
dev.copy(jpeg,filename="plot2.png")
dev.off()

#plot 3
library(ggplot2)
baltimore <- subset(NEI,fips==24510)

ggplot(baltimore, aes(year, Emissions)) + 
  geom_abline() + 
  facet_grid(. ~ type) +
  geom_smooth(method = "lm") +
  theme_dark()

dev.copy(jpeg,filename="plot3.png")
dev.off()

#plot 4
library(ggplot2)
NEI_SCC <- merge(NEI, SCC,  by="SCC")
coal <- grepl("coal",NEI_SCC$EI.Sector, ignore.case = TRUE)
NEI_coal <- NEI_SCC[coal,]

ggplot(NEI_coal, aes(year, Emissions)) + 
  geom_abline() + 
  geom_smooth(method = "lm") +
  theme_dark()

dev.copy(jpeg,filename="plot4.png")
dev.off()


#plot 5
library(ggplot2)
NEI_SCC <- merge(NEI, SCC,  by="SCC")
vehicle <- grepl("vehicle",NEI_SCC$EI.Sector, ignore.case = TRUE)
NEI_vehicle <- NEI_SCC[vehicle,]
baltimore_vehicle <- subset(NEI_vehicle,fips==24510)

ggplot(baltimore_vehicle, aes(year, Emissions)) + 
  geom_abline() + 
  geom_smooth(method = "lm") +
  theme_dark()

dev.copy(jpeg,filename="plot5.png")
dev.off()

#plot 6
library(ggplot2)
NEI_SCC <- merge(NEI, SCC,  by="SCC")
vehicle <- grepl("vehicle",NEI_SCC$EI.Sector, ignore.case = TRUE)
NEI_vehicle <- NEI_SCC[vehicle,]
baltimore_la_vehicle <- subset(NEI_vehicle,fips %in% c("24510","06037"))

ggplot(baltimore_la_vehicle, aes(year, Emissions)) + 
  geom_abline() + 
  facet_grid(. ~ fips) +
  geom_smooth(method = "lm") +
  theme_dark()

dev.copy(jpeg,filename="plot6.png")
dev.off()