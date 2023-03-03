n, q = map(int, input().split())
A = list(map(int, input().split()))
Z = [0 for _ in range(n+1)]
for i in range(1, n+1):
    Z[i] = Z[i-1] + A[i-1]
LR = []
for _ in range(q):
    l, r = map(int, input().split())
    LR.append((l, r))
for l, r in LR:
    print(Z[r] - Z[l-1])
