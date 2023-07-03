from typing import List

def min_for(i, j, memo, R, A, B):
  prev = memo[i - 1][j - 1] if i > 0 else 0
  temp = prev + ((R[i] - j) * B if j < R[i] else (j - R[i]) * A)
  return min(memo[i][j - 1], temp) if j > i + 1 else temp

def getMinimumSecondsRequired(N: int, R: List[int], A: int, B: int) -> int:
  UPPER_BOUND = max(R) + N
  memo = [[0] * UPPER_BOUND for _ in range(N)]
  # memo[0][0] = float('inf')
  for i in range(N):
    for j in range(i + 1, UPPER_BOUND):
      memo[i][j] = min_for(i, j, memo, R, A, B)
      
  return memo[N - 1][UPPER_BOUND - 1]

r1 = getMinimumSecondsRequired(5, [2, 5, 3, 6, 5], 1, 1); print(r1, r1 == 5)

r2 = getMinimumSecondsRequired(3, [100, 100, 100], 2, 3); print(r2, r2 == 5)

r3 = getMinimumSecondsRequired(3, [100, 100, 100], 7, 3); print(r3, r3 == 9)

r4 = getMinimumSecondsRequired(4, [6, 5, 4, 3], 10, 1); print(r4, r4 == 19)

r5 = getMinimumSecondsRequired(4, [100, 100, 1, 1], 2, 1); print(r5, r5 == 207)

r6 = getMinimumSecondsRequired(6, [6, 5, 2, 4, 4, 7], 1, 1); print(r6, r6 == 10)
