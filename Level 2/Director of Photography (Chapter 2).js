const getArtisticPhotographCount = (N, C, X, Y) => {
  var res = 0
  const PSum = [0]
  const BSum = [0]
  const As = []
  
  for (var i = 0; i < C.length; i++) {
    if (C[i] === "P") PSum.push(PSum[PSum.length - 1]  + 1)
    else PSum.push(PSum[PSum.length - 1])
    
    if (C[i] === "B") BSum.push(BSum[BSum.length - 1] + 1)
    else BSum.push(BSum[BSum.length - 1])
    
    if (C[i] === 'A') As.push(i)
  }
  
  for (const a of As) {
    const Rwindow = [Math.max(0, Math.min(a + X, N)), Math.max(0, Math.min(a + Y + 1, N))]
    const Lwindow = [Math.max(0, Math.min(a - Y, N)), Math.max(0, Math.min(a - X + 1, N))]

    const leftPs = PSum[Lwindow[1]] - PSum[Lwindow[0]]
    const rightPs = PSum[Rwindow[1]] - PSum[Rwindow[0]]

    const rightBs = BSum[Rwindow[1]] - BSum[Rwindow[0]]
    const leftBs = BSum[Lwindow[1]] - BSum[Lwindow[0]]

    res += leftPs * rightBs
    res += leftBs * rightPs
  }

  return res
}