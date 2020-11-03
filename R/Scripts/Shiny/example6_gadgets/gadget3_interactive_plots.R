library(shiny)
library(miniUI)

gadget3 <- function(){
  ui <- miniPage(
    gadgetTitleBar("Select points by draging your mouse"),
    miniContentPanel(
     plotOutput("plot", height = "100%", brush = "brush")
    )
  )
  server <- function(input, output, sesion){
    output$plot <- renderPlot({
      plot(trees$Girth, trees$Volume, main = "Trees",
           xlab = "Girth", ylab = "Volume")
    })
    observeEvent(input$done, {
      stopApp(
        brushedPoints(trees, input$brush,
                      xvar = "Girth", yvar= "Volume")
      )
    })
  }
  runGadget(ui, server)
}
