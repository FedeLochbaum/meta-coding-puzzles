from typing import List
from collections import deque

def getSecondsRequired(R: int, C: int, G: List[List[str]]) -> int:
  # dijkstra, basically
  directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]  # right, left, down, up
  portals = {}
  visited = {}
  exits = []
  distances = [[float('inf')] * C for _ in range(R)]
  queue = deque()

  for i in range(R):
    for j in range(C):
      char = G[i][j]
      if char == 'E': exits.append((i, j))
      if char == 'S':
        distances[i][j] = 0
        queue.append((i, j))
      elif char != '.' and char != '#':
        if char not in portals: portals[char] = []
        portals[char].append((i, j))

  # Apply dijkstra
  while queue:
    x, y = queue.popleft()
    if (x, y) in visited: continue
    visited[(x, y)] = True
    
    if (G[x][y] != '.' and G[x][y] != '#' and G[x][y] != 'S'):
      for nx, ny in portals[G[x][y]]:
        jump = distances[x][y] + 1
        if (jump < distances[nx][ny]):
          distances[nx][ny] = jump
          queue.append((nx, ny))

    for dx, dy in directions:
      nx, ny = x + dx, y + dy
      if 0 <= nx < R and 0 <= ny < C and G[nx][ny] != '#':
        move = distances[x][y] + 1
        if (move < distances[nx][ny]):
          distances[nx][ny] = move
          queue.append((nx, ny))

  _min = float('inf')
  for ex, ey in exits: _min = min(_min, distances[ex][ey])
  
  return -1 if _min == float('inf') else _min