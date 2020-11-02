library(shiny)

shinyUI(fluidPage(
  titlePanel("Visualize"),
  sidebarLayout(
        sidebarPanel(
            h3("Slope"),
            textOutput("SlopeOut"),
            h3("Intercept"),
            textOutput("intOut")
        ),    
        mainPanel(
            plotOutput("plot1", brush =  brushOpts(
                id = "brush1"
            ))
        )
    )
))
