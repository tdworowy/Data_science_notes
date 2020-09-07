library(rpart)
# use Recursive Partitioning Algorithm
# possible metrics  Gini impurity (similar to Gini 
# coefficient but coefficient works only for the binary classification)
# and entropy 
data <- read.csv("Data/loan3000.csv") 
data$outcome <- ordered(data$outcome, levels=c('paid off', 'default'))

loan_tree <- rpart(outcome ~ borrower_score + payment_inc_ratio, data = data,
                   control = rpart.control(cp=0.002)) # check also for 0.003, 0.005 etc

plot(loan_tree, uniform = TRUE, margin = 0.05)
text(loan_tree, cex=0.75)

loan_tree
