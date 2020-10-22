require('caret')
require('kernlab')

#preprocessing with principal components analysis

data(spam)
in_train <- createDataPartition( y = spam$type, p = 0.75, list = FALSE)

traning <- spam[in_train,]
test <- spam[-in_train,]

m <- abs(cor(traning[,-58])) # 58 column is outcome
diag(m) <- 0
which(m > 0.8,arr.ind = TRUE) # find witch variables are correlated 

#2 variables
smallSpam <- traning[,c(34,32)] # take columns 34 and 32
prComp <- prcomp(smallSpam)

plot(prComp$x[,1],prComp$x[,2])
prComp$rotation

#all variables
type_color <- ((traning$type == "spam")* 1 + 1) # red spam, black not
prComp  <- prcomp(log10(traning[,-58] + 1))

plot(prComp$x[,1], prComp$x[,2], col = type_color, xlab = 'PC1', ylab = 'PC2')

#PCA witch caret
preProc <- preProcess(log10(traning[,-58] + 1), method = 'pca', pcaComp = 2)
spam_pc <- predict(preProc, log10(traning[,-58] + 1))

plot(spam_pc[,1], spam_pc[,2], col = type_color, xlab = 'PC1', ylab = 'PC2')

# use PC in training
model_fit <- train(type ~ ., method = 'glm',preProcess = 'pca', data = traning)
