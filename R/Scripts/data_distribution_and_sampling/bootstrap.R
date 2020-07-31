library(boot)
data <- read.csv("Data/loans_income.csv")

stat_fun <- function(x, idx) median(x[idx,]) # use data median
boot_object <- boot(data, R=1000, statistic = stat_fun)

# density plot original
hist(data[["x"]], freq = FALSE)
lines(density(data[["x"]]), lwd=3, col="green") 

# density plot bootstrapped 1
hist(boot_object[["t"]], freq = FALSE)
lines(density(boot_object[["t"]]), lwd=3, col="green") 

stat_fun2 <- function(x, idx) x[idx,] # just resample data (with replacement)
boot_object2 <- boot(data, R=1000, statistic = stat_fun2)


# density plot bootstrapped 2
hist(boot_object2[["t"]], freq = FALSE)
lines(density(boot_object2[["t"]]), lwd=3, col="green") 