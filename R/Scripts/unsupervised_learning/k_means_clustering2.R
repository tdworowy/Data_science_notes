library(ggplot2)
library(tidyr)

data <- read.csv("Data/sp500_data.csv")
oil <- data[row.names(data)>="2011-01-01", c("CVX","XOM")]

km <- kmeans(oil,centers = 4)


oil$cluster <- factor(km$cluster)
centers <- data.frame(cluster = factor(1:4), km$centers)

ggplot(data=oil, aes(x = XOM,y = CVX, color = cluster, shape = cluster)) +
  geom_point(alpha = 0.5) + 
  geom_point(data = centers, aes(x = XOM,y = CVX, size = 3, stroke = 2, color = "black"))


syms <- c( 'AAPL', 'MSFT', 'CSCO', 'INTC', 'CVX', 'XOM', 'SLB', 'COP',
           'JPM', 'WFC', 'USB', 'AXP', 'WMT', 'TGT', 'HD', 'COST')
top_sp <- data[row.names(data)>='2011-01-01', syms]

km <- kmeans(top_sp,centers = 5, nstart = 10)

km$size

centers <- as.data.frame(t(km$centers))
names(centers) <- paste("Cluster", 1:5)
centers$Symbol <- row.names(centers)
centers <- gather(centers, "Cluster", "Mean", -Symbol)
centers$Color <- centers$Mean > 0

ggplot(centers, aes(x = Symbol, y = Mean, fill = Color)) + 
  geom_bar(stat="identity", position = "identity", width=.75) +
  facet_grid(Cluster ~ ., scales = "free_y")


# try to find best number of clusters (how many clusters explains most of data variance)
pct_var <- data.frame(pct_var = 0, num_clusters = 2:20)
totals <- kmeans(top_sp, centers = 20, nstart = 50, iter.max = 100)$totss

for(i in 2:20) {
  kmCluster <- kmeans(top_sp, centers = i, nstart = 50, iter.max = 100)
  pct_var[i-1,'pct_var'] <- kmCluster$betweenss / totals
}

ggplot(pct_var, aes(x=num_clusters, y=pct_var)) +
  geom_line() +
  geom_point() +
  labs(y='% Variance Explained', x='Number of Clusters') +
  scale_x_continuous(breaks=seq(2, 20, by=2))   +
  theme_dark()