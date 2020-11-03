install.packages("googleVis")
library(googleVis)

graph <- gvisMotionChart(Fruits, "Fruit", "Year")
plot(graph)

print(graph, file = "graph.html")