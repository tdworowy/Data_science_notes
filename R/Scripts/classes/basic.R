getS3method("mean","default") # default mean method(old S3 style)


# new class (new S4 style)

setClass("Mypolygon",
         representation(x = "numeric",
                        y = "numeric"))
# plot is generic function
setMethod("plot","Mypolygon",
          function(x,y,...){
            plot(x@x,x@y, type="n", ...)
            xp <- c(x@x, x@x[1])
            yp <- c(x@y, x@y[1])
            lines(xp,yp)
          })


showMethods("plot")


polygon_obj <- new("Mypolygon", x=c(1,2,3,4),y=c(1,2,3,1))
plot(polygon_obj)

getMethod("plot","Mypolygon") # get method code 