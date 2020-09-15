set.seed(9999)

x <- rnorm(48, mean = rep(1:3,each=8),sd=0.2)
y <- rnorm(48, mean = rep(c(1,2,1),each=8),sd=0.2)

df <- data.frame(x,y)

k_means <- kmeans(df,centroids=3) # need to guess number of clusters in advance 

library(cluster)
clusplot(df, k_means$cluster, color=TRUE, shade=TRUE,
         labels=2, lines=0) # plot clusters


plot(x,y, col=k_means$cluster, pch=19) # color clusters on plot
points(k_means$centers, col = 1:3, pch=3, cex = 3, lwd = 3) # plot centroids 