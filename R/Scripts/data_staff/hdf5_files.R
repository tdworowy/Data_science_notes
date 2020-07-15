install.packages("BiocManager")
BiocManager::install(c("rhdf5"))
library(rhdf5)

file_path <- "Data/example.h5"
file <- h5createFile(file_path) 

h5createGroup(file_path,"Test1")
h5createGroup(file_path,"Test2")
h5createGroup(file_path,"Test1/Test1.1")


m1 <- matrix(rnorm(1000),nr=100,nc=10)
h5write(m1,file_path,"Test1/matrix")


h5ls(file_path)

h5read(file_path, "Test1/matrix")