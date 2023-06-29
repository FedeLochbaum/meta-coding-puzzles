from typing import List

def minimum_of(source, to, N):
  return min(max(source, to) - min(source, to), N - max(source, to) + min(source, to))

def solve(N, M, C):
  current = [minimum_of(1, C[0], N)]
  for i in range(1, M):
    current.append(current[0] + minimum_of(1, C[i], N))

    for j in range(1, i): current[i] = min(current[i], current[j] + minimum_of(C[j - 1], C[i], N))

    inc = minimum_of(C[i - 1], C[i], N)
    for j in range(i): current[j] += inc

  return min(current)

def getMinCodeEntryTime(N: int, M: int, C: List[int]) -> int:
  return solve(N, M, C)
