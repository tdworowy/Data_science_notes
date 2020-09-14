
m <- matrix(rnorm(400), nrow=40)

image(1:10, 1:40, t(m)[,nrow(m):1]) # heatmap

heatmap(m) # heatmap witch hierarchical cluster analysis

# no pattern in data

# add pattern to data
for (i in 1:40) {
  flip <- rbinom(1, size=1, prob=0.5)
  if(flip) {
    m[i,] <- m[i,] + rep(c(0,3),each=5)
  }
}

heatmap(m)  # pattern is viable (columns)

hh <- hclust(dist(m))
m_ordered <- m[hh$order,]

par(mfrow = c(1,3))
image(t(m_ordered)[, nrow(m_ordered):1])
plot(rowMeans(m_ordered), 40:1, pch=19)
plot(colMeans(m_ordered), pch=19)



#SVD - singular value decomposition  

svd1 <- svd(scale(m_ordered))

par(mfrow = c(1,3))
image(t(m_ordered)[, nrow(m_ordered):1])
plot(svd1$u[,1], 40:1, pch=19)
plot(svd1$v[,1], pch=19)

# Components of the SVD
# Variance explained

par(mfrow = c(1,2))
plot(svd1$d, pch=19, xlab="Columns", ylab="Singular value") # Singular value, each singular value representing the percent of
                     # the total variation in your dataset that's explained by that particular component.

plot(svd1$d^2/sum(svd1$d^2), pch=19,xlab="Columns", ylab="Proportion (percent) of variance explained") # same plot as before but scaled

# relationship to principal component
pca1 <- prcomp(m_ordered, scale = TRUE)
plot(pca1$rotation[, 1], svd1$v[,1], pch = 19, xlab="Principal component 1", ylab="Right singular vactor 1")
abline(lm(pca1$rotation[, 1] ~ svd1$v[,1]))

# principal component is basically the same think as Singular value 


# add second pattern to data
for (i in 1:40) {
  flip1 <- rbinom(1, size=1, prob=0.5)
  flip2 <- rbinom(1, size=1, prob=0.5)
  if(flip1) {
    m[i,] <- m[i,] + rep(c(0,3),each=5)
  }
  if(flip2) {
    m[i,] <- m[i,] + rep(c(0,3),5)
  }
}

hh <- hclust(dist(m))
m_ordered <- m[hh$order,]

svd2 <- svd(scale(m_ordered))

par(mfrow = c(1,4))
image(t(m_ordered)[, nrow(m_ordered):1])
plot(svd2$u[,1], 40:1, pch=19)
plot(svd2$v[,1], pch=19) # first right singular vector
plot(svd2$v[,2], pch=19) # second right singular vector

# Variance explained
par(mfrow = c(1,2))
plot(svd2$d, pch=19, xlab="Columns", ylab="Singular value") 
plot(svd2$d^2/sum(svd2$d^2), pch=19,xlab="Columns", ylab="Proportion (percent) of variance explained") 



