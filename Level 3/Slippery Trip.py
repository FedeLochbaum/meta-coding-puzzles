from typing import List
from collections import deque

DIR = { 'DOWN': 'v', 'RIGHT': '>' }

def next_pos(R, C, pos, dir):
  return ((pos[0] + 1) % R, pos[1]) if dir == DIR['DOWN'] else (pos[0], (pos[1] + 1) % C)

def coins(R, C, G):
  _coins = 0
  pos = (0, 0)
  visited = set()
  dir = DIR['DOWN']

  while not pos in visited:
    visited.add(pos)
    cell = G[pos[0]][pos[1]]

    if cell != '.':
      if cell == '*': _coins += 1
      else: dir = dir = cell

    if pos[0] == R - 1 and dir == DIR['DOWN']: break
    pos = next_pos(R, C, pos, dir)

  return _coins

def count_of_coins(R, C, G):
  _coins = 0
  for i in range(R):
    G[i] = deque(G[i])
    for j in range(C):
      if G[i][j] == '*': _coins += 1
  
  return _coins

def getMaxCollectableCoins(R, C, G):
  _max_possible = count_of_coins(R, C, G)
  _max = 0

  for r in range(R):
    for n in range(C + 1):
      _max = max(_max, coins(R, C, G))
      if (_max == _max_possible): return _max_possible
      G[r].rotate(1)

  return _max

G1 = [
  ['.','*','*','*'],
  ['*','*','v','>'],
  ['.','*','.','.']
]

G2 = [ [ '>', '*', '*' ], [ '*', '>', '*' ], [ '*', '*', '>' ] ]

G3 = [ [ '>', '>' ], [ '*', '*' ] ]

G4 = [
  [ '>', '*', 'v', '*', '>', '*' ],
  [ '*', 'v', '*', 'v', '>', '*' ],
  [ '.', '*', '>', '.', '.', '*' ],
  [ '.', '*', '.', '.', '*', 'v' ]
]

r1 = getMaxCollectableCoins(3, 4, G1); print(r1, r1 == 4)

r2 = getMaxCollectableCoins(3, 3, G2); print(r2, r2 == 4)

r3 = getMaxCollectableCoins(2, 2, G3); print(r3, r3 == 0)

r4 = getMaxCollectableCoins(4, 6, G4); print(r4, r4 == 6)
