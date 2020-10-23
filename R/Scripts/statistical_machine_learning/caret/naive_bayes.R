require('caret')
require('ggplot2')
require('rattle')

data(iris)

#example
in_train <- createDataPartition( y = iris$Species, p = 0.75, list = FALSE)

traning <- iris[in_train,]
test <- iris[-in_train,]

modlda <- train(Species ~ ., data = traning, method = 'lda') # linear discriminant analysis 
modnb <- train(Species ~ ., data = traning, method = 'nb')  # nb = naive Bayes

plda <- predict(modlda, test)
pnb <- predict(modnb, test)

table(plda,pnb)