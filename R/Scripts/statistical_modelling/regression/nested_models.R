data(swiss)

fit1 <- lm(Fertility ~ Agriculture, data = swiss)
fit2 <- update(fit1, Fertility ~ Agriculture + Examination + Education, data = swiss)
fit3 <- update(fit1, Fertility ~ Agriculture + Examination + Education + Catholic + Infant.Mortality, data = swiss)

result <- anova(fit1, fit2, fit3)

result
summary(result)
plot(result)