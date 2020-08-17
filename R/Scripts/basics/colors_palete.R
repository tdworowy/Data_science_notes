pal1 <- colorRamp(c("red","blue"))
pal1(0)
pal1(1)
pal1(.5)

pal2 <- colorRamp(c("red","green","blue"))
pal2(0)
pal2(1)
pal2(.5)

pal1(seq(0,1, len=10))# sequence of colors 
pal2(seq(0,1, len=10)) 

pal3 <- colorRampPalette(c("red","yellow"))
pal3(2)
pal3(13)


install.packages("RColorBrewer")
library(RColorBrewer)

cols <- brewer.pal(5, "BuGn")
pal4 <- colorRampPalette(cols)

image(volcano, col = pal4(20))

x <- rnorm(10000)
y <- rnorm(10000)
smoothScatter(x,y, colramp = pal4)