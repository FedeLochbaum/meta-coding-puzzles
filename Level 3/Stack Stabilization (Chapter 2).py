
def get_moves(R, N):
  pivots = [[]] * N 
  for j in range(N-1, -1, -1):
    for i in range(j, -1, -1):
      v = R[j] - (j - i)
      if v > i: pivots[i].append(v)
    pivots[j].append(R[j])
    pivots[j].sort()
    pivots[j] = list(set(pivots[j]))

  return pivots

def min_using_dp(R, N, i, min_value, moves, A, B, memo):
  if i == N: return 0
  
  if not min_value in memo[i]:
    p = moves[i]
    p.append(min_value)
    _min = float('inf')

    for it in p:
      if it < min_value: continue

      cost = 0
      if it > R[i]: cost = (it - R[i]) * A
      if R[i] > it: cost = (R[i] - it) * B
      
      _min = min(_min, cost + min_using_dp(R, N, i + 1, it + 1, moves, A, B, memo))

    memo[i][min_value] = _min

  return memo[i][min_value]

def getMinimumSecondsRequired(N, R, A, B): return min_using_dp(R, N, 0, 1, get_moves(R, N), A, B, [{} for _ in range(N)])

r1 = getMinimumSecondsRequired(5, [2, 5, 3, 6, 5], 1, 1); print(r1, r1 == 5)

r2 = getMinimumSecondsRequired(3, [100, 100, 100], 2, 3); print(r2, r2 == 5)

r3 = getMinimumSecondsRequired(3, [100, 100, 100], 7, 3); print(r3, r3 == 9)

r4 = getMinimumSecondsRequired(4, [6, 5, 4, 3], 10, 1); print(r4, r4 == 19)

r5 = getMinimumSecondsRequired(4, [100, 100, 1, 1], 2, 1); print(r5, r5 == 207)

r6 = getMinimumSecondsRequired(6, [6, 5, 2, 4, 4, 7], 1, 1); print(r6, r6 == 10)
