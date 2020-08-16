data <- read.csv("Data/click_rates.csv")

clicks <- matrix(data$Rate, nrow=3, ncol=2, byrow=TRUE)
dimnames(clicks) <- list(unique(data$Headline), unique(data$Click))

chisq.test(clicks, simulate.p.value=TRUE)

chisq.test(clicks, simulate.p.value=FALSE)

fisher.test(clicks) # check all possible permutations that can occur