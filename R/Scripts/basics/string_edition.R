url <- "http://data.baltimorecity.gov/api/views/dz54-2aru/rows.csv?accessType=DOWNLOAD"
download.file(url,destfile = "Data/cameras.csv")

data <- read.csv("Data/cameras.csv")
tolower(names(data)) # to lower letters

split_names <- strsplit(names(data),"\\.") # split by "."
split_names <- sapply(split_names, function(x){x[1]}) # clean up (not perfect eg. X2010 is now duplicated)

test1 <- c("Test","Test_test", "test123")
sub("_","",test1) # remove "_"

test2 <- c("Test","Test_test_test_gets_www", "test123")
gsub("_","",test2) # remove "_" (works for multiple "_")