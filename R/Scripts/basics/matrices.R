#Create matrices
vector1 <- c(10:20)
vector2 <- c(30:40)
matrix1 <- cbind(vector1,vector2)
matrix2 <- rbind(vector1,vector2)

print(matrix1)
print(matrix2)

matrix3 <- matrix(1:15, nrow = 5, ncol = 3)