#split
x <-c(rnorm(10),runif(10),rnorm(10,1))
y1 <- split(x,gl(3,10))

#example1
y3 <- lapply(split(x,gl(3,10)),mean) # works the same as tapply

#example2
data("iris")
splited_by_species <- split(iris,iris$Species)

#exampl3
x3 <- rnorm(10)
f1 <- gl(2,5)
f2 <- gl(5, 2)
y4 <- split(x, list(f1,f2),drop=TRUE) # drop=TRUE <- drop empty levels