url <- "http://data.baltimorecity.gov/api/views/k5ry-ef3g/rows.csv?accessType=DOWNLOAD"
download.file(url,destfile = "Data/res.csv")

data <- read.csv("Data/res.csv")

summary(data)
str(data)

quantile(data$councilDistrict, na.rm = TRUE)
table(data$zipCode, useNA = "ifany") #useNA = "ifany" will count missing values
table(data$zipCode,data$policeDistrict)

sum(is.na(data$zipCode)) # count missing values
all(data$zipCode >0) # check if there are negative numbers

table(data$zipCode %in% c("21212", "21213")) # are there any zpipcodes with are either "21212" or "21213"
data[data$zipCode %in% c("21212", "21213"),]

print(object.size(data),units = "Mb")