install.packages("lmPerm")
library(lmPerm)
data <- read.csv("Data/four_sessions.csv")

head(data)
# one way ANOVA

summary(aovp(Time ~ Page, data = data))# permutation test
#  0.08894 - it means that 0.8% of the time the response rate among 4 pages
# might differ as much as was actually observer - is less than traditional p value - 5%

summary(aov(Time ~ Page, data = data)) # F-statistic (F-value)