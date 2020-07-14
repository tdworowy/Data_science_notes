data <- read.csv(file.path("Data","hw1_data.csv"))

percentiles <- quantile(data[["Temp"]], p= c(.05,.25,.5,.75,.95))

boxplot(data[["Temp"]])

breaks <- seq(from=min(data[["Temp"]]), to=max(data[["Temp"]]), length =5)
temp_freq <- cut(data[["Temp"]], breaks = breaks, right = TRUE, include.lowest = TRUE)
table(temp_freq) # frequency table

hist(data[["Temp"]], breaks = breaks)
         
hist(data[["Temp"]], freq = FALSE)
lines(density(data[["Temp"]]), lwd=3, col="green") # density plot