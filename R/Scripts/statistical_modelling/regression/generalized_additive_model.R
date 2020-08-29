# another way to handle non linear regression - automaticaly fir a spline regression
library(mgcv)

data <- read.csv("Data/house_sales.csv", sep='\t')

house_gam <- gam(AdjSalePrice ~ s(SqFtTotLiving) + #s finds best knots
                 SqFtLot + 
                 Bathrooms +
                 Bedrooms + 
                 BldgGrade, 
               data = data, na.action = na.omit)


plot(house_gam)