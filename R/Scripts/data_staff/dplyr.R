install.packages("dplyr")
library(dplyr)

data <- readRDS("Data/Chicago.rds")

head(select(data, city:dptp)) #select columns from city to dptp
head(select(data, -(city:dptp))) #select all columns except columns from city to dptp

filter(data, pm25tmean2 > 50) # filter data
filter(data, pm25tmean2 > 50 & tmpd > 70)# filter data multiple columns
filter(data, pm25tmean2 > 50, tmpd > 70)# filter data multiple columns 

head(arrange(data, date)) # sort by date (ascending)
head(arrange(data, desc(date))) # sort by date (descending)

data <- rename(data, pm25 = pm25tmean2, dewpoint = dptp) # rename column

data <- mutate(data, pm25detrend = pm25 - mean(pm25, na.rm = TRUE)) # add new columns

data <- mutate(data, tempcat = factor(1 *(tmpd > 80), labels = c("cold","hot"))) # add categorical variable (column)
hotcold <- group_by(data, tempcat) # create grouped table
summarize(hotcold, pm25=mean(pm25, na.rm = TRUE), o3 = max(o3tmean2), no2 = median(no2tmean2))
               

#same as above but use pipeline operator
data %>% mutate(tempcat = factor(1 *(tmpd > 80), labels = c("cold","hot"))) %>% 
  group_by(tempcat) %>% 
  summarize(pm25=mean(pm25, na.rm = TRUE), o3 = max(o3tmean2), no2 = median(no2tmean2))

data_tbl_df <- tbl_df(data) # create dplyr specific data type