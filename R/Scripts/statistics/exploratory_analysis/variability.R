data <- read.csv(file.path("Data","hw1_data.csv"))

standard_deviation <- sd(data[["Wind"]])
interquartile_range <- IQR(data[["Wind"]]) # difference between 75th and 25th percentiles
median_absolute_deviation <- mad(data[["Wind"]])
                 