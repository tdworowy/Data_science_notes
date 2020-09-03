data <- read.csv(file.path('Data', 'loan_data.csv'))
data$outcome <- ordered(data$outcome, levels=c('paid off', 'default'))

# gml stands for generalized linear model
logistic_model <- glm(outcome ~ payment_inc_ratio + purpose_ + home_ + emp_len_ + borrower_score, data=data,
                      family = 'binomial')

logistic_model
plot(logistic_model)

pred <- predict(logistic_model)
head(pred)

summary(pred)
summary(logistic_model)

# logistic generalized additive model
library(mgcv)
logistic_gam <- gam(outcome ~ s(payment_inc_ratio) + purpose_ + home_ + emp_len_ + s(borrower_score), data=data,
                    family = 'binomial')

pred <- predict(logistic_gam)
head(pred)

summary(pred)
summary(logistic_gam)


library(ggplot2)

partial_redid_plot <- function(model,variable, terms_variable){
  terms <- predict(model, type='terms')
  partial_resid <- resid(model) + terms
  
  df <- data.frame(payment_inc_ratio = data[,variable],
                   terms = terms[,terms_variable],
                   partial_resid = partial_resid[,terms_variable])
  
  ggplot(df, aes(x=payment_inc_ratio, y=partial_resid, solid=FALSE)) +
    geom_point(shape=46,alpha=0.4) +
    geom_line(aes(x=payment_inc_ratio, y=terms), color="red", size=1.5) +
    xlim(0, 25) +
    theme_bw()
}

# partial residuals for glm (linear)
partial_redid_plot(logistic_model,"payment_inc_ratio", "payment_inc_ratio")

# partial residuals for gam (non linear)
partial_redid_plot(logistic_gam,"payment_inc_ratio", "s(payment_inc_ratio)")

# top cloud correspondence to response 1 (default) and bottom to 0 (paid off)

# Confusion Matrix
pred <- predict(logistic_gam, newdata=data)

pred_y <- as.numeric(pred > 0)
true_y <- as.numeric(data$outcome=='default')
true_pos <- (true_y==1) & (pred_y==1)
true_neg <- (true_y==0) & (pred_y==0)

false_pos <- (true_y==0) & (pred_y==1)
false_neg <- (true_y==1) & (pred_y==0)

conf_mat <- matrix(c(sum(true_pos), sum(false_pos),
                     sum(false_neg), sum(true_neg)), 2, 2)
colnames(conf_mat) <- c('Predicted Y = 1', 'Predicted y = 0')
rownames(conf_mat) <- c('True Y = 1', 'True Y = 0')

conf_mat

# precision
conf_mat[1,1] / sum(conf_mat[,1])

# recall/sensitivity
conf_mat[1,1] / sum(conf_mat[1,])

# specificity
conf_mat[2,2] / sum(conf_mat[2,])

# accuracy
sum(conf_mat[1,1],conf_mat[2,2]) / sum(conf_mat)

# ROC (receiver operating characteristic) Curve
idx <- order(-pred)

recall <- cumsum(true_y[idx] == 1) / sum(true_y == 1)
specificity <- (sum(true_y == 0) - cumsum(true_y[idx] == 0)) / sum(true_y == 0)

roc_df <- data.frame(recall = recall, specificity = specificity)

ggplot(roc_df, aes(x=specificity, y=recall)) +
  geom_line(color='blue') + 
  scale_x_reverse(expand=c(0, 0)) +
  scale_y_continuous(expand=c(0, 0)) + 
  geom_line(data=data.frame(x=(0:100) / 100), aes(x=x, y=1-x),
            linetype='dotted', color='red') +
  theme_bw() + theme(plot.margin=unit(c(5.5, 10, 5.5, 5.5), "points"))


