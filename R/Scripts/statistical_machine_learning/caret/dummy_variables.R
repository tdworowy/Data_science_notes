install.packages("gower")
install.packages("lava")
require('caret')
require('ISLR')
require('splines')

#dummy variables

data(Wage)

in_train <- createDataPartition( y = Wage$wage, p = 0.75, list = FALSE)

traning <- Wage[in_train,]
test <- Wage[-in_train,]


#dummy variables
dummyies <- dummyVars(wage ~ jobclass, data = traning)
head(predict(dummyies, newdata = traning))

#remove zero covariates (features)
nsv <- nearZeroVar(traning, saveMetrics = TRUE)
nsv

#splin basis (can be useful in linear regression)
bsBasis <- bs(traning$age, df = 3) # create 3 polynomial values age ** 1 ate ** 2 and age ** 3
head(bsBasis)