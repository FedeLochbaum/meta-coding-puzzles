from typing import List

def getMinProblemCount(N: int, S: List[int]) -> int:
  _max = max(S)
  
  if _max % 3 == 0: return _max // 3 + int(any(x % 3 != 0 for x in S))

  if _max % 3 == 1 and 1 not in S and _max-1 not in S: return _max // 3 + 1
  
  return _max // 3 + int(any(x % 3 == 1 for x in S)) + int(any(x % 3 == 2 for x in S))
