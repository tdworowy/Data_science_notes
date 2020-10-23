require('caret')
require('ggplot2')
require('rattle')
require('randomForest') # getTree function

data(iris)

#example
in_train <- createDataPartition( y = iris$Species, p = 0.75, list = FALSE)

traning <- iris[in_train,]
test <- iris[-in_train,]

fit <- train(Species ~., data = traning, method = 'rf', prox = TRUE) # rf == random forest

getTree(fit$finalModel, k = 2) # look on single tree
