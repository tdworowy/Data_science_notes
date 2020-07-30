# Base plot 1
library(datasets)
data(cars)
with(cars, plot(speed, dist))

# Base plot 2
with(subset(airquality, Month != 7), plot(Wind, Ozone, main ="Ozone and Wind", pch = 16, col = "blue"))
with(subset(airquality, Month == 7), points(Wind, Ozone, pch = 16, col="red"))
#add regression line 
model <- lm(Ozone ~ Wind, airquality)
abline(model,lwd=2)

# Base plot 3 (multiple plots)
model1 <- lm(Ozone ~ Wind, airquality)
model2 <- lm(Ozone ~ Solar.R, airquality)

par(mfrow = c(1,2))
with(airquality, {
  plot(Wind, Ozone, main="Ozone and wind")
  abline(model1,lwd=2)
  plot(Solar.R, Ozone, main="Ozone and Solar Radiation")
  abline(model2,lwd=2)
})

# Lattice plot
library(lattice)
state <- data.frame(state.x77, region=state.region) #data from lattice package
xyplot(Life.Exp ~ Income | region, data=state, layout=c(4,1))

#ggplot2 plot
install.packages("ggplot2")
library(ggplot2)
data(mpg)
qplot(displ,hwy, data=mpg)