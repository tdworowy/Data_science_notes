# data from https://github.com/DataScienceSpecialization/courses/blob/master/04_ExploratoryAnalysis/CaseStudy/pm25_data.zip

pm_0 <- read.table("Data/pm25_data/RD_501_88101_1999-0.txt", comment.char = "#",header=FALSE, sep="|",na.strings="")
pm_1 <- read.table("Data/pm25_data/RD_501_88101_2012-0.txt", comment.char = "#",header=FALSE, sep="|",na.strings="")

dim(pm_0)
head(pm_0)

dim(pm_1)
head(pm_1)

columns_names <- readLines("Data/pm25_data/RD_501_88101_1999-0.txt",1)
columns_names <- strsplit(columns_names, "|", fixed=TRUE)

names(pm_0) <- make.names(columns_names[[1]])
names(pm_1) <- make.names(columns_names[[1]])

x_0 <- pm_0$Sample.Value
x_1 <- pm_1$Sample.Value

str(x_0)
summary(x_0)

mean(is.na(x_0)) # check how many % of data is NA
mean(is.na(x_1)) # check how many % of data is NA

boxplot(x_0, x_1) # outliers in x_1 make it hard to read
boxplot(log10(x_0), log10(x_1))

negative <-x_1 < 0 # there shouldn't by any negative numbers (but there are)
sum(negative, na.rm = TRUE) # count negative numbers in x_1
mean(negative, na.rm = TRUE) # check how many % of data is negative

dates <- pm_1$Date
dates <- as.Date(as.character(dates),"%Y%m%d")

hist(dates, "month")
hist(dates[negative], "month") # negative values by month

site_0 <- unique(subset(pm_0, State.Code==36, c(County.Code, Site.ID))) # 36 - New York
site_1 <- unique(subset(pm_1, State.Code==36, c(County.Code, Site.ID)))

site_0 <- paste(site_0[,1],site_0[,2], sep = ".")
site_1 <- paste(site_1[,1],site_1[,2], sep = ".")

both <- intersect(site_0, site_1) # intersection between site_0, and site_1

pm_0$County.Site <- with(pm_0, paste(County.Code, Site.ID, sep=".")) # add County.Site column to original data frame
pm_1$County.Site <- with(pm_1, paste(County.Code, Site.ID, sep="."))

cnt_0 <- subset(pm_0, State.Code==36 & County.Site %in% both)
cnt_1 <- subset(pm_1, State.Code==36 & County.Site %in% both)

# split by monitor(County.Site) and count observations
sapply(split(cnt_0, cnt_0$County.Site),nrow)
sapply(split(cnt_1, cnt_1$County.Site),nrow)

pm_0_sub <- subset(pm_0, State.Code==36 & County.Site == 63.2008)
pm_1_sub <- subset(pm_1, State.Code==36 & County.Site == 63.2008)

dim(pm_0_sub)
dim(pm_1_sub)

dates_0 <- pm_0_sub$Date
dates_0 <- as.Date(as.character(dates_0),"%Y%m%d")
x1_sub_0 <- pm_0_sub$Sample.Value

dates_1 <- pm_1_sub$Date
dates_1 <- as.Date(as.character(dates_1),"%Y%m%d")
x1_sub_1 <- pm_1_sub$Sample.Value

# plot 1 
par(mfrow = c (1,2))
plot(dates_0, x1_sub_0, pch=19)
abline(h = median(x1_sub_0, na.rm = TRUE))

plot(dates_1, x1_sub_1, pch=19)
abline(h = median(x1_sub_1, na.rm = TRUE))


# plot 2 (witch common range) 
rng <- range(x1_sub_0, x1_sub_1, na.rm = TRUE) # range of data sets together 

par(mfrow = c (1,2))
plot(dates_0, x1_sub_0, pch=19, ylim=rng)
abline(h = median(x1_sub_0, na.rm = TRUE))

plot(dates_1, x1_sub_1, pch=19, ylim=rng)
abline(h = median(x1_sub_1, na.rm = TRUE))


#plot state means
# plot by state
mean_0 <- with(pm_0, tapply(Sample.Value, State.Code, mean, na.rm=TRUE))
mean_1 <- with(pm_1, tapply(Sample.Value, State.Code, mean, na.rm=TRUE))

d_0 <- data.frame(state = names(mean_0), mean = mean_0)
d_1 <- data.frame(state = names(mean_1), mean = mean_1)

mrg <- merge(d_0,d_1, by = "state")
par(mfrow = c (1,1))
with(mrg, plot(rep(1999, 52), mrg[,2], xlim = c(1998,2013),pch=19))
with(mrg, points(rep(2012, 52), mrg[,3],pch=19))
with(mrg, segments(rep(1999,52),mrg[,2], rep(2012,52), mrg[,3]))

#plot state max
max_0 <- with(pm_0, tapply(Sample.Value, State.Code, max, na.rm=TRUE))
max_1 <- with(pm_1, tapply(Sample.Value, State.Code, max, na.rm=TRUE))

d_0 <- data.frame(state = names(mean_0), max = max_0)
d_1 <- data.frame(state = names(mean_1), max = max_1)

mrg <- merge(d_0,d_1, by = "state")
rng <- range(max_0, max_1, na.rm = TRUE)

par(mfrow = c (1,1))
with(mrg, plot(rep(1999, 52), mrg[,2], xlim = c(1998,2013), ylim=rng,pch=19))
with(mrg, points(rep(2012, 52), mrg[,3],pch=19))
with(mrg, segments(rep(1999,52),mrg[,2], rep(2012,52), mrg[,3]))