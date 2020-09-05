# k-means algorithm (classification)
install.packages("FNN")
library(FNN)

data <- read.csv("Data/loan200.csv") 
loan200$outcome <- ordered(loan200$outcome, levels=c('paid off', 'default'))
new_data <- data[1,2:3, drop=FALSE]

knn_pred <- knn(train = data[-1,2:3], test = new_data, cl<-data[-1,1], k=20)
knn_pred