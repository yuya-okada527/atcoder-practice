from itertools import permutations

N, K = map(int, input().split())
T = [list(map(int, input().split())) for _ in range(N)]

ans = 0
for p in permutations(list(range(1, N))):
    temp = 0
    p = list(p)
    p.insert(0, 0)
    p.append(0)
    for i in range(len(p)-1):
        temp += T[p[i]][p[i+1]]
    if temp == K:
        ans += 1
print(ans)
