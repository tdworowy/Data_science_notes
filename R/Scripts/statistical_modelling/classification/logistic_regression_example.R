library('MASS')
shuttle$auto <- 1 * (shuttle$use == "auto")
shuttle$headwind <- 1 * (shuttle$wind == "head")
fit1 <- glm(auto ~ headwind, data = shuttle, family = binomial)
exp(coef(fit1))

shuttle$auto <- 1 * (shuttle$use == "auto")
shuttle$headwind <- 1 * (shuttle$wind == "head")
fit2 <- glm(auto ~ headwind + magn, data = shuttle, family = binomial)
exp(coef(fit2))

plot(fit1)
plot(fit2)