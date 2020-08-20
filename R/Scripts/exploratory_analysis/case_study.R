
clust_ <- function( hclust, lab=hclust$labels, lab.col=rep(1,length(hclust$labels)), hang=0.1,...){
  # function from https://github.com/DataScienceSpecialization/courses/blob/master/04_ExploratoryAnalysis/clusteringExample/myplclust.R
  y <- rep(hclust$height,2)
  x <- as.numeric(hclust$merge)
  y <- y[which(x<0)]
  x <- x[which(x<0)]
  x <- abs(x)
  y <- y[order(x)]
  x <- x[order(x)]
  plot( hclust, labels=FALSE, hang=hang, ... )
  text( x=x, y=y[hclust$order]-(max(hclust$height)*hang), 
        labels=lab[hclust$order], col=lab.col[hclust$order], 
        srt=90, adj=c(1,0.5), xpd=NA, ... )}



load("Data/SamsungData.rda")
names(samsungData)[1:12]

table(samsungData$activity)

#average acceleration for first subject
par(mfrow = c (1,2), mar = c(5,4,1,1))
samsungData <- transform(samsungData, activity = factor(activity))

subject1 <- subset(samsungData, subject == 1)

plot(subject1[,1], col=subject1$activity, ylab= names(subject1)[1], pch=19)
plot(subject1[,2], col=subject1$activity, ylab= names(subject1)[2], pch=19)
legend("bottomright",legend = unique(subject1$activity), col = unique(subject1$activity), pch=19)

#hierarchical clustering (average acceleration)
par(mfrow = c(1,1))
dist_matrix <- dist(subject1[, 1:3])
h_clust <- hclust(dist_matrix)
clust_(h_clust, lab.col =  unclass(subject1$activity))

#max acceleration for first subject
par(mfrow = c(1,2))
plot(subject1[,10], col=subject1 $activity, ylab= names(subject1)[10], pch=19)
plot(subject1[,11], col=subject1$activity, ylab= names(subject1)[11], pch=19)

#hierarchical clustering (max acceleration)
par(mfrow = c(1,1))
dist_matrix <- dist(subject1[, 10:12])
h_clust <- hclust(dist_matrix)
clust_(h_clust, lab.col =  unclass(subject1$activity))

#Singular value Decomposition
svd1 <- svd(scale(subject1[,-c(562,563)]))
par(mfrow = c(1,2))
plot(svd1$u[,1], col=subject1 $activity, pch=19)
plot(svd1$u[,2], col=subject1$activity, pch=19)

#maximum contributor
par(mfrow = c(1,1))
plot(svd1$v[, 2], pch=19)

max_contrib <- which.max(svd1$v[,2])
dist_matrix <- dist(subject1[, c(10:12, max_contrib)])
h_clust <- hclust(dist_matrix)
clust_(h_clust, lab.col =  unclass(subject1$activity))

names(samsungData)[max_contrib] # check what is max contributor


#k-means clustering
k_clust <- kmeans(subject1[, -c(562,563)], centers = 6, nstart = 200)
table(k_clust$cluster, subject1$activity)

#cluster 5 variable centers (laying)
plot(k_clust$center[5, 1:10], pch=19)

#cluster 1 variable centers (walking)
plot(k_clust$center[1, 1:10], pch=19)