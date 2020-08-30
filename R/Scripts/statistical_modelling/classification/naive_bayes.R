install.packages("klaR")
library(klaR)
library(ggplot2)
data <- read.csv(file.path('Data', 'loan_data.csv'))
data$outcome <- ordered(data$outcome, levels=c('paid off', 'default'))

naive_model <- NaiveBayes(outcome ~ purpose_ + home_ + emp_len_, data=na.omit(data))

naive_model$table

plot(naive_model)

new_loan <- data[147, c("purpose_", "home_","emp_len_")]

row.names(new_loan) <- NULL

predict(naive_model, new_loan)



less_naive <- NaiveBayes(outcome ~ borrower_score + payment_inc_ratio + 
                           purpose_ + home_ + emp_len_, data = data)

stats <- less_naive$table[[1]]
ggplot(data.frame(borrower_score=c(0,1)), aes(borrower_score)) +
  stat_function(fun = dnorm, color='blue', linetype=1, 
                arg=list(mean=stats[1, 1], sd=stats[1, 2])) +
  stat_function(fun = dnorm, color='red', linetype=2, 
                arg=list(mean=stats[2, 1], sd=stats[2, 2])) +
  labs(y='probability')

new_loan <- data[147, c("borrower_score","payment_inc_ratio","purpose_", "home_","emp_len_")]
predict(less_naive, new_loan)

