data(mtcars)

fit1 <- lm(mpg  ~ factor(cyl) + wt, data = mtcars)
fit2 <- lm(mpg  ~ factor(cyl), data = mtcars)
           
t.test(fit1$coefficients,fit2$coefficients)

fit3 <- lm(mpg ~ I(wt * 0.5) + factor(cyl), data = mtcars)

x <- c(0.586, 0.166, -0.042, -0.614, 11.72)
y <- c(0.549, -0.026, -0.127, -0.751, 1.344)

fit4 <- lm(x ~y)


x <- c(0.586, 0.166, -0.042, -0.614, 11.72)
y <- c(0.549, -0.026, -0.127, -0.751, 1.344)

fit5 <- lm(x ~y)
dfbeta(fit5)