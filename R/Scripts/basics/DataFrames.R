table1 <- data.frame(column1 = c(1:3), column2 = c("a","b","c"))
table2 <- data.frame(column1 = c(1:3), column2 =c(1:3))

cor(table2[c("column1","column2")])


table3 <- data.frame(column1 = c(1,2,3,NA,4), column2 =c(1,2,3,NA,NA))