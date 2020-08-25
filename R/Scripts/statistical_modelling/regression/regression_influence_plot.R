data <- read.csv("Data/house_sales.csv", sep='\t')

house_98105 <- data[data$ZipCode == 98105,]
lm_98105 <- lm(AdjSalePrice ~ SqFtTotLiving + SqFtLot + Bathrooms + 
                 Bedrooms + BldgGrade, data=house_98105)

#influence plot
# bigger cooks distance means that observation is more influential 
std_resid <- rstandard(lm_98105)
cooks_D <- cooks.distance(lm_98105)
hat_values <- hatvalues(lm_98105)

plot(subset(hat_values, cooks_D > 0.08),
     subset(std_resid, cooks_D > 0.08),
     cex = 10 * sqrt(subset(cooks_D, cooks_D >0.08)),
     pch=16, col = "lightblue")
points(hat_values, std_resid, cex = 10 * sqrt(cooks_D),col = "red")
abline(h = c(-2.5,2.5), lty=2)