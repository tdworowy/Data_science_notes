library(shiny)

shinyUI(fluidPage(
    titlePanel("Tabs"),
    sidebarLayout(
        sidebarPanel(
            textInput("box1","Enter text", value = "Tab1"),
            textInput("box2","Enter text", value = "Tab2"),
            textInput("box3","Enter text", value = "Tab3")
        ),
        mainPanel(
            tabsetPanel(type = "tabs",
                        tabPanel("Tab 1", br(), textOutput("out1")),
                        tabPanel("Tab 2", br(), textOutput("out2")),
                        tabPanel("Tab 3", br(), textOutput("out3"))
                        )
        )
    )
))
