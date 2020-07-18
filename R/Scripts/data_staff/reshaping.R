install.packages("reshape2")
library(reshape2)
data(mtcars)

# melting data frames
mtcars$carname <- rownames(mtcars)
carMelt <- melt(mtcars, id=c("carname","gear","cyl"), measure.vars=c("mpg","hp"))

#casting data frames
cylData1 <- dcast(carMelt, cyl ~ variable) # summarize by length of cyl
cylData2 <- dcast(carMelt, cyl ~ variable, mean) # summarize by mean of cyl

# example: sum count by spray (InsectSprays data set)
data(InsectSprays)
tapply(InsectSprays$count,InsectSprays$spray,sum)