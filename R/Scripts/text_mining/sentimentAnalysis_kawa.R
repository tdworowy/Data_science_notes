install.packages(c("sentimentr", "dplyr", "ggplot2","SnowballC","wordcloud","tm","dendextend"))

library("sentimentr")
library("dplyr")
library("stringr")
library("tm")
library("SnowballC")
library("wordcloud")
library("dendextend")
library("ggplot2")


coffee <- read.csv("Data\\text_mining\\text_mining_data\\coffee_tweets.csv",sep = ";")
res <- sentiment(coffee)
res <- sentiment_by(coffee)

coffee_source <- VectorSource(coffee$text)
coffee_corpus <- VCorpus(coffee_source)


clear_corpus <- function(corpus, words = ""){
  corpus <- tm_map(corpus, stripWhitespace)
  corpus <- tm_map(corpus, removePunctuation)
  corpus <- tm_map(corpus, content_transformer(tolower))
  corpus <- tm_map(corpus, removeNumbers)
  corpus <- tm_map(corpus, removeWords, c(stopwords("en"), words))
  return(corpus)
}

coffee_clear <- clear_corpus(coffee_corpus, "coffee")


coffee_clear[[]]$content


l<-c()
i=1

while(i<1000) {
  
    list_coffee<-c(l,coffee_clear[[i]]$content)
    i=i+1
}




coffee_tdm <- TermDocumentMatrix(coffee_clear)

dataFrame<-data.frame(text=unlist(sapply(coffee_clear, `[`, "content")), stringsAsFactors=F)


wynik_by <- sentiment_by(offee)
wynik_by <- sentiment_by(list_coffee)
wynik_by <- sentiment_by(dataFrame)
wynik_by <- sentiment_by(coffee_tdm)


plot(res)
plot(res_by)

ggplot(res_by, aes(element_id, ave_sentiment)) +
  geom_bar(stat = "identity") +
  theme_minimal() 

colors <- c("red4", "skyblue", "chartreuse2")



res_by%>%
#wynik%>%
  mutate(kolor = ifelse(ave_sentiment == 0, "Neutralna", ifelse(ave_sentiment < 0, "Negatywna", "Pozytywna"))) %>%
  ggplot(aes(element_id, ave_sentiment, fill = kolor, color = kolor)) +
  geom_bar(stat = "identity") +
  scale_fill_manual(values = moje_kolory) +
  scale_color_manual(values = moje_kolory) +
  labs(x = "Opinie", y = "Ocena sentymentu") +
  theme_minimal()