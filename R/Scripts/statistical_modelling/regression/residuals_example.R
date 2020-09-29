library(ggplot2)

x <- runif(100, 0, 6); y <- x + rnorm(100,  mean = 0, sd = .001 * x); 
ggplot(data.frame(x = x, y = y), aes(x = x, y = y)) +
 geom_smooth(method = "lm", colour = "black") +
 geom_point(size = 7, colour = "black", alpha = 0.4) +
 geom_point(size = 5, colour = "red", alpha = 0.4) # regression line looks like perfect fit


 ggplot(data.frame(x = x, y = resid(lm(y ~ x))),aes(x = x, y = y)) + 
  geom_hline(yintercept = 0, size = 2) +
  geom_point(size = 7, colour = "black", alpha = 0.4) +
  geom_point(size = 5, colour = "red", alpha = 0.4) +
  xlab("X") + ylab("Residual") # but residual plot shows that there is increasing variation of y (heteroskedasticity)
# residual plot shouldn't have any visible patterns.