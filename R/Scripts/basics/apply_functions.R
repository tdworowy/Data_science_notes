#lapply (use for lists, if possible will performe as.list)
x <- list(a1=1:10, a2= rnorm(10))
y1 <- lapply(x, function(x){x ** 3})
y2 <- lapply(x, mean)

z <- 1:5
y3 <- lapply(z, runif,min=0,max=13)# runif arguments


#sapply (simplify results, use for anything)
y4 <- sapply(x, function(x){x ** 3})
y5 <- sapply(x, mean)


#apply (use for arrays)
m <- matrix(rnorm(200),20,10)
y6<- apply(m,2,mean) #2 use columns (second dimension)
y7<- apply(m,1,sum) # 1 use rows (first dimension)

ar <- array(rnorm(2 * 2 * 10),c(2,2,10))
y8<- apply(ar,c(1,2),mean) #average matrix in an array


#mapply (can by use for multiple lists)
y9 <-mapply(rep,1:4,4:1) # rep =repeat 
list(rep(1,4),rep(2,3),rep(3,2),rep(4,1)) # equivalent

#tapply (apply function over sobset of a vector)
x2 <-c(rnorm(10),runif(10),rnorm(10,1))
fa <- gl(3,10)
y10 <- tapply(x2,fa,mean) # returns factor
y11 <- tapply(x2,fa,mean, simplify = FALSE) #returns list
