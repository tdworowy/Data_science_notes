library(lattice)
library(datasets)

#scatter plot 1
xyplot(Ozone ~ Wind, data=airquality)

#scatter plot 2
airquality <- transform(airquality, Month=factor(Month))
xyplot(Ozone ~ Wind | Month, data=airquality, layout=c(5,1)) # by month

# scatter plot 3
set.seed(1410)
x <- rnorm(200)
f <- rep(0:1,each=100)
y <- x + f - f * x + rnorm(200, sd=0.5)
f <- factor(f, labels = c("G1","G2"))
xyplot(y ~ x | f, layout=c(2,1)) 

# custom panel function 1
xyplot(y ~ x | f, panel = function(x, y, ...){
  regression_line <- lm(y ~x)
  panel.xyplot(x, y, ...)
  panel.abline(h=median(y),lty=2, col="blue")
  panel.abline(h=mean(y),lty=2, col="green")
  panel.abline(regression_line, col="red")
}) 

# custom panel function 2 (same plot, different way to plot regression line)
xyplot(y ~ x | f, panel = function(x, y, ...){
  panel.xyplot(x, y, ...)
  panel.abline(h=median(y),lty=2, col="blue")
  panel.abline(h=mean(y),lty=2, col="green")
  panel.lmline(x,y, col="red")
}) 

# plot 4
library(nlme)
xyplot(weight ~ Time | Diet, BodyWeight)

# plot 5
data(airquality)
p <- xyplot(Ozone ~ Wind | factor(Month), data = airquality)