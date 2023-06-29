const getMaximumEatenDishCount = (N, D, K) => {
  var t_eaten = 0
  const last_eaten = Array(K) // buffer which one insert using % with t_eaten
  const in_range = {} // Id -> n

  for (var i = 0; i < D.length; i++) {
    if (in_range[D[i]] && in_range[D[i]] > 0) continue
    
    // can eat it
    in_range[last_eaten[t_eaten % K]] = in_range[last_eaten[t_eaten % K]] || 0
    in_range[last_eaten[t_eaten % K]] -= 1
    last_eaten[t_eaten % K] = D[i]
    in_range[D[i]] = in_range[D[i]] || 0
    in_range[D[i]] += 1
    t_eaten += 1
  }

  return t_eaten
}