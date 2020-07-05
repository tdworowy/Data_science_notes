#bar plot
data("iris")


data <- matrix()
for (Species in iris[["Species"]]) {
  sum(iris["Species"] == Species)
  data[Species] <- sum(iris["Species"] == Species)
}
barplot(data)