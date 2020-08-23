library(dplyr)
data <- read.csv("Data/house_sales.csv", sep='\t')


house_regresion <- lm(AdjSalePrice ~ SqFtTotLiving + SqFtLot + Bathrooms + 
                       Bedrooms + BldgGrade,
                     data=data, na.action=na.omit)

zip_groups <- data %>%
  mutate(resid=residuals(house_regresion)) %>%
  group_by(ZipCode) %>%
  summarise(med_resid = median (resid),
            cnt = n()) %>%
  arrange(med_resid) %>%
  mutate(cum_cnt = cumsum(cnt),
         ZipGroup = ntile(cum_cnt,5))

house <- data %>% left_join(select(zip_groups, ZipCode, ZipGroup), by = "ZipCode")

house_regresion

house_regresion2 <- lm(AdjSalePrice ~ SqFtTotLiving + SqFtLot + Bathrooms + 
                        Bedrooms + BldgGrade + ZipGroup,
                      data=house, na.action=na.omit)

house_regresion2

house_regresion3 <- lm(AdjSalePrice ~ SqFtTotLiving * ZipGroup + SqFtLot + Bathrooms + 
                         Bedrooms + BldgGrade + PropertyType,
                       data=house, na.action=na.omit) # * include interaction between variables SqFtTotLiving and ZipGroup
house_regresion3