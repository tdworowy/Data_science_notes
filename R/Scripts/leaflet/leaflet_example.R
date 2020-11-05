install.packages("leaflet")

library(leaflet)

# Single marker
map1 <- leaflet() %>%
  addTiles() %>%
  addMarkers(lat = 50.097030, lng = 18.496200,
             popup = "My house")

map1


# many markers
df1 <- data.frame(lat = runif(30, min = 49.9, max = 50.6),
                 lng = runif(30, min = 17.9, max = 18.6)) # 30 random coordinates


map2 <- df1 %>%
        leaflet() %>%
        addTiles() %>%
        addMarkers()

map2


# many markers clustering
df2 <- data.frame(lat = runif(500, min = 49.5, max = 50.6),
                 lng = runif(500, min = 17.5, max = 18.6)) # 30 random coordinates


map3 <- df2 %>%
  leaflet() %>%
  addTiles() %>%
  addMarkers(clusterOptions = markerClusterOptions()) # cool

map3



# circle markers
df3 <- data.frame(lat = runif(30, min = 49.9, max = 50.6),
                  lng = runif(30, min = 17.9, max = 18.6)) # 30 random coordinates


map4 <- df3 %>%
  leaflet() %>%
  addTiles() %>%
  addCircleMarkers()

map4

# draw rectangle

map5 <- leaflet() %>%
  addTiles() %>%
  addRectangles(lat1 = 50.0, lng1 = 18.4,
                lat2 = 50.2, lng2 = 18.7)

map5
