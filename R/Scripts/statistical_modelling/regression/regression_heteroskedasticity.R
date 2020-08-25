#Heteroskedasticity - is the lack of constant residual variance across the range of predicted values.
# errors ar greater for some portions of the range.

data <- read.csv("Data/house_sales.csv", sep='\t')

house_98105 <- data[data$ZipCode == 98105,]
lm_98105 <- lm(AdjSalePrice ~ SqFtTotLiving + SqFtLot + Bathrooms + 
                 Bedrooms + BldgGrade, data=house_98105)


# plot absolute residuals versus the predicted values
library(ggplot2)

df <- data.frame(resid = residuals(lm_98105),pred = predict(lm_98105))

ggplot(df, aes(pred, abs(resid))) + 
  geom_point() + 
  geom_smooth() # data has heteroskedastic errors

