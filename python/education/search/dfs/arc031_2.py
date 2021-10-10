import pdb
from pprint import pprint

from copy import deepcopy

A = [list(input()) for _ in range(10)]

def dfs(i, j, maps, another_map, visited):
    if not (0 <= i < 10) or not (0 <= j < 10): return
    if maps[i][j] == "x": return
    if visited[i][j]: return
    visited[i][j] = True
    another_map[i][j] = "o"
    print("maps")
    pprint(maps)
    print()
    print("another_map")
    pprint(another_map)
    print()
    print("visited")
    pprint(visited)
    pdb.set_trace()
    dfs(i+1, j, maps, another_map, visited)
    dfs(i-1, j, maps, another_map, visited)
    dfs(i, j+1, maps, another_map, visited)
    dfs(i, j-1, maps, another_map, visited)


for i in range(10):
    for j in range(10):
        maps = deepcopy(A)
        maps[i][j] = "o"
        visited = [
            [False for _ in range(10)] for _ in range(10)
        ]
        another_map = [
            ["x" for _ in range(10)] for _ in range(10)
        ]
        dfs(0, 0, maps, another_map, visited)
        if maps == another_map:
            print("Yes")
            exit()
print("No")
