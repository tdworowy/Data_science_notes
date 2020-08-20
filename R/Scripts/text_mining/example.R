library(tm)

text <- c("Bought it as a random gift for my daughter and she loves it!!!!!",
           "I bought this for my daughter and family. Everybody loves Alexa!",
           "Pretty disappointing . It's pretty worthless.",
           "Disappointing and frustrating ? I'm returning Echo")

source <- VectorSource(text)
corpus <- VCorpus(source)

corpus <- tm_map(corpus, content_transformer(tolower))
corpus <- tm_map(corpus, removeNumbers)
corpus <- tm_map(corpus, removeWords,stopwords("en"))
corpus <- tm_map(corpus, stemDocument)
corpus <- tm_map(corpus, removePunctuation)
corpus <- tm_map(corpus, stripWhitespace)