data <- read.csv(file.path("Data","kc_tax.csv"))
kc_tax <- subset(data, data$TaxAssessedValue < 750000 & data$SqFtTotLiving  > 100 & data$SqFtTotLiving  < 3500)

library("ggplot2")

plot_conditional_zip_code <- function(data,zpi_codes= c(98188,98105,98108,98126)){
    ggplot(subset(data, ZipCode %in% zpi_codes),
           aes(x=SqFtTotLiving,y=TaxAssessedValue))+
      stat_bin_hex(color='blue')+
      theme_bw() +
      scale_fill_gradient(low="blue", high="red")+
      facet_wrap("ZipCode") # set conditioning variable
    }


plot_conditional_zip_code(kc_tax)
plot_conditional_zip_code(data) # with outliers