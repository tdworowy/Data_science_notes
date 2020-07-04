
m <- matrix(1:15, nrow = 5, ncol = 3)
dput(m,file="test.R") # will generate file with R code with can generate object m 
dput(dput) # will display function code

rep(c(0,1,2), times = 10)
rep(c(0,1,2), each = 10)

my_seq1 <- seq(5,10, by = 0.3)
my_seq2 <- seq(5,10, length.out = 30)

seq_along(my_seq)


inst <- sample(12)
which(ints > 4)

library("swirl")
swirl() # courses