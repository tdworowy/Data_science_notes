url <- "http://data.baltimorecity.gov/api/views/dz54-2aru/rows.csv?accessType=DOWNLOAD"
download.file(url,destfile = "Data/cameras.csv",method = "curl")
list.files("./Data")