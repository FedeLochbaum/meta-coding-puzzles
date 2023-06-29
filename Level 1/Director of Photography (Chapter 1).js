const getArtisticPhotographCount = (N, C, X, Y) => {

  let res = 0
  const seen = { A: [], P: [], B: [] }
  
  for (var i = 0; i < C.length; i++) {
    const letter = C[i]
    
    if (letter === 'P') {
      for (var a_i = seen['A'].length - 1; a_i >= 0; a_i--) {
        const PAdist = Math.abs(seen['A'][a_i] - i)
        if (PAdist > Y) break
        if (PAdist < X) continue
        
        for (var b_i = seen['B'].length - 1; b_i >= 0; b_i--) {
          if (seen['B'][b_i] > seen['A'][a_i]) continue
          
          const ABdist = Math.abs(seen['A'][a_i] - seen['B'][b_i])
          if (ABdist < X) continue
          if (ABdist > Y) break

          res += 1
        }
      }
    }
    
    if (letter === 'B') {
      for (var a_i = seen['A'].length - 1; a_i >= 0; a_i--) {
        const BAdist = Math.abs(seen['A'][a_i] - i)
        if (BAdist > Y) break
        if (BAdist < X) continue
        
        for (var p_i = seen['P'].length - 1; p_i >= 0; p_i--) {
          if (seen['P'][p_i] > seen['A'][a_i]) continue

          const PAdist = Math.abs(seen['A'][a_i] - seen['P'][p_i])
          if (PAdist < X) continue
          if (PAdist > Y) break

          res += 1
        }
      }
    }
    
    if (letter !== '.') seen[letter].push(i)
  }
  
  return res
}
