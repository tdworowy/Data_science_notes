# k-nearest neighbors algorithm (classification)
install.packages("FNN")
library(FNN)

data <- read.csv("Data/loan200.csv") 
data$outcome <- ordered(data$outcome, levels=c('paid off', 'default'))
new_data <- data[1,2:3, drop=FALSE]

knn_pred <- knn(train = data[-1,2:3], test = new_data, cl<-data[-1,1], k=20)
knn_pred

# add new feature using K-nn, new feature can be use in further modeling/classification process 
loan_data <- read.csv(file.path('Data', 'loan_data.csv'))
loan_data$outcome <- ordered(loan_data$outcome, levels=c('paid off', 'default'))


borrow_df <- model.matrix(~ -1 + dti + revol_bal + revol_util + open_acc +
                            delinq_2yrs_zero + pub_rec_zero, data=loan_data)

borrow_knn <- knn(borrow_df, test=borrow_df, cl=loan_data[, 'outcome'], prob=TRUE, k=20)

prob <- attr(borrow_knn, "prob")
borrow_feature <- ifelse(borrow_knn == 'default', prob, 1 - prob)
summary(borrow_feature)

loan_data$borrower_score <- borrow_feature
plot(borrow_feature)