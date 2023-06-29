from typing import List

def getSecondsElapsed(C: int, N: int, A: List[int], B: List[int], K: int) -> int:
  tunnels = sorted([(A[i], B[i]) for i in range(N)])

  sum_tunnels = sum([B[i] - A[i] for i in range(N)])
  laps, remaining_time = divmod(K, sum_tunnels)

  if remaining_time == 0: return (laps - 1) * C + tunnels[-1][-1]

  for i in range(N):
    tunnel_length = tunnels[i][1] - tunnels[i][0]
    if tunnel_length >= remaining_time:
      return laps * C + tunnels[i][0] + remaining_time

    remaining_time -= tunnel_length
