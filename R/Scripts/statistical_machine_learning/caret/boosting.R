require('caret')
require('ISLR')
require('ggplot2')

#boosting

data(Wage)

Wage <- subset(Wage, select = -c (logwage)) # remove logwage from data set
in_train <- createDataPartition( y = Wage$wage, p = 0.75, list = FALSE)

traning <- Wage[in_train,]
test <- Wage[-in_train,]

fit <- train(wage ~ ., method = 'gbm', data = traning, verbose = TRUE) # gbm: boosting with trees
fit

qplot(predict(fit,test), wage, data = test)