install.packages("MASS")
library(MASS)

data <- read.csv("Data/house_sales.csv", sep='\t')


house_full <- lm(AdjSalePrice ~ SqFtTotLiving + SqFtLot + Bathrooms + 
                   Bedrooms + BldgGrade + PropertyType + NbrLivingUnits + 
                   SqFtFinBasement + YrBuilt + YrRenovated + NewConstruction,
                 data=data, na.action=na.omit)

step <- stepAIC(house_full, direction = "both")