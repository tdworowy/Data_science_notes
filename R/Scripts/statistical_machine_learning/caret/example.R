install.packages('AppliedPredictiveModeling')
library(AppliedPredictiveModeling)
data(concrete)
library(caret)
library(ggplot2)

set.seed(1000)
inTrain = createDataPartition(mixtures$CompressiveStrength, p = 3/4)[[1]]
training = mixtures[ inTrain,]
testing = mixtures[-inTrain,]

qplot(x = CompressiveStrength, y = 1:nrow(training),color = Cement, data = training)
qplot(x = CompressiveStrength, y = 1:nrow(training),color = BlastFurnaceSlag , data = training)
qplot(x = CompressiveStrength, y = 1:nrow(training),color = Age, data = training)


qplot(Superplasticizer, data = training)

set.seed(3433)
data(AlzheimerDisease)
adData = data.frame(diagnosis,predictors)
inTrain = createDataPartition(adData$diagnosis, p = 3/4)[[1]]
training = adData[ inTrain,]
testing = adData[-inTrain,]

#_______

data(segmentationOriginal)

set.seed(125)
in_train <- createDataPartition( y = segmentationOriginal$Case , p = 0.75, list = FALSE)
training = segmentationOriginal[ in_train,]
testing = segmentationOriginal[-in_train,]

fit <- train(Case ~ ., data = training, nethod = 'rpart')

fit$finalModel