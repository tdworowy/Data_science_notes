library(lubridate)
data <- read.csv("Data/house_sales.csv", sep='\t')
data$Year = year(data$DocumentDate)
data$Weight = data$Year - 2005 # weight as number of years from 2005 (newest observation will have bigger impact)


house_weighted_regresion <- lm(AdjSalePrice ~ SqFtTotLiving + SqFtLot + Bathrooms + 
                   Bedrooms + BldgGrade,
                   data=data, na.action=na.omit, weight=Weight) # weighted

house_regresion <- lm(AdjSalePrice ~ SqFtTotLiving + SqFtLot + Bathrooms + 
                                 Bedrooms + BldgGrade,
                               data=data, na.action=na.omit) # not weighted

round(cbind(house_lm = house_regresion$coefficients,
            house_wt=house_weighted_regresion$coefficients)
      ,digits=3)