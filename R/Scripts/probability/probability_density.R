x <- c(-0.5, 0 , 1, 1, 1.5)
y <- c(0, 0, 2, 0, 0) # example probability density

plot(x ,y, lwd = 3, frame = FALSE, type="l")
polygon(c(0, .75, .75, 0), c(0, 0, 1.5, 0), lwd = 3, col = "lightblue") # smaller tringle (75%)

# probability of 75%  (subset of data that contains 75% of tingle)
(1 * 2)/2 # area of the tingle

1.5 * 0.75/2 # area of the smaller tingle (75%)
pbeta(0.75,2,1) # same as above from beta distribution 