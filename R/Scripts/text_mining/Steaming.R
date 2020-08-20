words<-c( "argue", "argued", "argues", "arguing")

core <- stemDocument(words)
cire

dictionary <- c("argue")

complete_words <- stemCompletion(core, dictionary)
complete_words

stemDocument("John is argumentative. He argues about everything, yesterday was arguing for one penny")

text <- "John is argumentative. He argues about everything, yesterday was arguing for one penny"
text_punc <- removePunctuation(text)
words <- str_split(text_punc, ' ')

words

cores <- stemDocument(words[[1]]) 
cores <- stemDocument(unlist(words)) 
cores 

dictionary <- c("argue", "everything", "penny")

complete_words <- stemCompletion(cores, dictionary)
complete_words
complete_words <- stemCompletion(cores, unlist(words), type = "prevalent")
complete_words
