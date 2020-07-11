outcome <- read.csv("data/outcome-of-care-measures.csv", colClasses = "character")

path <-"data/outcome-of-care-measures.csv"

best <- function(state, outcome) {
  data <- read.csv("data/outcome-of-care-measures.csv")
  outcome_state <-subset(data, data$State==state)
  death_column <- paste("Hospital.30.Day.Death..Mortality..Rates.from.",outcome, sep = "")
  outcome_state_30 <- outcome_state[c(
    "Hospital.Name",  
    death_column
    )]
  outcome_state_30[death_column] <- as.numeric(outcome_state_30[[death_column]])
  outcome_state_30 <-  na.omit(outcome_state_30)

  subset(outcome_state_30, outcome_state_30[death_column]==min(outcome_state_30[death_column]))
}
#works

rankhospital <- function(state, outcome, num = "best") {
  data <- read.csv("data/outcome-of-care-measures.csv")
  outcome_state <-subset(data, data$State==state)
  death_column <- paste("Hospital.30.Day.Death..Mortality..Rates.from.",outcome, sep = "")
  outcome_state_30 <- outcome_state[c(
    "Hospital.Name",  
    death_column
  )]
  outcome_state_30[death_column] <- as.numeric(outcome_state_30[[death_column]])
  outcome_state_30 <-  na.omit(outcome_state_30)
  
  ordered <- order(outcome_state_30[death_column])
  data.frame(outcome_state_30[ordered, ], rank = as.numeric(factor(outcome_state_30[[death_column]][ordered])))
}
