install.packages("tm")
library(tm)

clear_corpus <- function(Corpus, words){
  data <- data.frame(text=unlist(lapply(Corpus, `[`, "content")),stringsAsFactors=F)
  
  temp <-removeWords(data[1,], words )
  for(i in 2:nrow(data)){
    temp <-append(temp ,removeWords(data[i,], words) ,after = i+1)
    }
 
  temp <- stripWhitespace(temp)
  temp <- removePunctuation(temp)
  temp <- removeNumbers(temp)
  
  source  <- VectorSource(temp)
  clean <- VCorpus(source)
  
}

coffee <- read.csv("Data\\text_mining\\text_mining_data\\coffee_tweets.csv",sep = ";")
coffee_source <- VectorSource(coffee$text)
coffee_coprus <- VCorpus(coffee_source)
coffee_clear <- clear_corpus(coffee_coprus, stopwords("en"))
coffee_clear[[1]]$content