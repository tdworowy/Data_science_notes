#remove NA

x1 <- c(1,2,NA,3,4,NA)
nans <- is.na(x1)
x2 <- x1[!nans]

x1
x2

x3 <- c(1,2,NA,3,4,NA,1,1,3)
x4 <- c(NA,2,NA,3,4,NA,6,7,8)

not_nans <- complete.cases(x3, x4)
x3[not_nans]
x4[not_nans]