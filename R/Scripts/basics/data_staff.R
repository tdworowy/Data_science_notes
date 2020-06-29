
data <-  read.csv("data/hw1_data.csv")
nrow(data)
data["Ozone"][47,]

z <- is.nan(data["Ozone"])
length(data["Ozone"][z==TRUE])
mean(data["Ozone"][!z])


install.packages("dplyr")    
library(dplyr)

new_data <-  data %>% filter(Ozone >31 | Temp > 90)
mean(new_data[["Solar.R"]][!is.na(new_data["Solar.R"])])

june <-  data %>% filter(Month == 6)
may <- june <-  data %>% filter(Month == 5)

max(may[["Ozone"]][!is.na(may["Ozone"])])