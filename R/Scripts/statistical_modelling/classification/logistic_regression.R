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
