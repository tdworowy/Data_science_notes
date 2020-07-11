library(descr)
# summarize the relationship between several categorical variables
data <- read.csv(file.path("Data","lcloans.csv"))

contingency_table <- CrossTable(data$grade, data$status, prop.c = FALSE, prop.chisq = FALSE, prop.t = FALSE)