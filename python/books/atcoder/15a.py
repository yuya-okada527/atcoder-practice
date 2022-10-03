"""
abc61 B
"""
n, m = map(int, input().split())
G = [[] for _ in range(n)]
for _ in range(m):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    G[a].append(b)
    G[b].append(a)
for roads in G:
    print(len(roads))
