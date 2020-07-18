library(boot)
data <- read.csv("Data/loans_income.csv")

stat_fun <- function(x, idx) median(x[idx,])
boot_object <- boot(data, R=1000, statistic = stat_fun)

# density plot original
hist(data[["x"]], freq = FALSE)
lines(density(data[["x"]]), lwd=3, col="green") 

# density plot bootstrapped
hist(boot_object[["t"]], freq = FALSE)
lines(density(boot_object[["t"]]), lwd=3, col="green") 