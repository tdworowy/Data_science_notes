# subseting
# vectors
x1 <- c(1,2,3,4,5,6,7)

x1[1]
x1[1:4]
x1[x1>4]

y <- x1 > 3
x1[y]

#lists
x2 <- list(test1 = 1:4,test2 = "a")
x2[1] # retruns list
x2[[1]] # retruns vector
x2$test1
x2$test2

x2["test1"]
x2[["test1"]]

#matrices
m <- matrix(1:6, 2, 3)
m[1,2] # returns vector
m[2,1] # returns vector
m[1,]  # returns vector
m[,1]  # returns vector

m[1, drop = FALSE] # returns matrix
m[1, , drop = FALSE] # returns matrix
