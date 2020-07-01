char_vector <- c("Test1", "aaa", "abc")
paste(char_vector, collapse = " ")

v1 <- c(1:10)
v2 <- c(10:20)
v3 <- c(v1, v2)

paste(LETTERS, 1:4, sep="-")

v4 <- -sample(c(v1,v2),2)


x <- sample(c(rnorm(1000), rep(NA,1000),200))
x[!is.na(x) & x >0]

