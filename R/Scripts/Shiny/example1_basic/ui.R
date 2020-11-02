library(shiny)

shinyUI(fluidPage(
    titlePanel("Title: example1"),
    sidebarLayout(
        sidebarPanel(
            h3("Move the Slider"),
            sliderInput("slider1", "Silide it",0,100,0)
        ),
        mainPanel(
            h3("Slider Value:"),
            textOutput("text1")
        
        )
    )
))