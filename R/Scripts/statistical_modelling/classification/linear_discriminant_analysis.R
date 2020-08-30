library(MASS)
library(ggplot2)

data <- read.csv(file.path('Data', 'loan3000.csv'))
data$outcome <- ordered(data$outcome, levels=c('paid off', 'default'))

loan_lda <- lda(outcome ~ borrower_score + payment_inc_ratio, data=na.omit(data))

loan_lda$scaling

pred <- predict(loan_lda) # probability of "default" and "paid off"
head(pred$posterior) 


pred <- predict(loan_lda)
lda_df <- cbind(data, prob_default=pred$posterior[,'default'])

center <- 0.5 * (loan_lda$mean[1, ] + loan_lda$mean[2, ])
slope <- -loan_lda$scaling[1] / loan_lda$scaling[2]
intercept = center[2] - center[1] * slope

ggplot(data=lda_df, aes(x=borrower_score, y=payment_inc_ratio, color=prob_default)) +
  geom_point(alpha=.6) +
  scale_color_gradientn(colors=c('#ca0020', '#f7f7f7', '#0571b0')) +
  scale_x_continuous(expand=c(0,0)) + 
  scale_y_continuous(expand=c(0,0), lim=c(0, 20)) + 
  geom_abline(slope=slope, intercept=intercept, color='darkgreen') +
  theme_dark()