install.packages("xgboost")
library(xgboost)
library(ggplot2)

data <- read.csv("Data/loan3000.csv") 
data$outcome <- ordered(data$outcome, levels=c('paid off', 'default'))

predictors <- data.matrix(data[, c("borrower_score","payment_inc_ratio")])
label <- as.numeric(data[,"outcome"]) - 1

xgb <- xgboost(data = predictors, label = label, objective = "binary:logistic",
               params = list(subsample=0.65,eta=0.1 ),
               nrounds = 200)

pred <- predict(xgb, newdata = predictors)
xgb_df <- cbind(data, pred_default = pred >0.5, pob_defuld = pred)

ggplot(data = xgb_df, aes(x = borrower_score,y = payment_inc_ratio,
                          color = pred_default, shape = pred_default,
                          size = pred_default)) + 
  geom_point(alpha = .8) +
  scale_color_manual(values =  c('FALSE' = '#b8e186', 'TRUE' = '#d95f02')) + 
  scale_shape_manual(values =  c('FALSE' = 0, 'TRUE' = 1)) + 
  scale_size_manual(values =  c('FALSE' = 0.5, 'TRUE' = 2))

# fit witch all variables


data <- read.csv('Data/loan_data.csv')
data <- select(data, -X, -status)
data$outcome <- ordered(data$outcome, levels=c('paid off', 'default'))

predictors <- data.matrix(data[,-which(names(data) %in% 'outcome')])
label <- as.numeric(data$outcome)-1
test_idx <- sample(nrow(data), 10000)

xgb_default <- xgboost(data=predictors[-test_idx,], label=label[-test_idx], 
                       objective='binary:logistic', nrounds=250, verbose=0)

pred_default <- predict(xgb_default, predictors[test_idx,])
error_default <- abs(label[test_idx] - pred_default) > 0.5
xgb_default$evaluation_log[250,]
mean(error_default)


xgb_penalty <- xgboost(data=predictors[-test_idx,], label=label[-test_idx], 
                       params=list(eta=.1, subsample=.63, lambda=1000),
                       objective='binary:logistic', nrounds=250, verbose=0)
pred_penalty <- predict(xgb_penalty, predictors[test_idx,])
error_penalty <- abs(label[test_idx] - pred_penalty) > 0.5
xgb_penalty$evaluation_log[250,]
mean(error_penalty)

error_default <- rep(0, 250)
error_penalty <- rep(0, 250)
for(i in 1:250) {
  pred_default <- predict(xgb_default, predictors[test_idx,], ntreelimit=i)
  error_default[i] <- mean(abs(label[test_idx] - pred_default) > 0.5)
  pred_penalty <- predict(xgb_penalty, predictors[test_idx,], ntreelimit=i)
  error_penalty[i] <- mean(abs(label[test_idx] - pred_penalty) > 0.5)
}

errors <- rbind(xgb_default$evaluation_log,
                xgb_penalty$evaluation_log,
                data.frame(iter=1:250, train_error=error_default),
                data.frame(iter=1:250, train_error=error_penalty))

errors$type <- rep(c('default train', 'penalty train', 
                     'default test', 'penalty test'), rep(250, 4))


ggplot(errors, aes(x=iter, y=train_error, group=type)) +
  geom_line(aes(linetype=type, color=type), size=1) +
  scale_linetype_manual(values=c('solid', 'dashed', 'dotted', 'longdash')) +
  theme_bw() +
  theme(legend.key.width = unit(1.5,"cm")) +
  labs(x="Iterations", y="Error") +
  guides(color = guide_legend(override.aes = list(size=1)))

