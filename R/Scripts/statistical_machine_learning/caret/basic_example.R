install.packages("gower")
install.packages("lava")
install.packages("ISLR")
require('caret')
require('kernlab')
require('ISLR')
require('Hmisc')


data(spam)

#example
in_train <- createDataPartition( y = spam$type, p = 0.75, list = FALSE)

traning <- spam[in_train,]
test <- spam[-in_train,]

model_fit <- train(type ~., data = traning, method = 'glm')
model_fit

model_fit$finalModel

predictions <- predict(model_fit, newdata = test)

confusionMatrix(predictions, test$type)

#k-fold data splitting
folds <- createFolds(y = spam$type, k = 10, list = TRUE, returnTrain = TRUE)
sapply(folds, length)


#resampling
samples <- createResample(y = spam$type, times = 10, list = TRUE)
sapply(samples, length)

#Time Slices
time = 1:1000
slices <- createTimeSlices(y = time, initialWindow = 20,horizon = 10)
names(slices)

