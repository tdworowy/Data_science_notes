library(ggplot2)

set.seed(667)
x <- rnorm(48, mean = rep(1:3,each=8),sd=0.2)
y <- rnorm(48, mean = rep(c(1,2,1),each=8),sd=0.2)

x_name <- "x"
y_name <- "y"

df <- data.frame(x,y)
names(df) <- c(x_name,y_name)


ggplot(df, aes(x,y)) + 
  geom_point()


distance <- dist(df) # calculate distant 
hlClustering <- hclust(distance) # clustering
plot(hlClustering) # dendrogram 

# K-Means Clustering with 5 clusters
fit <- kmeans(df, 3)


library(cluster)
clusplot(df, fit$cluster, color=TRUE, shade=TRUE,
         labels=2, lines=0)

clusplot(df, fit$cluster, color=TRUE, shade=TRUE)


ggplot(df, aes(x = x, y = y, color = fit$cluster)) + 
  geom_point()+
  stat_ellipse() # don't work
  
  