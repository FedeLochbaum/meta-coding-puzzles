from typing import List

CELL = { 'DOWN': 'v', 'RIGHT': '>', 'COIN': '*', 'EMPTY': '.' }

def res_by_analysis(there_coin, there_is_down, max_possible_before_down, next):
  if max_possible_before_down != 0: return max_possible_before_down + next()
  elif there_coin: return 1 + next()
  elif there_is_down: return next()

  return 0

def max__coins(R, G, r):
  if r == R: return 0
  
  row = G[r] * 2

  there_coin = False
  there_is_down = False
  there_is_right = False
  move_right = False
  max_possible_before_down = 0
  coins_before_down = 0
  all_coins_in_row = 0
  
  for i in row:
    if i == CELL['EMPTY']: there_is_down = True

    if i == CELL['COIN']:
      all_coins_in_row += 1
      there_coin = True
      if move_right: coins_before_down += 1
    elif i == CELL['DOWN']:
      there_is_down = True
      if move_right:
        max_possible_before_down = max(max_possible_before_down, coins_before_down)
        coins_before_down = 0; move_right = False
    elif i == CELL['RIGHT']: there_is_right = True; move_right = True
  
  res = res_by_analysis(there_coin, there_is_down, max_possible_before_down, lambda : max__coins(R, G, r + 1))

  if max_possible_before_down == 0 and there_is_right: res = max(res, all_coins_in_row // 2)
  
  return res

def getMaxCollectableall_coins_in_row(R, C, G):
  return max__coins(R, G, 0)

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

r1 = getMaxCollectableall_coins_in_row(3, 4, G1); print(r1, r1 == 4)

r2 = getMaxCollectableall_coins_in_row(3, 3, G2); print(r2, r2 == 4)

r3 = getMaxCollectableall_coins_in_row(2, 2, G3); print(r3, r3 == 0)

r4 = getMaxCollectableall_coins_in_row(4, 6, G4); print(r4, r4 == 6)
