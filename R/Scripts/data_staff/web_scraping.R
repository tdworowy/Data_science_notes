install.packages("rvest")
library(rvest)

# example1
url = "https://www.last.fm/pl/user/TotaledThomas/library/artists?date_preset=ALL"
html <- read_html(url)


values <- xml2::xml_find_all(html,"//a[@class='link-block-target']")

#example2
con = url("http://biostat.jhsph.edu/~jleek/contact.html")
htmlCode = readLines(con)

nchar(htmlCode[10])
