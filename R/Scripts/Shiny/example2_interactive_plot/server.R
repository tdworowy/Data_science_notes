
library(shiny)


shinyServer(function(input, output) {
    output$plot1 <- renderPlot({
      number_of_points <- input$numeric
      
      minX <- input$sliderX[1]
      maxX <- input$sliderX[2]
      minY <- input$sliderY[1]
      maxY <- input$sliderY[2]
      
      dataX <- runif(number_of_points, minX, maxX)
      dataY <- runif(number_of_points, minY, maxY)
      
      xlab <- ifelse(input$Xlab, "X axis", "")
      ylab <- ifelse(input$ylab, "Y axis", "")
      main <- ifelse(input$title, "Title", "")
      
      plot(dataX, dataY, xlab = xlab, ylab = ylab, main = main,
           xlim = c(-100,100), ylim = c(-100, 100))
    })
  
})
