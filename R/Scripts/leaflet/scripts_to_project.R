setwd("Scripts/leaflet")
data <- read.csv("nuforc_reports.csv")

data_subset <- data %>% select (city_latitude ,city_longitude,stats,summary,shape)
data_subset$popup <- paste(data_subset$stats,"Summary:",data_subset$summary,"Shape:",data_subset$shape)
data_subset <- data_subset %>% select (city_latitude,city_longitude,popup)
data_subset <- data_subset[complete.cases(data_subset),]


map1 <-data_subset %>%
  leaflet() %>%
  addTiles() %>%
  addCircleMarkers(lat = ~city_latitude, lng = ~city_longitude, popup = ~popup, clusterOptions = markerClusterOptions())

map1