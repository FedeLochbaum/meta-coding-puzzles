from typing import List
# Idea 1: DP + memo the minimum count of seconds
# Idea 2: A * exploring all the states
# Idea 3: Shortest path

def min_using_dp(ti, N, R, A, B, memo):
  val_prev, cur_index = ti
  if cur_index == N - 1: return 0 if R[cur_index] > val_prev else ((val_prev + 1) - R[cur_index]) * A
  
  key = tuple(ti)
  c_val = R[cur_index]
  next = R[cur_index + 1]

  if not key in memo:
    _min = float('inf')
    if c_val >= next:
      for j in range(val_prev + 1, c_val):
        # aca exploro todos los posibles de decrementar curr mientras sea mas grande que prev
        n_cost = (B * (c_val - j))
        _val = min_using_dp((j, cur_index + 1), N, R, A, B, memo)
        print('teniendo ti = ', ti, ' probamos decrementar con j: ', j, ' da como resultado un costo de ', n_cost, ' y _val: ', _val)
        _min = min(_min, n_cost + _val)
    else:
      for j in range(val_prev + 1, next):
        # aca se que i + 1 es mass grande que i, entonces, pruebo el minimo de incrementar i mientrasas seaa maas chico que i + i
        n_cost = (A * (j - c_val))
        _val = min_using_dp((j, cur_index + 1), N, R, A, B, memo)
        print('teniendo ti = ', ti, ' probamos incrementar con j: ', j, ' da como resultado un costo de ', n_cost, ' y _val: ', _val)
        _min = min(_min, n_cost + _val)

    memo[key] = _min

  return memo[key]

def getMinimumSecondsRequired(N: int, R: List[int], A: int, B: int) -> int:
  memo = {}
  va = min_using_dp((R[0], 1), N, R, A, B, memo)
  print('memo: ', memo)
  return va

r1 = getMinimumSecondsRequired(5, [2, 5, 3, 6, 5], 1, 1); print(r1, r1 == 5)

# r2 = getMinimumSecondsRequired(3, [100, 100, 100], 2, 3); print(r2, r2 == 5)

# r3 = getMinimumSecondsRequired(3, [100, 100, 100], 7, 3); print(r3, r3 == 9)

# r4 = getMinimumSecondsRequired(4, [6, 5, 4, 3], 10, 1); print(r4, r4 == 19)

# r5 = getMinimumSecondsRequired(4, [100, 100, 1, 1], 2, 1); print(r5, r5 == 207)

# r6 = getMinimumSecondsRequired(6, [6, 5, 2, 4, 4, 7], 1, 1); print(r6, r6 == 10)