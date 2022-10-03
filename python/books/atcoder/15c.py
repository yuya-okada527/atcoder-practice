"""
abc166 C
"""
n, m = map(int, input().split())
H = list(map(int, input().split()))
G = [[] for _ in range(n)]
for _ in range(m):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    G[a].append(b)
    G[b].append(a)
ans = 0
for i, edeges in enumerate(G):
    is_peak = True
    for j in edeges:
        if H[i] <= H[j]:
            is_peak = False
    if is_peak:
        ans += 1
print(ans)
