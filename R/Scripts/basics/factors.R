#factors
factor1 <- factor(c("a","b","b","C","C"))
print(factor1)
factor2 <- factor(factor1, levels <- c("c","b","a")) #wierd thing happens
print(factor2)


factor3 <- factor(c("Atest","Btest","Btest", "Ctest","Ctest"), levels <- c("Ctest","Btest","Atest")) #workd ok
print(factor3)