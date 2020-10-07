library(ggplot2)
library(UsingR)
library(reshape)
library(manipulate)
library(dplyr)

data(galton)

long <- melt(galton)

ggplot(long, aes(x = value, fill = variable)) +
  geom_histogram(color = "black", binwidth = 1) +
  facet_grid(. ~ variable)

my_hist <- function(mu) {
  mse <- mean((galton$child - mu)^2)
  ggplot(galton, aes (x = child)) + 
      geom_histogram(fill = 'green', colour = "black", binwidth = 1) +
      geom_vline(xintercept = mu, size = 3) + 
      ggtitle(paste("mu =", mu, " ", "MSE = ", round(mse,2), sep = ""))
}
manipulate(my_hist(mu), mu = slider(61, 73, step = 0.5)) # don't work


# Galton parent child scaterplot

freqData <- as.data.frame(table(galton$child, galton$parent))
names(freqData) <- c("child", "parent", "freq")
freqData$child <- as.numeric(as.character(freqData$child))
freqData$parent <- as.numeric(as.character(freqData$parent))

data <- filter(freqData, freq > 0)

ggplot(data, aes(x = parent, y = child)) +
   scale_size(range = c(2, 20), guide = "none" ) +
   geom_point(colour="grey50", aes(size = freq+20)) + 
   geom_point(aes(colour=freq, size = freq)) + 
   geom_smooth(method='lm') +
   scale_colour_gradient(low = "lightblue", high="white")
  
  


fit <- lm(child ~ parent, data=galton)

plot(predict(fit), resid(fit)) # residuals

fit_df <- data.frame(predict = predict(fit), resid = resid(fit))

ggplot(fit_df,aes(x = predict, y = resid )) +
  geom_point() +
  geom_smooth()