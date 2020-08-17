data <- read.csv("Data/house_sales.csv", sep='\t')

house_lm <- lm(AdjSalePrice ~ SqFtTotLiving + 
                              SqFtLot + 
                              Bathrooms +
                              Bedrooms + 
                              BldgGrade, 
                              data = data, na.action = na.omit)

house_lm
summary(house_lm)

str(house_lm)

install.packages("ggiraphExtra")
library(ggiraphExtra)

house_lm_simple <- lm(AdjSalePrice ~ SqFtTotLiving + 
                 SqFtLot + 
                 Bedrooms, 
               data = data, na.action = na.omit)

ggPredict(house_lm_simple, colorAsFactor = TRUE, interactive=FALSE) # can plot to max 3 variables 
ggPredict(house_lm_simple)