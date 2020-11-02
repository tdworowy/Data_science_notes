library(shiny)

shinyUI(fluidPage(
    titlePanel("Title: example2"),
    sidebarLayout(
        sidebarPanel(
            numericInput("numeric", "count of random numbers",
                         value = 100, min = 1, max = 1000, step = 1),
            
            sliderInput("sliderX", "Pick min and max X value",
                        -100, 100, value = c(-50, 50)),
            sliderInput("sliderY", "Pick min and max Y value",
                        -100, 100, value = c(-50, 50)),
            
            checkboxInput("Xlab", "show/hide", value = TRUE),
            checkboxInput("ylab", "show/hide", value = TRUE),
            checkboxInput("title", "show/hide", value = TRUE)
            
        ),
        mainPanel(
            h3("Plot"),
           plotOutput("plot1")
        
        )
    )
))