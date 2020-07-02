column_mean  <- function(m, removeNA = TRUE) {
  column_count <- ncol(m)
  means <- numeric(column_count)
  for(i in 1:column_count) {
    means[i] <- mean(m[,i], na.rm = removeNA)
  }
  means #last expression is returned
}