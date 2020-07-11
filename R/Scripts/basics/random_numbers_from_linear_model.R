set.seed(13)
x <- rnorm(200)
e <- rnorm(200,0,2)

y <- 0.5 + 2 * x + e

summary(y)
str(y)
plot(x,y)