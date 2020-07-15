install.packages("rvest")
library(rvest)

url = "https://www.last.fm/pl/user/TotaledThomas/library/artists?date_preset=ALL"
html <- read_html(url)


values <- xml2::xml_find_all(html,"//a[@class='link-block-target']")

