const getMinCodeEntryTime = (N, M, C) => {

  var res = 0
  var current = 1
  for (i = 0; i < C.length; i++) {
    if (C[i] === current) continue
    
    const dist_forward = C[i] > current ? C[i] - current : ((N - current) + C[i])
    const dist_backward = C[i] > current ? (N + current) - C[i] : current - C[i]
    res += Math.min(dist_forward, dist_backward)
    current = C[i]
  }

  return res
}