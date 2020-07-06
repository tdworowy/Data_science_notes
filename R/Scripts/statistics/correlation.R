# get sp500 data
library(TTR)
data(speed)
sp500 <- getYahooData('^GSPC',start=20100101,end=20200628,freq='daily')
ep <- endpoints(sp500, on="months", k=1)
sp500 <- sp500[ep[2:(length(ep)-1)]]
sp500$sp500_ret <- log(sp500$Close) - lag(log(sp500$Close))
sp500 <- na.exclude(sp500)

library(corrplot)
corrplot(cor(sp500),method = "ellipse")
corrplot(cor(sp500),method = "color")
corrplot(cor(sp500),method = "number")

#example2
library(boot)
data("catsM")

corrplot(cor(catsM[c("Bwt","Hwt")]))

#example3
data("melanoma")
corrplot(cor(melanoma))