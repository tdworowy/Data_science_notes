library(boot)
data <- read.csv("Data/loans_income.csv")

stat_fun <- function(x, idx) median(x[idx])
boot_object <- boot(data, R=1000, statistic = stat_fun)