install.packages("kernlab")
library(kernlab)

data(spam)

# Sampling
set.seed(6543)
train_indicator <- rbinom(4601, size=1, prob=0.5)
table(train_indicator)

train_spam <- spam[train_indicator == 1,]
test_spam <- spam[train_indicator == 1,]

plot(train_spam$money~train_spam$type) # to skewed 

plot(log10(train_spam$money + 1)~train_spam$type) # not skewed 

plot(log10(train_spam[, 1:6]+1))

hclust <- hclust(dist(t(log10(train_spam[, 1:55]+1)))) # hierarchical clustering 
plot(hclust)

#logistic regression
library(boot)
train_spam$numType <- as.numeric(train_spam$type) - 1
cost_function <- function(x,y) sum(x !=(y > 0.5))
cv_error <- rep(NA, 55)

for (i in 1:55) {
  lm_formula <- reformulate(names(train_spam)[1], response = "numType")
  glm_fit <- glm(lm_formula, family = "binomial", data = train_spam)
  cv_error[i] <- cv.glm(train_spam, glm_fit, cost_function, 2)$delta[2]  
}

best_predictor <- names(train_spam)[which.min(cv_error)] 

#measure of uncertainty
prediction_model <- glm(numType ~ business, family="binomial", data = train_spam) # best predictor is business is (in that case, may change for multiple runs)
prediction_test <- predict(prediction_model, test_spam)
predict_spam <- rep("nonspam", dim(test_spam)[1])

predict_spam[prediction_model$fitted > 0.5] = "spam" # spam if probability of spam is >0.5

table(predict_spam, test_spam$type) # check test results 
