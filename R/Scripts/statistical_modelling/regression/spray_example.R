require(datasets)

summary(lm(count ~ spray, data = InsectSprays))$coef # sprayA is reference (Intercept), other sprays are relative to sprayA,
# Intercept Estimate is counts mean fro sprayA, and SprayB Estimate is SprayB counts mean minus SprayA counts mean. 
summary(lm(count ~ spray - 1, data = InsectSprays))$coef # Estimate are now equal to spray counts means.