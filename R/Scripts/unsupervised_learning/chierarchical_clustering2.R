library(ggplot2)


data <- read.csv("Data/sp500_data.csv")

syms1 <- c('GOOGL', 'AMZN', 'AAPL', 'MSFT', 'CSCO', 'INTC', 'CVX', 
           'XOM', 'SLB', 'COP', 'JPM', 'WFC', 'USB', 'AXP',
           'WMT', 'TGT', 'HD', 'COST')

df <- data[row.names(data) >= '2011-01-01', syms1]
d <- dist(t(df))
hcl <- hclust(d)

plot(hcl, ylab='distance', xlab='', sub='', main='')
cutree(hcl, k=4)