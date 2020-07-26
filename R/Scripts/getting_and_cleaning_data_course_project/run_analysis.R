
setwd("Scripts/getting_and_cleaning_data_course_project")

################################################################################
# Loads required libraries
################################################################################
install.packages("dplyr")
library(dplyr)

################################################################################
#Function that load txt files as data frames
################################################################################
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
################################################################################
#Merges the training and the test sets to create one data set.
################################################################################
data_set <- clear_data("UCI HAR Dataset","test","subject_test.txt","y_test.txt","X_test.txt")
data_set <- data_set %>% rbind(clear_data("UCI HAR Dataset","train","subject_train.txt","y_train.txt","X_train.txt"))


################################################################################
#Uses descriptive activity names to name the activities in the data set.
################################################################################
activity_labels <-  read.table(paste("UCI HAR Dataset","activity_labels.txt",sep = "/"))
data_set[[2]] <- factor(data_set[[2]],
                           levels = activity_labels[[1]],
                           labels = activity_labels[[2]])


################################################################################
#Appropriately labels the data set with descriptive variable names. 
################################################################################
features <- read.table(paste("UCI HAR Dataset","features.txt",sep = "/"))
features <- gsub(pattern = "BodyBody", replacement = "Body",features[[2]])

names(data_set) <- c("Subject","Activity",features)

################################################################################
#Extracts only the measurements on the mean and standard deviation for each measurement.
################################################################################
filtered_data_set <- data_set %>% select(contains("Subject")|contains("Activity")|contains("Mean")|contains("std"))
filtered_data_set <- filtered_data_set %>% select(!contains("angle"))
################################################################################
#creates a second, independent tidy data set with the average of each variable for each activity and each subject.
################################################################################
new_data_set <- filtered_data_set %>% group_by(Subject,Activity) %>% summarise_all(list(mean))
new_features <- names(new_data_set)[3:length(names(new_data_set))]
new_features <- paste("Mean_Of", new_features, sep="_")
names(new_data_set) <- c("Subject","Activity", new_features)
write.csv(new_data_set,"tidy.csv")