setwd("Scripts/leaflet")
data <- read.csv("nuforc_reports.csv")

data_subset <- data %>% select (city_latitude ,city_longitude,posted,summary)

names(data_subset)[names(data_subset) == 'city_latitude'] <- 'lat'
names(data_subset)[names(data_subset) == 'city_longitude'] <- 'long'
data_subset$popup <- paste(data_subset$posted,data_subset$summary)

data_subset <- data_subset %>% select (lat,long,popup)
data_subset <- data_subset[complete.cases(data_subset),]



map1 <-data_subset %>%
  leaflet() %>%
  addTiles() %>%
  addCircleMarkers(lat = ~lat, lng = ~long, popup = ~popup, clusterOptions = markerClusterOptions())

map1