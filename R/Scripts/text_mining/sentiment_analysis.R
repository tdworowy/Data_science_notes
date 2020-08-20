setwd("C:/Users/Thomas/Dysk Google/Studia_magister/Semestr3/TextMining/recenzje")

library("sentimentr")


tekst <- c("Bought it as a random gift for my daughter and she loves it!!!!!",
           "I bought this for my daughter and family. Everybody loves Alexa!",
           "Pretty disappointing. It's pretty worthless.",
           "Disappointing and frustrating ? I'm returning Echo")

extract_sentiment_terms(tekst)

get_sentences(tekst)

wynik <- sentiment(tekst)
wynik
plot(wynik)
plot(wynik$sentiment/sum(abs(wynik$sentiment))*100, type = "l")

wynik_by <- sentiment_by(tekst)
plot(wynik_by)

ggplot(wynik_by, aes(element_id, ave_sentiment)) +
  geom_bar(stat = "identity") +
  labs(title = "Analiza nastrojów opinii", x = "Opinie", y = "Ocena sentymentu") +
  theme_minimal()