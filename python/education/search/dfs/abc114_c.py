import pdb

N = int(input())
pool = set()

def dfs(s, count):
    if s != "" and not (1 <= int(s) <= N): return
    if s != "" and all(count):
        pool.add(s)
    dfs("7" + s, [True, count[1], count[2]])
    dfs("5" + s, [count[0], True, count[2]])
    dfs("3" + s, [count[0], count[1], True])

dfs("", [False, False, False])
print(len(pool))
