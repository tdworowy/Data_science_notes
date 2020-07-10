
make_cache_matrix <- function(x = matrix()) {
  inv <- NULL
  set <- function(y) {
    x <<- y
    i <<- NULL
  }
  get <- function() x
  set_invers <- function(invers) inv <<- invers
  get_invers <- function() inv
  list(set = set, get = get,
       set_invers = set_invers,
       get_invers = get_invers)
}

cache_solve <- function(x) {
  inv <- x$get_invers()
  if(!is.null(inv)) {
    return(inv)
  }
  data <- x$get()
  inv <- solve(data)
  x$set_invers(inv)
  inv
}
