install.packages("dplyr")
library(dplyr)

setwd("Scripts/getting_and_cleaning_data_course_project")

clear_data <- function(main_dir,directory,subject_file,activity_file,data_file){
  subject <- read.table(paste(main_dir,directory,subject_file,sep = "/"), header = FALSE, sep = "")
  data_set <- data.frame(subject)
  names(data_set) <- c("Subject")
  
  activities <- read.table(paste(main_dir,directory,activity_file,sep = "/"), header = FALSE, sep = "")
  data_set <- mutate(data_set,activities)
  names(data_set) <- c("Subject","Activity")
  
  data <- read.table(paste(main_dir,directory,data_file,sep = "/"), header = FALSE, sep = "")
  data_set <- mutate(data_set,data)
  
  data_set
}

data_set <- clear_data("UCI HAR Dataset","test","subject_test.txt","y_test.txt","X_test.txt")
data_set <- data_set %>% rbind(clear_data("UCI HAR Dataset","train","subject_train.txt","y_train.txt","X_train.txt"))


activity_labels <-  read.table(paste("UCI HAR Dataset","activity_labels.txt",sep = "/"))

data_set[[2]] <- factor(data_set[[2]],
                           levels = activity_labels[[1]],
                           labels = activity_labels[[2]])


features <- read.table(paste("UCI HAR Dataset","features.txt",sep = "/"))
features <- gsub(pattern = "BodyBody", replacement = "Body",features[[2]])

names(data_set) <- c("Subject","Activity",features)

filtered_data_set <- data_set %>% select(contains("Subject")|contains("Activity")|contains("Mean")|contains("std"))

# TODO 
# creates a second, independent tidy data set with the average of each variable for each activity and each subject
# add comments (describe process)
# add readme
# add CodeBook.md with variable description
