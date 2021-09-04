from collections import defaultdict

N, K = map(int, input().split())
C = list(map(int, input().split()))

d = defaultdict(int)
for i in range(K):
    d[C[i]] += 1
ans = len(d)
for i in range(1, N-K+1):
    d[C[i-1]] -= 1
    d[C[i+K-1]] += 1
    if d[C[i-1]] == 0:
        d.pop(C[i-1])
    ans = max(ans, len(d))

print(ans)