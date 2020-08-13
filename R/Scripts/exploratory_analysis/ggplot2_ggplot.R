library(ggplot2)

#https://github.com/lupok2001/datasciencecoursera/blob/master/maacs.Rda <- correct data
load("Data/maacs.rda")

#plot 1
g <- ggplot(maacs, aes(logpm25, NocturnalSympt))
g + geom_point() + geom_smooth()

#plot 2
ggplot(maacs, aes(logpm25, NocturnalSympt)) + 
  geom_point() + 
  geom_smooth(method = "lm")

#plot 3
ggplot(maacs, aes(logpm25, NocturnalSympt)) + 
  geom_point() + 
  facet_grid(. ~ bmicat) +
  geom_smooth(method = "lm") +
  theme_dark()

#plot 4
ggplot(maacs, aes(logpm25, NocturnalSympt)) + 
  geom_point(aes(color = bmicat)) + 
  geom_smooth(method = "lm") + 
  labs(title = "MAACS") +
  labs(x = expression("log " * PM[2.5]), y = "Nocturnal Symptoms") +
  theme_light()

#plot 5
data1 <- data.frame(x=1:300, y=rnorm(100)) 
data1[150,2] <- 100 # add outlier

ggplot(data1, aes(x = x, y = y)) +
  geom_line() # with outlier

ggplot(data1, aes(x = x, y = y)) +
  geom_line() + 
  coord_cartesian(ylim = c (-4,4)) # y axis is limited by outlier is still included


#plot 6
# create new factor variable from continues one
cut_points <- quantile(maacs$logno2_new, seq(0, 1, length = 4), na.rm = TRUE)
maacs$no2dec <- cut(maacs$logno2_new, cut_points)
levels(maacs$no2dec)

ggplot(maacs, aes(logpm25, NocturnalSympt)) + 
  geom_point(alpha = 1/4) + 
  facet_wrap(bmicat ~ no2dec, nrow = 2, ncol = 4) +
  geom_smooth(method = "lm", col = "red", se=FALSE) + 
  theme_dark(base_family =  "Avenir", base_size = 8) + 
  labs(x = expression("log " * PM[2.5])) + 
  labs(y = "Nocturnal Symptoms")
 

#plot 7
ggplot(mpg, aes(x=displ, y=hwy, color=factor(year))) + 
  geom_point() + 
  facet_grid(drv~cyl, margins=TRUE) + 
  geom_smooth(method ="lm", se=FALSE, size=1, color="black") + 
  labs(x="Displacement",y="Highway Mileage")

