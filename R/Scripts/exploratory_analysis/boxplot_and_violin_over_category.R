airline_data <-  read.csv(file.path("Data","airline_stats.csv"))

#boxplot
boxplot(pct_carrier_delay ~ airline, data = airline_data, ylim=c(0,100),las = 2)

#violin
library("ggplot2")
ggplot(data = airline_data, aes(airline, pct_carrier_delay))+
  ylim(0,100)+
  geom_violin()