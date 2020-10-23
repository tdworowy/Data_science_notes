require('caret')
require('ggplot2')
require('rattle')

data(iris)

#example
in_train <- createDataPartition( y = iris$Species, p = 0.75, list = FALSE)

traning <- iris[in_train,]
test <- iris[-in_train,]

qplot(Petal.Width, Sepal.Width, color = Species, data = traning)


fit <- train(Species ~., method = 'rpart', data = traning)
print(fit$finalModel)

plot(fit$finalModel, uniform = TRUE)
text(fit$finalModel, use.n = TRUE, all = TRUE, cex = 0.8)

fancyRpartPlot(fit$finalModel) # cool