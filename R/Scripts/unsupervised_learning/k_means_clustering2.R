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