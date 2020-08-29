#regression with splines (non linear)

library(splines)
library(ggplot2)
data <- read.csv("Data/house_sales.csv", sep='\t')

knots <- quantile(data$SqFtTotLiving, p=c(.25,.5,.75))

house_splines <- lm(AdjSalePrice ~ bs(SqFtTotLiving, knots=knots, degree=3) + 
                   SqFtLot + 
                   Bathrooms +
                   Bedrooms + 
                   BldgGrade, 
                 data = data, na.action = na.omit)

plot(house_splines)

#partial residual plot
terms <- predict(house_splines, type='terms')
partial_resid <- resid(house_splines) + terms

df <- data.frame(SqFtTotLiving = data[,'SqFtTotLiving'],
                 Terms = terms[,'bs(SqFtTotLiving, knots = knots, degree = 3)'],
                 PartialResid = partial_resid[,'bs(SqFtTotLiving, knots = knots, degree = 3)'])

ggplot(df,aes(SqFtTotLiving, PartialResid)) +
  geom_point() +
  scale_shape(solid = FALSE) + 
  geom_smooth(linetype = 2) +  # relation between SqFtTotLiving and price (with consideration of other variables) - partial residual
  geom_line(aes(SqFtTotLiving, Terms), col="red") # regression line (witch splines)