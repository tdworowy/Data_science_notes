install.packages("gower")
install.packages("lava")
require('caret')
require('kernlab')

in_train <- createDataPartition( y = spam$type, p = 0.75, list = FALSE)

traning <- spam[in_train,]
test <- spam[-in_train,]

mean(traning$capitalAve)
sd(traning$capitalAve)

#Standardization - manual
trainCapitalAve <- traning$capitalAve
trainCapitalAveS <- (trainCapitalAve - mean(trainCapitalAve))/sd(trainCapitalAve)

mean(trainCapitalAveS)
sd(trainCapitalAveS)

#Standardization - preprocess
pre_obj <- preProcess(traning[,-58],method = c('center','scale'))
trainCapAveS <- predict(pre_obj, traning[,-58])$capitalAve
mean(trainCapAveS)
sd(trainCapAveS)

#apply to test set (need to use object created from training set)
testCapAveS <- predict(pre_obj, test[,-58])$capitalAve
mean(testCapAveS)
sd(testCapAveS)

#Standardization - preprocess in train function
model_fit <- train(type ~., data = traning, method = 'glm', preProcess=c('center','scale'))
model_fit
