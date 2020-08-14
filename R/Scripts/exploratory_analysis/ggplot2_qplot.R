install.packages("ggplot2")
library(ggplot2)

#plot 1
qplot(displ, hwy, data = mpg)

#plot 2
qplot(displ, hwy, data = mpg, 
                  color = drv,
                  geom = c("point","smooth"))

#plot 3
qplot(hwy, data = mpg, fill = drv)

#plot 4
#facets = panels 
qplot(displ, hwy, data = mpg, 
                  facets = . ~ drv, 
                  color = drv)

#plot 5
qplot(displ, hwy, data = mpg, 
                  facets = . ~ drv, 
                  color = drv,
                  geom = c("point","smooth"))

#plot 6
qplot(hwy, data = mpg, 
            facets = drv ~ .,
            fill = drv)

#plot 7
qplot(hwy, data = mpg, 
      facets = drv ~ .,
      fill = drv,
      geom = "density")

#plot 8
qplot(hwy, data = mpg, 
      fill = drv,
      geom = "density")

#plot 9
qplot(displ, hwy, data = mpg, 
      facets = . ~ drv, 
      color = drv) +
  geom_smooth(method = "lm")


#plot 10
library(datasets)
data(airquality)

qplot(Wind, Ozone, data = airquality, facets = . ~ factor(Month))


airquality = transform(airquality, Month = factor(Month))
qplot(Wind, Ozone, data = airquality, facets = . ~ Month)