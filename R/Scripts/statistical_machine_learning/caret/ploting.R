install.packages("gower")
install.packages("lava")
require('caret')
require('Hmisc')
require('gridExtra')

#ploting

data(Wage)
summary(Wage)

in_train <- createDataPartition( y = Wage$wage, p = 0.75, list = FALSE)

traning <- Wage[in_train,]
test <- Wage[-in_train,]

featurePlot(x = traning[,c("age","education","jobclass")], y = traning$wage, plot = "pairs")
qplot(age, wage, data = traning)
qplot(education, wage, data = traning)
qplot(jobclass, wage, data = traning)

qplot(age, wage, color = jobclass, data = traning)


qplot(age, wage, color = education, data = traning) +
  geom_smooth()


cut_wage <- cut(traning$wage, breaks = 3)
plt1 <- qplot(cut_wage,age, data = traning, fill=cut_wage, geom = c('boxplot'))
plt2 <- qplot(cut_wage,age, data = traning, fill=cut_wage, geom = c('boxplot','jitter'))
grid.arrange(plt1,plt2,ncol=2)

qplot(wage, color = education, data = traning, geom = 'density')