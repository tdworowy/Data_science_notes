data <- read.csv("Data/house_sales.csv", sep='\t')

house_lm_poly <- lm(AdjSalePrice ~ poly(SqFtTotLiving,2) + 
                   SqFtLot + 
                   Bathrooms +
                   Bedrooms + 
                   BldgGrade, 
                   data = data, na.action = na.omit)


house_lm <- lm(AdjSalePrice ~ SqFtTotLiving + 
                 SqFtLot + 
                 Bathrooms +
                 Bedrooms + 
                 BldgGrade, 
               data = data, na.action = na.omit)


#non linear
terms_non_linear <- predict(house_lm_poly, type='terms')
partial_residn_non_linear <- resid(house_lm_poly) + terms

df_non_linear <- data.frame(SqFtTotLiving = data[,'SqFtTotLiving'],
                 Terms = terms_non_linear[,'poly(SqFtTotLiving, 2)'],
                 PartialResid = partial_residn_non_linear[,'poly(SqFtTotLiving, 2)'])
# linear 
terms_linear <- predict(house_lm, type='terms')
partial_residn_linear <- resid(house_lm) + terms_linear

df_linear <- data.frame(SqFtTotLiving = data[,'SqFtTotLiving'],
                            Terms = terms_linear[,'SqFtTotLiving'],
                            PartialResid = partial_residn_linear[,'SqFtTotLiving'])
#partial residual plot
ggplot(df_non_linear,aes(SqFtTotLiving, PartialResid)) +
  geom_point() +
  scale_shape(solid = FALSE) + 
  geom_smooth(linetype = 2) +  # relation between SqFtTotLiving and price
  geom_line(aes(SqFtTotLiving, Terms), col="red")+ # regression line (non linear)
  geom_line(data=df_linear,aes(SqFtTotLiving, Terms), col="green")# regression line (non linear)