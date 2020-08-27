library(ggplot2)

data <- read.csv("Data/house_sales.csv", sep='\t')

house_98105 <- data[data$ZipCode == 98105,]
lm_98105 <- lm(AdjSalePrice ~ SqFtTotLiving + SqFtLot + Bathrooms + 
                 Bedrooms + BldgGrade, data=house_98105)

terms <- predict(lm_98105, type='terms')
partial_resid <- resid(lm_98105) + terms

df <- data.frame(SqFtTotLiving = house_98105[,'SqFtTotLiving'],
                 Terms = terms[,'SqFtTotLiving'],
                 PartialResid = partial_resid[,'SqFtTotLiving'])

ggplot(df,aes(SqFtTotLiving, PartialResid)) +
  geom_point() +
  scale_shape(solid = FALSE) + 
  geom_smooth(linetype = 2) +  # relation between SqFtTotLiving and price
  geom_line(aes(SqFtTotLiving, Terms), col="red") # regression line