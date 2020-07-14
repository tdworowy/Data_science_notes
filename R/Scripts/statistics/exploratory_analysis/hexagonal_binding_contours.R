data <- read.csv(file.path("Data","kc_tax.csv"))
kc_tax <- subset(data, data$TaxAssessedValue < 750000 & data$SqFtTotLiving  > 100 & data$SqFtTotLiving  < 3500)

library("ggplot2")

#hexagonal binding plot
ggplot(kc_tax, (aes(x=SqFtTotLiving,y=TaxAssessedValue)))+
  stat_binhex(color="Blue")+
  theme_bw()+
  scale_fill_gradient(low="Blue",high="Red")

#contour plot
ggplot(kc_tax, aes(SqFtTotLiving,TaxAssessedValue))+
  theme_bw()+
  geom_point(alpha=0.5)+
  geom_density2d(color="blue")
