install.packages("plotly")

library(plotly)
library(tidyr)
library(dplyr)

#scatter plot
plot_ly(data = mtcars, x = mtcars$wt, y = mtcars$mpg, color = as.factor(mtcars$cyl), 
        mode = "markers", type = 'scatter', size = mtcars$hp)

#3D scatter plot
temp <- rnorm(100, mean = 30, sd = 5)
pressue <- rnorm(100)
dtime <- 1:100

plot_ly(x = temp, y = pressue, z = dtime, 
        mode = "markers", type = 'scatter3d', color =  temp)


#line graph
data("airmiles")
plot_ly(x = time(airmiles), y = airmiles, type = 'scatter', mode = 'lines')

#multi line graph

data("EuStockMarkets")

stocks <- as.data.frame(EuStockMarkets) %>%
  gather(index, price) %>%
  mutate(time = rep(time(EuStockMarkets), 4))

plot_ly(x = stocks$time, y = stocks$price, color = stocks$index,
        type = 'scatter', mode = 'lines')

#box plot
plot_ly(x = iris$Petal.Length, color = iris$Species, type = "box")

#heatmap
terrain1 <- matrix(rnorm(100*100), nrow = 100, ncol = 100)
plot_ly(z = terrain1, type = "heatmap")

#3D surface
terrain2 <- matrix(sort(rnorm(100*100)), nrow = 100, ncol = 100)
plot_ly(z = terrain2, type = "surface")

plot_ly(z = terrain1, type = "surface")


#choropleth map

state_pop <- data.frame(State = state.abb, Pop = as.vector(state.x77[,1]))
state_pop$hover <- with(state_pop, paste(State, '<br>', "Population:", Pop))
borders <- list(color = toRGB("red"))

map_options <- list(
  scope = "usa",
  projection = list(type = "albers usa"),
  showlakes = TRUE,
  lakecolor = toRGB("white")
)

plot_ly(z = state_pop$Pop, text = state_pop$hover, locations = state_pop$State,
        type = "choropleth", locationmode = "USA-states",
        color = state_pop$Pop, colors = "Blues", marker = list(line = borders)) %>%
  layout(title = "US population in 1975", geo = map_options)
