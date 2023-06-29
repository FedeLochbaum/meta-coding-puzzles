const getHitProbability = (R, C, G) => {
  let tbattleships = 0
  
  for (let i = 0; i < R; i++) {
    for (let j = 0; j < C; j++) {
      if (G[i][j] === 1) tbattleships += 1
    }
  }

  return tbattleships / (R * C)
}