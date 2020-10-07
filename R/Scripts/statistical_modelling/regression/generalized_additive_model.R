# another way to handle non linear regression - automaticaly fir a spline regression
library(mgcv)
library(ggplot2)

data <- read.csv("Data/house_sales.csv", sep='\t')

house_gam <- gam(AdjSalePrice ~ s(SqFtTotLiving) + #s finds best knots
                 SqFtLot + 
                 Bathrooms +
                 Bedrooms + 
                 BldgGrade, 
               data = data, na.action = na.omit)


plot(house_gam)
plot(predict(house_gam), resid(house_gam))

fit_df <- data.frame(predict = predict(house_gam), resid = resid(house_gam))

ggplot(fit_df,aes(x = predict, y = resid )) +
  geom_point() +
  geom_smooth()