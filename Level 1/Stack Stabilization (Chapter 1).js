const getMinimumDeflatedDiscCount = (N, R) => {
  var res = 0
  var prev = R[R.length - 1]
  if (R.length === 1) return 0
  for (var i = R.length - 2; i >= 0; i--) {
    if (R[i] < prev) { prev = R[i]; continue }
    
    if (prev === 1) return -1
    
    res += 1; prev -= 1
  }

  return res
}