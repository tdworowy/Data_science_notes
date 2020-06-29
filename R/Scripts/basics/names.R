#add names to vectro
vector <- 1:3
names(vector) <- c("name1","name2","name3")
print(vector)

#add names to metrics
m <- matrix(1:4, nrow = 2, ncol = 2)
dimnames(m) <- list(c("A","B"), c("C","D"))
print(m)

