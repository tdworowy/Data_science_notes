
expected <- rep(1,10)
steps <-  c()

for (i in 1:1000){
  step <-1
  while(TRUE){
    res <-sample(c(0,1),size=10,prob=c(0.5,0.5),replace=TRUE)
    step <- step + 1
    if(all(res == expected)){
      steps[i] <- step
      break()
    }
  }
}
mean(steps)
hist(steps)
sd(steps)