const getSecondsRequired = (N, F, P) => {
  const sorted = P.sort((a, b) => a - b)
  var res = N - sorted[F - 1]
  var prev = sorted[F - 1]

  for (var i = F - 2; i >= 0; i--) {
    res += (prev - sorted[i]) - 1
    prev = sorted[i]
  }
  
  return res + (F - 1)
}