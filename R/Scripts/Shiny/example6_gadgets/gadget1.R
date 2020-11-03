library(shiny)
library(miniUI)

gadget1 <- function(){
  ui <- miniPage(
    gadgetTitleBar("Gadget 1")
  )
  server <- function(input, output, sesion){
    observeEvent(input$done, {
      stopApp()
    })
  }
  runGadget(ui, server)
}