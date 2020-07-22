date1 <- Sys.Date()

format(date1,"%a %b %d")

str_date <- c("1jan1960","28feb2234")
date2 <- as.Date(str_date,"%d%b%Y")

date2[2] - date2[1]

weekdays(date2)
months(date2)

julian(date2)