install.packages(c("stringr", "tm", "SnowballC", "wordcloud"))
library("stringr")
library("tm")
library("SnowballC")
library("wordcloud")


install.packages("qdap")
library("qdap")


install.packages(c("tm", "dendextend", "ggplot2"))
library("dendextend")
library("ggplot2")


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

dirNeg <-paste0("Data/text_mining/text_mining_data/recenzje/neg")
dirPos <-paste0("Data/text_mining/text_mining_data/recenzje/pos")

source_dir1 <- DirSource(dirNeg)
source_dir2 <- DirSource(dirPos)

recCorp <- VCorpus(source_dir1,source_dir2)


recCorpClean <-czysc_korpus(recCorp,stopwords("en")) 

termDMatrix <- TermDocumentMatrix(recCorpClean )
termDMatrix2 <- TermDocumentMatrix(recCorpClean ,control=list(weight=weightTfIdf))
termDMatrix3 <- TermDocumentMatrix(recCorpClean ,control=list(weight=weightBin))  
termDMatrix4 <- TermDocumentMatrix(recCorpClean ,control=list(weight=weightTf))  
termDMatrix5 <- TermDocumentMatrix(recCorpClean ,control=list(weight=weightSMART)) 

termDMatrixAfterRemove <-removeSparseTerms(termDMatrix ,.95)
termDMatrixAfterRemove2 <-removeSparseTerms(termDMatrix2 ,.95)
termDMatrixAfterRemove3 <-removeSparseTerms(termDMatrix3 ,.95)
termDMatrixAfterRemove4 <-removeSparseTerms(termDMatrix4 ,.95)
termDMatrixAfterRemove5 <-removeSparseTerms(termDMatrix5 ,.95)

termMatrix  <- as.matrix(termDMatrixAfterRemove )
termMatrix2  <- as.matrix(termDMatrixAfterRemove2 )
termMatrix3  <- as.matrix(termDMatrixAfterRemove3 )
termMatrix4  <- as.matrix(termDMatrixAfterRemove4 )
termMatrix5  <- as.matrix(termDMatrixAfterRemove5 )

rec_term <- rowSums(termMatrix )
rec_term <- sort(rec_term, decreasing = TRUE)

rec_term2 <- rowSums(termMatrix2 )
rec_term2 <- sort(rec_term2, decreasing = TRUE)


rec_term3 <- rowSums(termMatrix3 )
rec_term3 <- sort(rec_term3, decreasing = TRUE)

rec_term4 <- rowSums(termMatrix4 )
rec_term4 <- sort(rec_term4, decreasing = TRUE)

rec_term5 <- rowSums(termMatrix5 )
rec_term5 <- sort(rec_term5,decreasing = TRUE)


barplot(rec_term[1:20], col = "forestgreen", las = 2)
barplot(rec_term2[1:20], col = "forestgreen", las = 2)
barplot(rec_term3[1:20], col = "forestgreen", las = 2)
barplot(rec_term4[1:20], col = "forestgreen", las = 2)
barplot(rec_term5[1:20], col = "forestgreen", las = 2)

