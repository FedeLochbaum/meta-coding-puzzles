const getMinProblemCount = (N, S) => {

  var there_odd = false
  var max_min_even_count = 0
  for (var i = 0; i < S.length; i++) {
    max_min_even_count = Math.max(max_min_even_count, Math.floor(S[i] / 2))
    if ((S[i] % 2) === 1) there_odd = true
  }
  
  return max_min_even_count + (there_odd ? 1 : 0)
}