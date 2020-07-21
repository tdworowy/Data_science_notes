library(ggplot2)
data <- read.csv("Data/loans_income.csv")
data <- data[["x"]]

sample_data <- data.frame(income=sample(data,1000),type='data_dist')

#sample of means 5 values
sample_mean_05 <- data.frame(
  income = tapply(
    sample(data,1000*5),
    rep(1:1000, rep(5,1000)),
    FUN=mean),
  type="mean_of_5"
  )
#sample of means 20 values
sample_mean_20 <- data.frame(
  income = tapply(
    sample(data,1000*20),
    rep(1:1000, rep(20,1000)),
    FUN=mean),
  type="mean_of_20"
)

income <- rbind(sample_data,sample_mean_05,sample_mean_20)
income$type = factor(
  income$type,
  levels = c("data_dist","mean_of_5","mean_of_20"),
  labels = c("Data", "Mean of 5", "Mean of 20")
)
#histogram
ggplot(income, aes(x=income))+
  geom_histogram(bins=40)+
  facet_grid(type ~ .)


#qq-plot -how close sample is to a specific distribution

norm_sample <- rnorm(200)
qqnorm(norm_sample)
abline(a=0,b=1, col='blue')
 
pois_sample <- rpois(1:100, lambda = 1)#?
qqnorm(pois_sample)
abline(a=0,b=1, col='blue')
