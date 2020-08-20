install.packages(c("stringr", "tm", "SnowballC", "wordcloud"))
install.packages("tm")
library("stringr")
library("tm")
library("SnowballC")
library("wordcloud")

install.packages(c("tm", "dendextend", "ggplot2"))
library("dendextend")
library("ggplot2")


coffee <- read.csv("Data\\text_mining\\text_mining_data\\coffee_tweets.csv",sep = ";")
kawa_zrodlo <- VectorSource(kawa$text)
kawa_korp <- VCorpus(kawa_zrodlo)


clear_corpus <- function(corpus, slowa = ""){
  corpus <- tm_map(corpus, stripWhitespace)
  corpus <- tm_map(corpus, removePunctuation)
  corpus <- tm_map(corpus, content_transformer(tolower))
  corpus <- tm_map(corpus, removeNumbers)
  corpus <- tm_map(corpus, removeWords, c(stopwords("en"), slowa))
  return(corpus)
}

coffee_clear <- clear_corpus(kawa_korp, "coffee")

coffee_tdm <- TermDocumentMatrix(coffee_clear)
str(coffee_tdm)

coffee_m <- as.matrix(coffee_tdm)
summary(coffee_m)
str(coffee_m)
coffee_term <- rowSums(coffee_m)
summary(coffee_term)
str(coffee_term)

inspect(coffee_tdm)
inspect(coffee_tdm[1000:1015 ,300:310])
inspect(coffee_tdm['gold' ,300:310])
inspect(coffee_tdm['gold' ,])
inspect(coffee_tdm[ ,1])
inspect(coffee_tdm[1 ,])


dim(kawa_tdm)
dim(kawa_m)
kawa_term
dim(kawa_term)


kawa_term <- sort(kawa_term, decreasing = TRUE)
kawa_term[1:6]
head(kawa_term)

barplot(kawa_term[1:20], col = "tan", las = 2)

wordcloud(names(kawa_term), kawa_term, max.words = 50, colors = "steelblue4")

______________________
Herbata


herbata <- read.csv2("tea_tweets.csv")
herbata_zrodlo <- VectorSource(herbata$text)
herbata_korp <- VCorpus(herbata_zrodlo)

herbata_czysty <- czysc_korpus(herbata_korp, c("tea","teatime","https","https...","httpst...","httpstcoizrgozu"))

herbata_tdm <- TermDocumentMatrix(herbata_czysty)
herbata_m <- as.matrix(herbata_tdm)

herbata_term <- rowSums(herbata_m)
herbata_term <- sort(herbata_term, decreasing = TRUE)

wordcloud(names(herbata_term), herbata_term, max.words = 50, colors = "steelblue4")

--------------------
kawaTekst <- paste(kawa$text, collapse = " ")
herbataTekst <- paste(herbata$text, collapse = " ")

razemTekst <- c(kawaTekst, herbataTekst)
str(razemTekst)
razem_source <- VectorSource(razemTekst)
razem_korp <- VCorpus(razem_source)


razem_czysty <- czysc_korpus(razem_korp, c("coffee", "teatime", "tea"))

razem_tdm <- TermDocumentMatrix(razem_czysty)

razem_m <- as.matrix(razem_tdm)
commonality.cloud(razem_m, max.words = 50, colors = "steelblue4")


razem_tdm_nazwy <- razem_tdm
colnames(razem_tdm_nazwy) <- c("kawa", "herbata")
razem_m_nazwy <- as.matrix(razem_tdm_nazwy)

comparison.cloud(razem_m_nazwy, max.words = 50, colors = c("orangered3", "darkolivegreen3"))


_____________________________

slowa<-c( "argue", "argued", "argues", "arguing")

rdzen <- stemDocument(slowa)
rdzen

slownik <- c("argue")

kompletne_slowa <- stemCompletion(rdzen, slownik)
kompletne_slowa

stemDocument("John is argumentative. He argues about everything, yesterday was arguing for one penny")

tekst <- "John is argumentative. He argues about everything, yesterday was arguing for one penny"
tekst_punc <- removePunctuation(tekst)
slowa <- str_split(tekst_punc, ' ')

slowa

rdzenie <- stemDocument(slowa[[1]]) 
rdzenie <- stemDocument(unlist(slowa)) #r?nowa?ne 
rdzenie 

slownik <- c("argue", "everything", "penny")

kompletne_slowa <- stemCompletion(rdzenie, slownik)
kompletne_slowa
kompletne_slowa <- stemCompletion(rdzenie, unlist(slowa), type = "prevalent")
kompletne_slowa

_____________________



install.packages("tm")
library("tm")

tekst <- c("Bought it as a random gift for my daughter and she loves it!!!!!",
           "I bought this for my daughter and family. Everybody loves Alexa!",
           "Pretty disappointing . It's pretty worthless.",
           "Disappointing and frustrating ? I'm returning Echo")

zrodlo <- VectorSource(tekst)
korpus <- VCorpus(zrodlo)

korpus <- tm_map(korpus, content_transformer(tolower))
korpus <- tm_map(korpus, removeNumbers)
korpus <- tm_map(korpus, removeWords,stopwords("en"))
korpus <- tm_map(korpus, stemDocument)
korpus <- tm_map(korpus, removePunctuation)
korpus <- tm_map(korpus, stripWhitespace)


termMatrix <- TermDocumentMatrix(korpus )
termMatrix 
inspect(termMatrix)

term_m <- as.matrix(termMatrix)
term <- rowSums(term_m)
term <- sort(term , decreasing = TRUE)

barplot(term , col = "tan", las = 2)

help(TermDocumentMatrix)
termMatrix2 <- TermDocumentMatrix(korpus) # pwinna by? jaka? lista argumetnow kontrolnych
termMatrix3 <- TermDocumentMatrix(korpus)

--------------------------
#gropowanie

tekst <- c("Bought it as a random gift for my daughter and she loves it!!!!!",
           "I bought this for my daughter and family. Everybody loves Alexa!",
           "Pretty disappointing . It's pretty worthless.",
           "Disappointing and frustrating ? I'm returning Echo")

zrodlo <- VectorSource(tekst)
korpus <- VCorpus(zrodlo)

korpus <- tm_map(korpus, content_transformer(tolower))
korpus <- tm_map(korpus, removeNumbers)
korpus <- tm_map(korpus, removeWords,stopwords("en"))
korpus <- tm_map(korpus, stemDocument)
korpus <- tm_map(korpus, removePunctuation)
korpus <- tm_map(korpus, stripWhitespace)

termMatrix <- TermDocumentMatrix(korpus )
termMatrix 

term_m <- as.matrix(termMatrix)
term_dist <- dist(term_m)

term_dist

term_clust <- hclust(term_dist)
term_clust
plot(term_clust)


termMatrix2 <- DocumentTermMatrix(korpus)
inspect(termMatrix2) 
term_m2 <- as.matrix(termMatrix2)
term_dist2 <- dist(term_m2)


term_clust2 <- hclust(term_dist2)
plot(term_clust2)
_____________________

'SnowballC

slowa<-c( "argue", "argued", "argues", "arguing")

rdzen <- stemDocument(slowa)
rdzen



