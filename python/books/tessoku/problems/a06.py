n, q = map(int, input().split())
A = [0] + list(map(int, input().split()))
Z = [0 for _ in range(n+1)]
for i in range(1, n+1):
    Z[i] = Z[i-1] + A[i]
LR = []
for _ in range(q):
    l, r = map(int, input().split())
    LR.append((l, r))
for l, r in LR:
    ans = Z[r] - Z[l-1]
    print(ans)
