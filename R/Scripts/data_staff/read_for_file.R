
data <- file("Data/getdata_wksst8110.for")
lines <- readLines(data)
lines <- lines[5:length(lines)]
data_frame <- data.frame(lines) # todo