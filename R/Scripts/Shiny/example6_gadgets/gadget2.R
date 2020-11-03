library(shiny)
library(miniUI)

gadget2 <- function(numbers1, numbers2){
  ui <- miniPage(
    gadgetTitleBar("Multiplication"),
    miniContentPanel(
      selectInput("num1", "first number", choices = numbers1),
      selectInput("num2", "second number", choices = numbers2)
    )
  )
  server <- function(input, output, sesion){
    observeEvent(input$done, {
      num1 <- as.numeric(input$num1)
      num2 <- as.numeric(input$num2)
      stopApp(num1 * num2)
    })
  }
  runGadget(ui, server)
}