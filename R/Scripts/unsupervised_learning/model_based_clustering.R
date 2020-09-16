install.packages("mclust")
library(mclust)
library(ggplot2)

data <- read.csv("Data/sp500_data.csv")

df <- data[row.names(data)>='2011-01-01', c('XOM', 'CVX')]
mcl <- Mclust(df)
summary(mcl)

cluster <- factor(predict(mcl)$classification)
 ggplot(data=df, aes(x=XOM, y=CVX, color=cluster, shape=cluster)) +
  geom_point(alpha=.8) +
  theme_bw() +
  scale_shape_manual(values = c(1,2,3,4),
                     guide = guide_legend(override.aes=aes(size=2))) 
 

 plot(mcl, what="BIC", ask=FALSE)
 plot(mcl, what="classification", ask=FALSE)
 plot(mcl, what="uncertainty", ask=FALSE)
 plot(mcl, what="density", ask=FALSE)