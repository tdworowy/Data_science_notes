install.packages("randomForest")
library(randomForest)
library(ggplot2)

data <- read.csv("Data/loan_data.csv") 
data$outcome <- ordered(data$outcome, levels=c('paid off', 'default'))

rf <- randomForest(formula = outcome ~ ., # . means it will take all columns 
                   ntree =15, # default 500
                   data = data)

error_df <- data.frame(error_rate = rf$err.rate[,"OOB"], num_trees = 1:rf$ntree)

ggplot(error_df, aes(x = num_trees, y = error_rate)) +
  geom_line()


pred <- predict(rf, prob=TRUE)
rf_df <- cbind(data, pred = pred)

ggplot(data=rf_df, aes(x = borrower_score, y = payment_inc_ratio, shape = pred, color =  pred)) +
  geom_point(alpha = 0.6) + 
  scale_color_manual(values =  c('paid off' = '#b8e186', 'default' = '#d95f02')) + 
  scale_shape_manual(values =  c('paid off' = 0, 'default' = 1)) + 
  scale_size_manual(values =  c('paid off' = 0.5, 'default' = 2))