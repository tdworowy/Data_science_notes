library(ggplot2)
data <- read.csv("Data/web_page_data.csv")

ggplot(data, aes(x=Page, Y=Time)) +
  geom_boxplot()

# compare means
mean_a <- mean(data[data["Page"] == "Page A", "Time"])
mean_b <- mean(data[data["Page"] == "Page B", "Time"])

mean_b - mean_a

permutation_func <- function(x, nA, nB) {
  n <-nA + nB
  idx_b <- sample(1:n, nB)
  idx_a <- setdiff(1:n, idx_b)
  mean_diff <- mean(x[idx_b]) - mean(x[idx_a])
  return(mean_diff)
}

perm_diffs <- rep(0,1000)
for (i in 1:1000) {
  perm_diffs[i] = permutation_func(data[, "Time"],21,15)
}
hist(perm_diffs, xlab =  "Session time differences")
abline(v=mean_b - mean_a, col="red", lwd = 3)

# how often mean difference of random permutation exceeds observed difference
mean(perm_diffs > (mean_b - mean_a))

#observed differences in session time between page A and B is well within the range of chance variation
#thus in not statistically significant 

#histogram of random;y permuted differences in conversion

obs_pct_diff <- 100 * (200 / 23739 - 182 / 22588)
conversion <- c(rep(0, 45945), rep(1, 382))
perm_diffs <- rep(0, 1000)
for (i in 1:1000) {
  perm_diffs[i] = 100 * permutation_func(conversion, 23739, 22588)
}
hist(perm_diffs)
abline(v=obs_pct_diff,lty=2, lwd=3,col="red")

#p-value
mean(perm_diffs > obs_pct_diff) # from permutation test
prop.test(x=c(200,182), n=c(23739,22588), alternative='greater') #p-value approximation (can use for binomial distribution)

#t-Test
t.test(Time ~ Page, data = data)
t.test(Time ~ Page, data = data, alternative ='less')