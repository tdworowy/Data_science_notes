library(ggplot2)
library(tidyr)

data <- read.csv("Data/sp500_data.csv")

oil <- data[, c("CVX","XOM")]

pca <- princomp(oil)
loadings <- pca$loadings

ggplot(data = oil, aes(x=CVX,y=XOM)) +
  geom_point() + 
  stat_ellipse(type = "norm", level=.99, color="green") +
  geom_abline(intercept = 0, slope = loadings[2,1]/loadings[1,1], color="red") + 
  geom_abline(intercept = 0, slope = loadings[2,2]/loadings[1,2], color="blue")
  


syms <- c( 'AAPL', 'MSFT', 'CSCO', 'INTC', 'CVX', 'XOM', 'SLB', 'COP',
           'JPM', 'WFC', 'USB', 'AXP', 'WMT', 'TGT', 'HD', 'COST')
top_sp <- data[row.names(data)>='2011-01-01', syms]

sp_pca <- princomp(top_sp)

par(mar=c(6,3,0,0)+.1, las=2)
screeplot(sp_pca, main='')

loadings <- sp_pca$loadings[,1:5]
loadings <- as.data.frame(loadings)
loadings$Symbol <- row.names(loadings)
loadings <- gather(loadings, 'Component', 'Weight', -Symbol)
loadings$Color = loadings$Weight > 0

ggplot(loadings, aes(x=Symbol, y=Weight, fill=Color)) +
  geom_bar(stat='identity', position='identity', width=.75) + 
  facet_grid(Component ~ ., scales='free_y') +
  guides(fill=FALSE)  +
  ylab('Component Loading') +
  theme_bw() +
  theme(axis.title.x=element_blank(),
        axis.text.x=element_text(angle=90, vjust=0.5))