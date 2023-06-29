from typing import List

def getMaxDamageDealt(N: int, H: List[int], D: List[int], B: int) -> float:
  ind = [0, 0] # curr, next
  dmg = [0, 0] # max, next

  for _ in range(20):
    for j in range(N):
      if ind[0] == j: continue
      di = D[ind[0]] * H[ind[0]]
      dj = D[j] * H[j]

      damage = di + dj + max(D[ind[0]] * H[j], D[j] * H[ind[0]])

      if damage > dmg[1]: dmg[1] = damage; ind[1] = j

    if dmg[1] > dmg[0]: dmg[0] = dmg[1]; ind[0] = ind[1]
    else: return dmg[0] / B
