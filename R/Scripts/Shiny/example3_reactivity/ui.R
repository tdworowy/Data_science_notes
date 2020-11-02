library(shiny)

shinyUI(fluidPage(
    titlePanel("Predict horsepower from MPG"),
    sidebarLayout(
        sidebarPanel(
            sliderInput("sliderMPG", "Car MPG", 10, 35, value = 20),
            checkboxInput("showModel1", "Show/Hide", value = TRUE),
            checkboxInput("showModel2", "Show/Hide", value = TRUE),
            submitButton("submit") # run reactive functions comment it to run them by data change
        ),
        mainPanel(
            plotOutput("plot1"),
            h3("Predicted Horsepowet from Model1: "),
            textOutput("pred1"),
            h3("Predicted Horsepowet from Model2: "),
            textOutput("pred2")
        )
    )
))
