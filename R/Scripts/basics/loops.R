m <- matrix(1:15,3,4)
for(i in seq_len(nrow(m))){
  for(j in seq_len(ncol(m))){
    print(m[i,j])
  }
}