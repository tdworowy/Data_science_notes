data <- read.csv("Data/res.csv")

data$zipWrong <- ifelse(data$zipCode < 0,TRUE, FALSE) # set zipWrong to TRUE if zipcode is negative

data$zipGroups <- cut(data$zipCode,breaks = quantile(data$zipCode)) # create categorical variable