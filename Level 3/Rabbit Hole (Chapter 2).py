from typing import List
from collections import defaultdict
from collections import deque

def strongest_components(N, edges):
  stack = []
  on_stack = [False] * N
  ids = [None] * N
  low = [None] * N
  cur_id = 0
  cycles = {}
  num_cycles = 0

  def dfs(i):
    nonlocal cur_id, num_cycles
    dfs_stack = [i]
    while dfs_stack:
      i = dfs_stack[-1]
      if not on_stack[i]: stack.append(i); on_stack[i] = True
      if ids[i] is None: ids[i] = cur_id; low[i] = cur_id; cur_id += 1
      for j in edges[i]:
        if ids[j] is None: dfs_stack.append(j); break
        if on_stack[j]: low[i] = min(low[i], low[j])

      if dfs_stack[-1] != i: continue

      if ids[i] == low[i]:
        cur_cycle = set()
        while on_stack[i]:
          j = stack.pop()
          low[j] = low[i]
          on_stack[j] = False
          cur_cycle.add(j)
        cycles[num_cycles] = cur_cycle
        num_cycles += 1
      dfs_stack.pop()

  for i in range(N):
    if ids[i] is None: dfs(i)

  return cycles.items(), lambda i : len(cycles[i]), num_cycles

def getMaxVisitableWebpages(N: int, M: int, A: List[int], B: List[int]) -> int:
  graph = defaultdict(set)
  reverse_graph = defaultdict(set)
  for a, b in zip(A, B): graph[a - 1].add(b - 1); reverse_graph[b - 1].add(a - 1)

  components, node_size, num_cycles = strongest_components(N, graph)

  map_ids = {
    old_id: new_id for new_id, old_ids in components for old_id in old_ids
  }

  graph_2 = defaultdict(set)
  for k, v in graph.items():
    n_k = map_ids[k]
    n_v = {map_ids[id] for id in v}
    n_v.discard(n_k)
    graph_2[n_k].update(n_v)

  indegrees = [0]*num_cycles
  for k, v in graph_2.items():
    for id in v: indegrees[id] += 1

  queue = deque([i for i, c in enumerate(indegrees) if c == 0])
  longest_path = [node_size(i) for i in range(num_cycles)]
  while queue:
    i = queue.popleft()
    for j in graph_2[i]:
      longest_path[j] = max(longest_path[j], longest_path[i] + node_size(j))
      indegrees[j] -= 1
      if indegrees[j] == 0: queue.append(j)

  return max(longest_path)
