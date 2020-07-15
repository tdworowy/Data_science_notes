
check_id <- function(id){
  s_id <- if (nchar(toString(id)) ==2) {
    paste("0", toString(id), sep = "")
  
    }else if(nchar(toString(id)) == 1) {
      paste("00",toString(id), sep = "")
  } else {
    toString(id)
  }
  s_id
}
#calculates the mean of a pollutant 
pollutant_mean <- function(directory, pollutant, id =1:332) {
  data <- list()
  for (i in id) {
    s_id <- check_id(i)
    data_partial <-read.csv(paste(directory,s_id,".csv",sep = ""))
    data[[i]] <- data_partial
  }
  data <- do.call(rbind, data)
  mean(data[[pollutant]], na.rm = TRUE)
}

# reads a directory full of files and reports the number of completely observed cases in each data file
complete <- function(directory,id =1:332) {
  data <- list()
  for (i in id) {
      s_id <- check_id(i)
      data_partial <-read.csv(paste(directory,s_id,".csv",sep = ""))
      dat_frame_partial <- data.frame(id = i, nobs = sum(complete.cases(data_partial)))
      data[[i]] <- dat_frame_partial
  }
  do.call(rbind, data)
}

corr <- function(directory, thrashold=0){
  completed <- complete(directory)
  ids <- completed["id"][completed["nobs"] > thrashold]
  data <- vector()
  for (i in ids) {
    s_id <- check_id(i)
    data_partial <-read.csv(paste(directory,s_id,".csv",sep = ""))
    data[i] <- cor(data_partial[["nitrate"]],data_partial[["sulfate"]],use = "complete.obs")

  }
  data
}

polution_mean("Data/specdata/","sulfate") #3.189369
