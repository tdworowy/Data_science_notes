# data.table is faster than data.fame
install.packages("data.table")
library(data.table)

dt1 <- data.table(x=rnorm(25),y=rep(c("a","b","c","d","e"),each=5),z=rnorm(25))
dt2 <- data.table(x=rnorm(50),y=rep(c("a","b","c","d","e"),each=10),z=rnorm(50))
head(dt1)
tables() #display all tables in memory

dt1[c(2,3)] #subset by rows
dt1[,c(2,3)] #subset by columns

dt1[,list(mean(x),sum(z))] # you can't do it in data.frame

dt1[,W:=z^2] # add new column

dt1[, m:= {
  temp <- (x+z)
  log2(temp+5)
}] # add new column, multi step operation 

setkey(dt1,y) #set key (can by use in search or merge(for two data.tables with same key))
dt1['a'] # search by key 