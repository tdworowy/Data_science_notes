data <- read.csv("Data/avgpm25.csv", colClasses = c("numeric","character","factor","numeric","numeric"))

summary(data$pm25)

#box plot 1
boxplot(data$pm25, col="green")
abline(h=12)


#box plot 2
boxplot(pm25 ~ region, data=data, col="green")
abline(h=12, col="red")

#histogram 1
hist(data$pm25, col="green", breaks = 100)
rug(data$pm25)
abline(v=12, lwd=2)
abline(v=median(data$pm25),col="red",lwd=2) # plot median

#histogram 2
par(mfrow = c(2,1),mar=c(4,4,2,1))
hist(subset(data,region == "east")$pm25, col="green", breaks = 100)
hist(subset(data,region == "west")$pm25, col="green", breaks = 100)

#scatterplt 1
with(data, plot(latitude, pm25, col=region))
abline(h=12, lwd=2, lty=2)

#scatterplt 2
par(mfrow = c(1,2),mar=c(5,4,2,1))
with(subset(data,region == "east"), plot(latitude, pm25, main="East"))
abline(h=12, lwd=2, lty=2)
with(subset(data,region == "west"), plot(latitude, pm25, main="West"))
abline(h=12, lwd=2, lty=2)