column_mean  <- function(m, removeNA = TRUE) {
  column_count <- ncol(m)
  means <- numeric(column_count)
  for(i in 1:column_count) {
    means[i] <- mean(m[,i], na.rm = removeNA)
  }
  means #last expression is returned
}

# Custom operatpr
"%p%" <- function(x,y){ 
  paste(x,y)
  
}
# using ...
test <- function(...){
  args <- list(...)
  x1 <- args[1]
  x2 <- args[2]
  x3 <- args[3]
  paste(x1,x2,x3)
}